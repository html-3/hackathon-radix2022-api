

from os import environ


class Config:
    ### Flask Config
    SECRET_KEY = environ.get("SECRET_KEY")
    ENV = environ.get("ENV")

    ### SQLAlchemy Config
    SQLALCHEMY_DATABASE_URI = "sqlite:///local.db" or str(environ.get("HEROKU_POSTGRESQL_PURPLE_URL")).replace("postgres://", "postgresql://", 1)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSON_SORT_KEYS = False

    ### JWT Config
    JWT_SECRET_KEY = environ.get("JWT_SECRET_KEY")


config = Config()