from sqlalchemy_utils import database_exists
from flask_restful import Resource
from api import db_uri, app, api
from api.models import populate_everything


@app.before_first_request
def populate_database():
    if not database_exists(db_uri):
        populate_everything()


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


class HelloSecondPage(Resource):
    def get(self):
        return {'hello': 'second'}


api.add_resource(HelloWorld, '/')
api.add_resource(HelloSecondPage, '/secondpage')


if __name__ == "__main__":
    app.run(port=8000, debug=True, host='0.0.0.0')
