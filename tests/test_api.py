import requests


def test_main(url):
    data = requests.get(url)
    assert data.status_code == 200
    assert data.json() == 'endpoints: /bosses, /characters, /dungeons, /enemies, /items'


def test_bosses(url):
    endpoint = url + '/bosses'
    data = requests.get(endpoint)

    assert data.status_code == 200
    assert len(data.json()) == 13
    assert len(data.json()[10]) == 5
    assert data.json()[10]['name'] == "Trinexx"
    assert list(data.json()[0].keys()) == ['id', 'name', 'effective_weapons', 'location', 'rewards']


def test_boss(url):
    good_endpoint = url + '/bosses/Ganon'
    good_data = requests.get(good_endpoint)
    bad_endpoint = url + '/bosses/ganon'
    bad_data = requests.get(bad_endpoint)

    assert good_data.status_code == 200
    assert good_data.json()['location'] == "Pyramid of Power"
    assert bad_data.status_code == 404
    assert bad_data.json()['message'] == "boss not found"


def test_characters(url):
    endpoint = url + '/characters'
    data = requests.get(endpoint)

    assert data.status_code == 200
    assert len(data.json()) == 67
    assert data.json()[0]['name'] == 'Link'
    assert len(data.json()[0]) == 5
    assert list(data.json()[0].keys()) == ['id', 'name', 'race', 'gender', 'location']


def test_character(url):
    good_endpoint = url + 'characters/3'
    bad_endpoint = url + 'characters/100'
    good_data = requests.get(good_endpoint)
    bad_data = requests.get(bad_endpoint)

    assert good_data.status_code == 200
    assert good_data.json()['name'] == "Agahnim"
    assert bad_data.status_code == 404
    assert bad_data.json()['message'] == "character not found"


def test_dungeons(url):
    endpoint = url + '/dungeons'
    data = requests.get(endpoint)

    assert data.status_code == 200
    assert len(data.json()) == 16
    assert data.json()[0]['name'] == 'Hyrule Castle'
    assert len(data.json()[0]) == 7
    assert list(data.json()[0].keys()) == ['id', 'name', 'boss', 'enemies', 'items', 'rewards', 'boss_id']


def test_dungeon(url):
    good_endpoint = url + 'dungeons/5'
    bad_endpoint = url + 'dungeons/100'
    good_data = requests.get(good_endpoint)
    bad_data = requests.get(bad_endpoint)

    assert good_data.status_code == 200
    assert good_data.json()['boss'] == "Moldorm"
    assert bad_data.status_code == 404
    assert bad_data.json()['message'] == "dungeon not found"


def test_enemies(url):
    endpoint = url + '/enemies'
    data = requests.get(endpoint)

    assert data.status_code == 200
    assert len(data.json()) == 107
    assert data.json()[13]['name'] == 'Keese'
    assert len(data.json()[0]) == 3
    assert list(data.json()[0].keys()) == ['id', 'name', 'location']


def test_enemy(url):
    good_endpoint = url + 'enemies/14'
    bad_endpoint = url + 'enemies/1200x'
    good_data = requests.get(good_endpoint)
    bad_data = requests.get(bad_endpoint)

    assert good_data.status_code == 200
    assert good_data.json()['name'] == "Keese"
    assert bad_data.status_code == 404
    assert bad_data.json()['message'] == "enemy not found"


def test_items(url):
    endpoint = url + '/items'
    data = requests.get(endpoint)

    assert data.status_code == 200
    assert len(data.json()) == 56
    assert data.json()[17]['name'] == "Silver Arrow"
    assert len(data.json()[0]) == 4
    assert list(data.json()[0].keys()) == ['id', 'name', 'location', 'uses']


def test_item(url):
    good_endpoint = url + 'items/18'
    bad_endpoint = url + 'items/12fsdfx'
    good_data = requests.get(good_endpoint)
    bad_data = requests.get(bad_endpoint)

    assert good_data.status_code == 200
    assert good_data.json()['name'] == "Silver Arrow"
    assert bad_data.status_code == 404
    assert bad_data.json()['message'] == "item not found"

