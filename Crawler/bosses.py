import requests
from bs4 import BeautifulSoup
import pandas as pd

BASE_URL = 'https://www.zeldadungeon.net'
BOSSES_LIST_URL = 'https://www.zeldadungeon.net/wiki/A_Link_to_the_Past_Bosses'
bosses_list_page = requests.get(BOSSES_LIST_URL)
soup_list = BeautifulSoup(bosses_list_page.content, 'html.parser')
bosses_list = soup_list.find_all('i')

all_bosses = []

for boss in bosses_list:
    if 'Main article' in boss.text:
        boss_dict = {'name': boss.find('a')['title']}
        href = boss.find('a').get('href')
        boss_url = BASE_URL + href
        boss_page = requests.get(boss_url)
        soup_boss = BeautifulSoup(boss_page.content, 'html.parser')
        info = soup_boss.find_all(class_='poem')

        for i in range(len(info)):
            try:
                if info[i].find('p').get_text(strip=True) == 'Dungeons':
                    boss_dict['location'] = info[i + 1].find('p').find('a')['title']
                elif info[i].find('p').get_text(strip=True) == 'Rewards':
                    boss_dict['rewards'] = [x['title'] for x in info[i + 1].find_all('a')]
                elif 'Effective' in info[i].find('p').get_text(strip=True):
                    boss_dict['effective weapons'] = [x['title'] for x in info[i + 1].find_all('a')]
            except:
                continue

        all_bosses.append(boss_dict)

print(all_bosses)

bosses_df = pd.DataFrame.from_records(all_bosses)
bosses_df.to_csv('bosses.csv', index=False)
