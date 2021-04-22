import requests
from bs4 import BeautifulSoup
import pandas as pd


BASE_URL = 'https://www.zeldadungeon.net'
CHARACTER_LIST_URL = 'https://www.zeldadungeon.net/wiki/Gallery:A_Link_to_the_Past_Characters'
character_list_page = requests.get(CHARACTER_LIST_URL)
soup_list = BeautifulSoup(character_list_page.content, 'html.parser')
character_list = soup_list.find_all('li', class_="gallerybox")

all_characters = []

for character in character_list:
    try:
        print(character.find('a')['title'])
        character_dict = {'Name': character.find('a')['title']}
        href = character.find('a').get('href')
        character_url = BASE_URL + href
        character_page = requests.get(character_url)
        soup_character = BeautifulSoup(character_page.content, 'html.parser')
        info = soup_character.find_all(class_="poem")
        for i in range(len(info)):
            if info[i].find('p').get_text(strip=True) == 'Race':
                character_dict['Race'] = info[i+1].find('p').find('a')['title']
            elif info[i].find('p').get_text(strip=True) == 'Gender':
                character_dict['Gender'] = info[i+1].find('p').get_text(strip=True)
            elif info[i].find('p').get_text(strip=True) == 'Location':
                character_dict['Locations'] = [x['title'] for x in info[i+1].find_all('a')]
    except:
        continue
    all_characters.append(character_dict)

character_df = pd.DataFrame.from_records(all_characters)
character_df.to_csv('characters.csv', index=False)
