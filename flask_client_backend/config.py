import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    """
    https://flask-sqlalchemy.palletsprojects.com/en/2.x/config/
    """
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite://")
    SQLALCHEMY_TRACK_MODIFICATIONS = False