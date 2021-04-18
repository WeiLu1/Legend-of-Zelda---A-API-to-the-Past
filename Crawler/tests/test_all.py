import requests


def test_main_page(main_site):
    assert requests.get(main_site) is not None


def test_character_page(main_site):
    assert requests.get(main_site + '/wiki/Link') is not None


def test_bosses_page(main_site):
    assert requests.get(main_site + '/wiki/A_Link_to_the_Past_Bosses') is not None
