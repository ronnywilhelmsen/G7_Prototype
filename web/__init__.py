from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from os import path

database = SQLAlchemy()

Database_Name = "database.db"

def start():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "VerySecret"
    app.config["SQLALCHEMY_DATABASE_URI"] = f'sqlite:///{Database_Name}'

    database.init_app(app)

    from .views import views

    app.register_blueprint(views, url_prefix='/')

    start_database(app)

    from .models import Category, Item

    return app

def start_database(app):
    if not path.exists("web/" + Database_Name):
        database.create_all(app=app)