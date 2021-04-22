import os
import pandas as pd
from . import db, project_path


class Bosses(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    effective_weapons = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(40), nullable=False)
    rewards = db.Column(db.String(50), nullable=True)

    dungeons = db.relationship('Dungeons', lazy=True)

    def __repr__(self):
        return f"id: {self.id}, name: {self.name}, effective weapons: {self.effective_weapons}, location: {self.location}, rewards: {self.rewards}\n"


class Characters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    race = db.Column(db.String(10))
    gender = db.Column(db.String(10))
    location = db.Column(db.String(100))

    def __repr__(self):
        return f"id: {self.id}, name: {self.name}, race: {self.race}, gender: {self.gender}, location: {self.location}\n"


class Dungeons(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)
    boss = db.Column(db.String(20))
    enemies = db.Column(db.String(500))
    items = db.Column(db.String(60))
    rewards = db.Column(db.String(50))
    boss_id = db.Column(db.Integer, db.ForeignKey('bosses.id'), nullable=True)

    def __repr__(self):
        return f"id: {self.id}, name: {self.name}, boss: {self.boss}, enemies: {self.enemies}, items: {self.items}, rewards: {self.rewards}, boss id: {self.boss_id}\n"


class Enemies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)
    location = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"id: {self.id}, name: {self.name}, location: {self.location}\n"


class Items(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    location = db.Column(db.String(100), nullable=False)
    uses = db.Column(db.String(100))

    def __repr__(self):
        return f"id: {self.id}, name: {self.name}, location: {self.location}, uses: {self.uses}\n"


def populate_everything():
    db.create_all()
    data_path = os.path.join(project_path, 'data')
    files = os.listdir(os.path.join(project_path, 'data'))
    for file in files:
        full_file_path = data_path + '/' + file
        model = file.split('.')[0]
        data = pd.read_csv(full_file_path).values.tolist()
        if model == 'bosses':
            for row in data:
                boss = Bosses(name=row[0], effective_weapons=row[1], location=row[2], rewards=row[3])
                db.session.add(boss)
        elif model == 'characters':
            for row in data:
                character = Characters(name=row[0], race=row[1], gender=row[2], location=row[3])
                db.session.add(character)
        elif model == 'dungeons':
            for row in data:
                dungeon = Dungeons(name=row[0], boss=row[1], enemies=row[2], items=row[3], rewards=row[4], boss_id=row[5])
                db.session.add(dungeon)
        elif model == 'enemies':
            for row in data:
                enemy = Enemies(name=row[0], location=row[1])
                db.session.add(enemy)
        elif model == 'items':
            for row in data:
                item = Items(name=row[0], location=row[1], uses=row[2])
                db.session.add(item)
        db.session.commit()
    db.session.close()
