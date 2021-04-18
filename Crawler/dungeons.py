import requests
from bs4 import BeautifulSoup
import pandas as pd

BASE_URL = 'https://www.zeldadungeon.net'
DUNGEONS_LIST_URL = 'https://www.zeldadungeon.net/wiki/A_Link_to_the_Past_Dungeons'
dungeons_list_page = requests.get(DUNGEONS_LIST_URL)
soup_list = BeautifulSoup(dungeons_list_page.content, 'html.parser')
dungeons_list = soup_list.find_all('i')

all_dungeons = []

for dungeon in dungeons_list:
    if 'Main article' in dungeon.text:
        dungeons_dict = {'name': dungeon.find('a')['title']}
        href = dungeon.find('a').get('href')
        dungeon_url = BASE_URL + href
        dungeon_page = requests.get(dungeon_url)
        soup_dungeon = BeautifulSoup(dungeon_page.content, 'html.parser')
        info = soup_dungeon.find_all(class_='poem')

        for i in range(len(info)):
            try:
                if info[i].find('p').get_text(strip=True) == 'Boss':
                    dungeons_dict['boss'] = info[i + 1].find('p').find('a')['title']
                elif info[i].find('p').get_text(strip=True) == 'Items':
                    dungeons_dict['items'] = [x['title'] for x in info[i + 1].find_all('a')]
                elif info[i].find('p').get_text(strip=True) == 'Rewards':
                    dungeons_dict['rewards'] = [x['title'] for x in info[i + 1].find_all('a')]
                elif info[i].find('p').get_text(strip=True) == 'Enemies':
                    dungeons_dict['enemies'] = [x['title'] for x in info[i + 1].find_all('a')]
            except:
                continue

        if 'enemies' not in dungeons_dict:
            enemies = []
            enemy_info = soup_dungeon.find_all(class_='gallerytext')
            for enemy in enemy_info:
                try:
                    enemies.append(enemy.find('p').find('a')['title'])
                except:
                    continue
            dungeons_dict['enemies'] = enemies

        print(dungeons_dict)
        all_dungeons.append(dungeons_dict)

print(all_dungeons)

dungeons_df = pd.DataFrame.from_records(all_dungeons)
dungeons_df.to_csv('dungeons.csv', index=False)
