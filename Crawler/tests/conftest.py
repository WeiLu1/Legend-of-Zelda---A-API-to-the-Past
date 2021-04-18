import pytest
import requests


@pytest.fixture(scope="session")
def main_site():
    return 'https://www.zeldadungeon.net'
