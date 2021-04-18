import requests


MAIN_SITE = 'https://www.zeldadungeon.net'


def test_main_page():
    assert requests.get(MAIN_SITE) is not None


def test_character_page():
    assert requests.get(MAIN_SITE + '/wiki/Link') is not None


def test_bosses_page():
    assert requests.get(MAIN_SITE + '/wiki/A_Link_to_the_Past_Bosses') is not None


def test_dungeons_page():
    assert requests.get(MAIN_SITE + '/wiki/A_Link_to_the_Past_Dungeons') is not None
