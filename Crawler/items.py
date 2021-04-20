import requests
from bs4 import BeautifulSoup
import pandas as pd

all_items = []

BASE_URL = 'https://www.zeldadungeon.net'
ITEMS_LIST_URL = 'https://www.zeldadungeon.net/wiki/A_Link_to_the_Past_Items'

items_list_page = requests.get(ITEMS_LIST_URL)
soup_list = BeautifulSoup(items_list_page.content, 'html.parser')
items_list = soup_list.find_all("dd")
for item in items_list:
    item_dict = {'name': item.find('i').find('a')['title']}
    href = item.find('i').find('a')['href']
    item_url = BASE_URL + item.find('i').find('a')['href']
    item_page = requests.get(item_url)
    soup_item = BeautifulSoup(item_page.content, 'html.parser')
    info = soup_item.find_all(class_="poem")
    for i in range(len(info)):
        if info[i].find('p').get_text(strip=True) == "Location":
            item_dict['location'] = info[i+1].find('p').get_text(strip=True)
        if info[i].find('p').get_text(strip=True) == "Uses":
            item_dict['uses'] = info[i+1].find('p').get_text(strip=True)
    all_items.append(item_dict)

items_df = pd.DataFrame.from_records(all_items)
items_df.to_csv('items.csv', index=False)
