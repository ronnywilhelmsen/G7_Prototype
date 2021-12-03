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
    duration = database.Column(database.Integer)
    type = database.Column(database.String(9))
    picture_url = database.Column(database.String(9999))
    category_id = database.Column(database.Integer, database.ForeignKey('category.id'))

    def __init__(self, producer, model, description, price, duration, type, picture_url, category_id):
        self.producer = producer
        self.model = model
        self.description = description
        self.price = price
        self.duration = duration
        self.type = type
        self.picture_url = picture_url
        self.category_id = category_id

class Category(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(99))
    description = database.Column(database.String(9999))
    items = database.relationship('Item')
    store_id = database.Column(database.Integer, database.ForeignKey('store.id'))

    def __init__(self, name, description, store_id):
        self.name = name
        self.description = description
        self.store_id = store_id

class Store(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(99), unique=True)
    description = database.Column(database.String(9999))
    picture_url = database.Column(database.String(9999))
    categories = database.relationship('Category')

    def __init__(self, name, description, picture_url):
        self.name = name
        self.description = description
        self.picture_url = picture_url

class User(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(99), unique=True)
    # cart = database.relationship('Item')

    def __init__(self, name):
        self.name = name


class Bid(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    userId = database.Column(database.Integer, database.ForeignKey('user.id'))
    itemId = database.Column(database.Integer, database.ForeignKey('item.id'))
    price = database.Column(database.Integer)


    def __init__(self, price):
        self.price = price

class Sale(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    userId = database.Column(database.Integer, database.ForeignKey('user.id'))
    itemId = database.Column(database.Integer, database.ForeignKey('item.id'))
    price = database.Column(database.Integer)


    def __init__(self, price):
        self.price = price


# Kan legge til en klasse "BID" som har en id, ForeignKey til User og Item, samt en pris.
# Gjør det mulig å holde styr på hvem som la inn bud
# Må først ha login på plass