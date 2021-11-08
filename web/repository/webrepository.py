from flask import request, flash, redirect, render_template
from flask_login import login_user

from web.models import Category, Item, Store, User

from web import database

def store():
    name = request.form.get('name')
    description = request.form.get('description')
    picture_url = request.form.get('picture_url')
    if len(name) < 3:
        flash("Name to short", category="error")
    elif len(description) < 3:
        flash("Description to short", category="error")
    elif len(picture_url) < 0:
        flash("URL to short", category="error")
    else:
        flash(name + " has been added...", category="success")
        new_Store = Store(name=name, description=description, picture_url=picture_url)
        database.session.add(new_Store)
        database.session.commit()

def category(storeId):
    name = request.form.get('name')
    description = request.form.get('description')
    if len(name) < 3:
        flash("Name to short", category="error")
    elif len(description) < 3:
        flash("Description to short", category="error")
    else:
        flash(name + " has been added...", category="success")
        new_Category = Category(name=name, description=description, store_id=storeId)
        database.session.add(new_Category)
        database.session.commit()

def item(catId):
    producer = request.form.get('producer')
    model = request.form.get('model')
    description = request.form.get('description')
    price = request.form.get('price')
    end_time = request.form.get('end_time')
    picture_url = request.form.get('picture_url')
    if len(producer) < 3:
        flash("Producer to short", category="error")
    elif len(model) < 3:
        flash("Model to short", category="error")
    elif len(description) < 3:
        flash("Description to short", category="error")
    elif len(price) < 0:
        flash("Price to low", category="error")
    elif len(end_time) < 0:
        flash("End time to short", category="error")
    elif len(picture_url) < 0:
        flash("URL to short", category="error")
    else:
        flash(model + " has been added to auction...", category="success")
        new_item = Item(producer=producer, model=model, description=description, price=price, end_time=end_time,
                        picture_url=picture_url, category_id=catId)
        database.session.add(new_item)
        database.session.commit()

def logick(itemId):
    item = Item.query.get(itemId)

    new_price = int(request.form.get('price'))
    if new_price > item.price:
        item.price = new_price
        database.session.commit()
        flash("Bid accepted...", category="success")
        return redirect(request.referrer)
    else:
        flash("New Bid is lower than current bid...", category="error")

def sign_up():
    name = request.form.get('name')

    flash(name + " added...", category="success")
    new_User = User(name=name)
    database.session.add(new_User)
    database.session.commit()

    login_user(new_User)

