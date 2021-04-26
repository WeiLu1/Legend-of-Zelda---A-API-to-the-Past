import pytest


@pytest.fixture(scope='session')
def url():
    return "http://localhost:8000/"
