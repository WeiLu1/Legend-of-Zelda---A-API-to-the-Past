##Legend of Zelda - A API to the Past

A Legend of Zelda - A Link to the Past API. 

Technologies to use to create this:
- BeautifulSoup
- SQLite
- SQLAlchemy
- Flask
- Pytest


Get all characters API example response:

```
{
	"data": [{
			"id": 1,
			"name": "Link",
			"race": "Hylian",
			"gender": "Male",
			"Location": ["Hyrule"]
		},
		{
			"id": 2,
			"name": "Zelda",
			"race": "Hylian",
			"gender": "female",
			"Location": ["Hyrule"]
		}
	]
}
```
\
Get all bosses API example response: 
```
{
	"data": [{
			"id": 20,
			"name": "Trinexx",
			"location": "Turtle Rock",
            "effective weapons": ["Fire rod", "Ice rod", "Sword"],
            "rewards": ["Heart Container", "Seventh Crystal"]
        }
	]
}
```
\
Get all items API example response:

```
{
	"data": [{
			"id": 10,
			"name": "Tempered Sword",
			"location": "Swordsmith's Shop"
		},
		{
			"id": 11,
			"name": "Golden Sword",
			"location": "Pyramid of Power"
		}
	]
}
```
\
