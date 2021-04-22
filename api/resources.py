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
        bosses = BossesModel.query.all()
        return bosses


class Characters(Resource):
    @marshal_with(character_fields)
    def get(self):
        characters = CharactersModel.query.all()
        return characters


class Dungeons(Resource):
    @marshal_with(dungeons_fields)
    def get(self):
        dungeons = DungeonsModel.query.all()
        return dungeons


class Enemies(Resource):
    @marshal_with(enemies_fields)
    def get(self):
        enemies = EnemiesModel.query.all()
        return enemies


class Items(Resource):
    @marshal_with(items_fields)
    def get(self):
        items = ItemsModel.query.all()
        return items
