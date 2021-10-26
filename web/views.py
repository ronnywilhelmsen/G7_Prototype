from flask import Blueprint, render_template, request, flash, redirect, url_for

from . import database
from web.models import Category, Item

views = Blueprint("views", __name__)

@views.route("/")
def homepage():
    return render_template("home.html", categories=Category.query.all())

@views.route("/category-overview")
def category_overview():
    return render_template("category-overview.html", items=Item.query.all())

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

@views.route("/addItem", methods=['GET', 'POST'])
def addItem():
    if request.method == 'POST':
        producer = request.form.get('producer')
        model = request.form.get('model')
        description = request.form.get('description')
        price = request.form.get('price')

        flash("Item has been added to auction...", category="success")
        new_item = Item(producer=producer, model=model, description=description, price=price)
        database.session.add(new_item)
        database.session.commit()
        return redirect(url_for('views.category-overview.html'))

    return render_template("addItem.html")