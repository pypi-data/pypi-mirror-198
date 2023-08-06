# noqa
import pytest
from time import sleep
import os
import time
from unittest.mock import patch, mock_open, call

import requests_mock

from tyko import Tyko


@pytest.fixture
def monotonic():

    class Monotonic:
        def __init__(self, value=0):
            self.reset(value)
        def reset(self, value=0):
            self.value = value
        def __call__(self):
            self.value += 1
            return self.value - 1

    monotonic_ns = patch('time.monotonic_ns', side_effect=Monotonic())
    mock = monotonic_ns.start()
    yield mock
    mock.stop()


@pytest.fixture
def netrc_not_found():
    with patch('tyko.netrc.netrc', side_effect=FileNotFoundError) as m:
        yield m


@pytest.fixture
def fs():
    m = mock_open()
    with patch('tyko.open', m):
        yield m

@pytest.fixture
def api():
    with requests_mock.Mocker() as m:
        m.get(
            "https://api.tyko.ai/v0/projects/?name=my-project",
            status_code=200,
            json={"count": 0}
        )

        m.post(
            "https://api.tyko.ai/v0/api_keys/",
            status_code=201,
            json={"key": "key"}
        )

        m.post(
            "https://api.tyko.ai/v0/runs/", status_code=201, json={
                "id": 'r123',
                "url": "https://api.tyko.ai/v0/runs/123/"
            }
        )

        m.post(
            "https://api.tyko.ai/v0/runs/r123/logs/", status_code=201, json={
                "data": {"i": 0}
            }
        )

        m.post(
            "https://api.tyko.ai/v0/projects/",
            status_code=201,
            json={
                'name': 'My Project',
                'slugified_name': 'my-project',
                'id': '123',
                'url': 'https://api.tyko.ai/v0/projects/123/'
            }
        )
        yield m

def test_dummy():
    assert True


def test_tyko_object(fs, monotonic):
    Tyko('my-project', offline=True)
    fs().write.assert_has_calls([
        call(b'{"version": "0.1"}\n'),
        call(b'{"started_at": 0}\n'),
        call(b'{"project_name": "my-project"}\n')
    ])

def test_simple_log(fs, monotonic):
    t = Tyko('my-project', offline=True)
    t.log({'i': 0})
    fs().write.assert_has_calls([
        call(b'{"version": "0.1"}\n'),
        call(b'{"started_at": 0}\n'),
        call(b'{"project_name": "my-project"}\n'),
        call(b'{"log": {"i": 0}, "at": 1}\n')
    ])


def test_tyko_object_api(fs, monotonic, api):
    t = Tyko('my-project')
    for i in range(3):
        t.log({'i': i})
    sleep(0.5)
    for h in api.request_history:
        print(time.time(), h)
    assert api.call_count == 7


def test_netrc_not_found(fs, netrc_not_found, api):
    t = Tyko(project_name="my-project")
    assert api.call_count == 1
    assert t._key_shm.buf.tobytes()[:3] == b"key"


def test_key_from_env(fs, netrc_not_found, api):
    with patch.dict(os.environ, {"TYKO_KEY": "yyy"}, clear=True) as m:
        tyko = Tyko(project_name="my-project")
        assert tyko._key_shm.buf.tobytes()[:3] == b"yyy"

def test_change_host(fs, netrc_not_found):
    with requests_mock.Mocker() as m:
        m.post(
            "http://localhost:8030/v0/api_keys/",
            status_code=201,
            json={"key": "key"}
        )
        tyko = Tyko(project_name="my-project", server="http://localhost:8030")
        assert tyko._key_shm.buf.tobytes()[:3] == b"key"
