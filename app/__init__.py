from app.config import config
from app.extensions import db, migrate, ma
from app.bundles.router import bundle_router
from app.items.router import item_router
from app.ships.router import ship_router
from app.oilrigs.router import oilrig_router
from app.users.router import user_router
from flask import Flask

from dd import create_dd

def create_app():

    ### Create APP
    app = Flask(__name__)
    app.config.from_object(config)


    ### Create ORM
    db.init_app(app)

    ### Create Migrations
    migrate.init_app(app)

    ### Create Validator
    ma.init_app(app)

    ### Blueprints
    app.register_blueprint(user_router)
    app.register_blueprint(bundle_router)
    app.register_blueprint(item_router)
    app.register_blueprint(ship_router)
    app.register_blueprint(oilrig_router)

    create_dd(app)


    return app