# coding=utf-8
"""Tyko library."""
__version__ = '0.1rc6'

from typing import List

import logging
import netrc
import os
import re
import queue
import json
import time
import threading
import multiprocessing
from urllib.parse import urlparse

try:
    from multiprocessing.shared_memory import SharedMemory
except ImportError:
    from shared_memory import SharedMemory

from typing import Dict
from urllib.parse import urljoin

import requests
import unicodedata
from unidecode import unidecode

logger = logging.getLogger(__name__)


_TYKO_KEY = 'TYKO_KEY'
_TYKO_VER = 'v0'


def _slugify(text):
    rv = []
    for c in unidecode(text):
        cat = unicodedata.category(c)[0]
        if cat in 'LN' or c in "_-":
            rv.append(c)
        elif cat == 'Z':
            rv.append(' ')
    return re.sub(r"[-\s]+", "-", ''.join(rv).strip()).lower()


class _TykoAPI:
    _session: requests.Session
    _key: str
    _key_shm: SharedMemory = None

    def __init__(
            self,
            key: bytes = None,
            key_shm: SharedMemory = None,
            server: str = None,
    ):

        if server is None:
            server = "https://api.tyko.ai/"

        # Split the server into scheme and host
        server_parts = urlparse(server)
        scheme = server_parts.scheme
        host = server_parts.netloc

        # Rebuilt the base url.
        self._base_url = f'{scheme}://{host}'
        self._session = requests.Session()

        # Save a local copy of the shared memory pointing to the API key.
        self._key_shm = key_shm

        # Try to get one from environ if not passed.
        if key is None and _TYKO_KEY in os.environ:
            key = bytes.fromhex(os.environ[_TYKO_KEY])

        # Try to get one from the netrc.
        if key is None:
            try:
                netrc_ = netrc.netrc()
                if host in netrc_.hosts:
                    key = bytes.fromhex(netrc_.hosts[self._hostname][2])
            except FileNotFoundError:
                pass

        # Finally, just try to create a new one.
        if key is None:
            key = self._get_new_key()
            print(f'A new key was created: {key.hex()}') # noqa

        self._set_key(key)

    def _set_key(self, key: bytes):
        self._key = key[:32]
        if self._key_shm is not None:
            self._key_shm.buf[:len(self._key)] = self._key
        self._session.headers['X-API-KEY'] = self._key.hex()

    def _fix_url(self, url: str) -> str:
        return urljoin(self._base_url, url)

    def _get_new_key(self) -> bytes:
        res = self._session.post(self._fix_url('/v0/api_keys/'))
        return bytes.fromhex(res.json()['key'])

    def post(self, url: str, data: dict = None):
        return self._session.post(self._fix_url(url), json=data)

    def get(self, url: str, params: dict = None) -> requests.Response:
        return self._session.get(
            self._fix_url(url), params=params if params else {}
        )


def _sanitize(data: Dict[str, any]):
    _data = {}
    if isinstance(data, dict):
        for k, v in data.items():
            if isinstance(v, (int, float, str)):
                _data[k] = v
    return _data


_readable = '0123456789abcdefghijklmnopqrstuv'


def _bytes_to_readable(data: bytes) -> str:
    res = ""
    for char in data:
        res += _readable[char // 32]
        res += _readable[char % 32]
    return res


def _append_json_line(fd, data):
    fd.write(json.dumps(data).encode('utf-8') + b"\n")


class _Reporter:

    _closed = False

    # Project info.
    _project_name: str = None
    _project_slug: str = None

    def set_project_name(self, name: str):
        self._project_name = name
        self._project_slug = _slugify(name)

    def close(self):
        raise NotImplementedError

    def __del__(self):
        if not self._closed:
            self.close()


class _LocalReporter(_Reporter):
    _filename: str
    _fd = None

    def __init__(self, filename: str, key_shm: SharedMemory = None):
        self._filename = filename
        self._fd = open(filename, "ab", buffering=0)

    def close(self):
        if self._fd and not self._fd.closed:
            self._fd.close()
        self._closed = True

    def _push(self, data):
        if not self._closed:
            self._fd.write(json.dumps(data).encode("utf-8") + b"\n")


class _TryAgainLaterException(Exception):
    pass


class _LiveReporterThread(threading.Thread):

    # Api Client
    _api: _TykoAPI = None

    # Project info.
    _project_name: str = None
    _project_slug: str = None

    # General data.
    _started_at = None

    def __init__(self, q, server: str, key_shm: SharedMemory = None):
        super().__init__()
        self._q = q
        self._keep_running = True
        self._api = _TykoAPI(key_shm=key_shm, server=server)

    def _set_project(self, data: dict):
        self._project_url = data['url']
        self._project_id = data['id']
        self._project_slug = data['slugified_name']
        self._project_name = data['name']

    def _set_run_info(self, data):
        self._run_id = data['id']
        self._run_url = data['url']

    def _create_run(self):
        res = self._api.post("/v0/runs/", {'config': {}, 'project': self._project_url})
        if res.status_code == 201:
            self._set_run_info(res.json())

    def _create_new_project(self, name: str):
        res = self._api.post('/v0/projects/', {'name': name})
        if res.status_code != 201:
            raise _TryAgainLaterException
        self._set_project(res.json())

    def _resolve_project(self, name: str):
        res = self._api.get('/v0/projects/', {'name': name})
        if res.status_code != 200:
            raise _TryAgainLaterException
        res = res.json()
        if res['count'] > 0:
            self._set_project(res['results'][0])
        else:
            return self._create_new_project(name)

    def _process(self, data):

        if 'version' in data:
            self._version = data['version']

        if 'project_name' in data:
            self._resolve_project(data['project_name'])
            self._create_run()

        if 'started_at' in data:
            self._started_at = data['started_at']

        if 'log' in data:
            self._post_log(data['log'])

        if "close" in data:
            self._keep_running = False

    def _post_log(self, entry: dict):
        res = self._api.post(f"/v0/runs/{self._run_id}/logs/", {'data': entry})
        if res.status_code != 201:
            raise Exception

    def run(self):

        count = 0

        while True:

            try:
                item = self._q.get(timeout=0.1)

                if isinstance(item, int) and item < 0:
                    break

                self._process(item)
                count = 0

            except queue.Empty:
                count += 1

            except (EOFError, OSError, ValueError):
                break
            if count > 100:
                break


class _LiveReporter(_Reporter):
    _thread: threading.Thread = None
    _queue: multiprocessing.Queue = None
    _key_shm: SharedMemory = None

    def __init__(self, server: str, key_shm: SharedMemory = None):

        # Keep a copy of the apikey.
        self._key_shm = key_shm

        # Get a multiproces-safe queue in case the main thread decides to fork.
        self._queue = multiprocessing.Queue()

        # Start a thread.
        self._thread = _LiveReporterThread(
            self._queue, server=server, key_shm=self._key_shm
        )
        self._thread.start()

    def close(self):
        if not self._closed:
            self._closed = True

            if self._queue is not None:
                self._queue.put(-1)
                self._queue.close()

            if self._thread is not None:
                self._thread.join()

            if self._key_shm is not None:
                self._key_shm.close()

    def _push(self, data):
        if isinstance(data, dict):
            self._queue.put(data)


class Tyko:
    """
    Tyko
    ====

    Main class for reporting to Tyko.

    Reporting to the API happens in two steps.
    First, a buffer is filled that ends in a local file.

    TODO: Add throttle.
    TODO: Add configurations.
    TODO: Add sensing memory and cpu/gpu usage.
    """

    _closed = False

    _reporters : List = None

    # Set the api_key as shared memory.
    _apikey: SharedMemory

    # Save the filename of the local report.
    local_report_filename: str

    def __init__(self, project_name: str, offline=False, **kwargs):
        """Nothing here."""

        # Keep track of a single api_key shared by all reporters.
        self._key_shm = SharedMemory(create=True, size=32)

        # Generate a local id.
        local_id = _bytes_to_readable(os.urandom(6))
        project_slug = _slugify(project_name)

        # Save file name
        self.local_report_filename = f".tyko-{project_slug}-{local_id}"

        # Add the reporters.
        self._reporters = [
            _LocalReporter(self.local_report_filename, key_shm=self._key_shm)
        ]

        if not offline:
            server = 'https://api.tyko.ai/'
            if 'server' in kwargs:
                server = kwargs['server']
            self._reporters.append(_LiveReporter(key_shm=self._key_shm, server=server))

        # Describe the version of the file.
        self._push({'version': '0.1'})
        self._push({'started_at': time.monotonic_ns()})

        # Save the project_name intended for this.
        self._push({'project_name': project_name})

    def __del__(self):
        self.close()

    def close(self):
        if not self._closed:
            self._key_shm.close()
            if self._reporters is not None:
                for reporter in self._reporters:
                    reporter.close()
            self._closed = True

    def _push(self, data):
        if self._reporters is not None:
            for r in self._reporters:
                r._push(data)

    def log(self, data: Dict[str, any]):
        """Create a log entry in the current run."""
        self._push({'log': _sanitize(data), 'at': time.monotonic_ns()})
