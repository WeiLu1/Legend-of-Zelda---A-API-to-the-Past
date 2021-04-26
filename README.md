# Legend of Zelda - A API to the Past

A Legend of Zelda - A Link to the Past API. 

Technologies to use to create this:
- BeautifulSoup
- SQLite
- SQLAlchemy
- Flask and Flask-RESTful
- Pytest

 
## Endpoints
If ID is added in the endpoint then it will get the resource specific to the ID. \
ID can be the number or name. \
If no ID is added, an entire list of will be returned.

- ### Bosses/< id >
Return a list of bosses. 
```
[
    {
        "id": 1,
        "name": "Armos Knight",
        "effective_weapons": "['Sword', 'Bow']",
        "location": "Eastern Palace",
        "rewards": "['Heart Container', 'Pendant of Courage']"
    }
]
```

- ### Characters/< id >
Return a list of characters.
```
{
    "id": 3,
    "name": "Agahnim",
    "race": null,
    "gender": null,
    "location": "['Hyrule Castle Tower', \"Ganon's Tower\"]"
}
```

- ### Dungeons/< id >
Return a list of dungeons.
```
{
    "id": 4,
    "name": "Desert Palace",
    "boss": "Lanmola",
    "enemies": "['Popo', 'Beamos', 'Green Eyegore', 'Red Eyegore', 'Green Leever', 'Purple Leever', 'Blue Devalant', 'Red Devalant']",
    "items": "['Power Glove']",
    "rewards": "['Heart Container', 'Pendant of Power']",
    "boss_id": 2
}
```

- ### Enemies/< id >
Return a list of enemies.
```
{
    "id": 23,
    "name": "Green Soldier",
    "location": "Light World Overworld and Dungeons"
}
```

- ### Items/< id >
Return a list of items.
```
{
    "id": 2,
    "name": "Master Sword",
    "location": "Lost Woods",
    "uses": "The legendary sword that seals the darkness"
}
```
