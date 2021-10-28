from datetime import timedelta

from flask import Blueprint, render_template, request, flash, redirect, url_for

from . import database
from web.models import Category, Item

views = Blueprint("views", __name__)

@views.route("/")
def homepage():
    return render_template("home.html", categories=Category.query.all())

@views.route("/category-overview/<catId>")
def category_overview(catId):
    category = Category.query.get(catId)
    return render_template("category-overview.html", items=category.items, catId=category.id)

@views.route("/addCategory", methods=['GET', 'POST'])
def addCategory():
    if request.method == 'POST':
        name = request.form.get('name')
        description = request.form.get('description')

        flash("Category has been added...", category="success")
        new_Category = Category(name=name, description=description)
        database.session.add(new_Category)
        database.session.commit()
        return redirect(url_for('views.homepage'))

    return render_template("addCategory.html")

@views.route("/category-overview/<catId>/addItem", methods=['GET', 'POST'])
def addItem(catId):
    category = Category.query.get(catId)

    if request.method == 'POST':
        producer = request.form.get('producer')
        model = request.form.get('model')
        description = request.form.get('description')
        price = request.form.get('price')
        end_time = request.form.get('end_time')
        picture_url = request.form.get('picture_url')

        flash("Item has been added to auction...", category="success")
        new_item = Item(producer=producer, model=model, description=description, price=price, end_time=end_time, picture_url=picture_url, category_id = catId)
        database.session.add(new_item)
        database.session.commit()
        return redirect(request.referrer)

    return render_template("addItem.html", catId=category.id)

@views.route("/category-overview/<catId>/item/<itemId>", methods=['GET', 'POST'])
def item_overview(catId, itemId):
    item = Item.query.get(itemId)
    category = Category.query.get(catId)

    if request.method == 'POST':
        new_price = int(request.form.get('price'))
        if item.price < new_price:
            item.price = new_price
            database.session.commit()
            flash("Bid accepted...", category="success")
            return redirect(request.referrer)
        else:
            flash("New Bid is lower than current bid...", category="error")

    return render_template("item-overview.html", item = item, catId=category.id)