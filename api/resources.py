from flask_restful import Resource, marshal_with, fields
from api.models import (
    BossesModel,
    CharactersModel,
    DungeonsModel,
    EnemiesModel,
    ItemsModel
)

boss_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'effective_weapons': fields.String,
    'location': fields.String,
    'rewards': fields.String
}


character_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'race': fields.String,
    'gender': fields.String,
    'location': fields.String
}

dungeons_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'boss': fields.String,
    'enemies': fields.String,
    'items': fields.String,
    'rewards': fields.String,
    'boss_id': fields.Integer
}

enemies_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'location': fields.String
}

items_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'location': fields.String,
    'uses': fields.String
}


class HelloWorld(Resource):
    def get(self):
        return "endpoints: /bosses, /characters, /dungeons, /enemies, /items"


class Bosses(Resource):
    @marshal_with(boss_fields)
    def get(self):
        return BossesModel.get_all_bosses()


class Boss(Resource):
    @marshal_with(boss_fields)
    def get(self, boss_id):
        boss = BossesModel.get_boss_by_id(boss_id)
        return boss


class Characters(Resource):
    @marshal_with(character_fields)
    def get(self):
        characters = CharactersModel.get_all_characters()
        return characters


class Character(Resource):
    @marshal_with(character_fields)
    def get(self, character_id):
        character = CharactersModel.get_character_by_id(character_id)
        return character


class Dungeons(Resource):
    @marshal_with(dungeons_fields)
    def get(self):
        dungeons = DungeonsModel.get_all_dungeons()
        return dungeons


class Dungeon(Resource):
    @marshal_with(dungeons_fields)
    def get(self, dungeon_id):
        dungeon = DungeonsModel.get_dungeon_by_id(dungeon_id)
        return dungeon


class Enemies(Resource):
    @marshal_with(enemies_fields)
    def get(self):
        enemies = EnemiesModel.get_all_enemies()
        return enemies


class Enemy(Resource):
    @marshal_with(enemies_fields)
    def get(self, enemy_id):
        enemy = EnemiesModel.get_enemy_by_id(enemy_id)
        return enemy


class Items(Resource):
    @marshal_with(items_fields)
    def get(self):
        items = ItemsModel.get_all_items()
        return items


class Item(Resource):
    @marshal_with(items_fields)
    def get(self, item_id):
        items = ItemsModel.get_item_by_id(item_id)
        return items
