from sqlalchemy_utils import database_exists
from api import db_uri, app, api
from api.models import populate_everything
from api.resources import (
    HelloWorld,
    Bosses,
    Characters,
    Dungeons,
    Enemies,
    Items
)


@app.before_first_request
def populate_database():
    if not database_exists(db_uri):
        populate_everything()


api.add_resource(HelloWorld, '/')
api.add_resource(Bosses, '/bosses')
api.add_resource(Characters, '/characters')
api.add_resource(Dungeons, '/dungeons')
api.add_resource(Enemies, '/enemies')
api.add_resource(Items, '/items')


if __name__ == "__main__":
    app.run(port=8000, debug=True, host='0.0.0.0')
