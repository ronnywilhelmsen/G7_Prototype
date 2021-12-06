from flask import request, flash

from web.models import Category, Item, Store
from web import database
from web.repository import businessRepo

def sale_type(itemId):
    item = Item.query.get(itemId)
    if item.type == "A":
        businessRepo.bid(itemId)
    else:
        businessRepo.sale(itemId)

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
    duration = request.form.get('duration')
    type = request.form.get('type')
    picture_url = request.form.get('picture_url')
    if len(producer) < 1:
        flash("Producer to short", category="error")
    elif len(model) < 1:
        flash("Model to short", category="error")
    elif len(description) < 1:
        flash("Description to short", category="error")
    elif len(price) < 0:
        flash("Price to low", category="error")
    elif len(duration) < 0:
        flash("Duration to low", category="error")
    elif len(type) < 0:
        flash("Not a sale type, must either be A-auction, S-sale or D-display", category="error")
    elif len(picture_url) < 0:
        flash("URL to short", category="error")
    else:
        new_item = Item(producer=producer, model=model, description=description, price=price,
                        duration=duration, type=type, picture_url=picture_url, category_id=catId)
        if type == "A":
            flash(model + " has been added to auction...", category="success")
            database.session.add(new_item)
            database.session.commit()
        elif type == "S":
            flash(model + " has been added to sale...", category="success")
            database.session.add(new_item)
            database.session.commit()
        elif type == "D":
            flash(model + " has been added to display...", category="success")
            database.session.add(new_item)
            database.session.commit()