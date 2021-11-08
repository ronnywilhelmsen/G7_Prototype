from flask_login import UserMixin
from sqlalchemy import func

from . import database

class Item(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    producer = database.Column(database.String(99))
    model = database.Column(database.String(99))
    description = database.Column(database.String(9999))
    price = database.Column(database.Integer)
    start_time = database.Column(database.DateTime(timezone=True), server_default=func.now())
    end_time = database.Column(database.String(20))
    duration = database.Column(database.Integer)
    picture_url = database.Column(database.String(9999))
    category_id = database.Column(database.Integer, database.ForeignKey('category.id'))

    def __init__(self, producer, model, description, price):
        self.producer = producer
        self.model = model
        self.description = description
        self.price = price

class Category(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(99))
    description = database.Column(database.String(9999))
    items = database.relationship('Item')
    store_id = database.Column(database.Integer, database.ForeignKey('store.id'))

    def __init__(self, name, description):
        self.name = name
        self.description = description

class Store(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(99), unique=True)
    description = database.Column(database.String(9999))
    picture_url = database.Column(database.String(9999))
    categories = database.relationship('Category')

    def __init__(self, name, description):
        self.name = name
        self.description = description

class User(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(99), unique=True)

    def __init__(self, name):
        self.name = name

# Could add user class to make a log in system