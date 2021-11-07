from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, current_user, login_required, logout_user

from . import database
from web.models import Category, Item, Store, User

views = Blueprint("views", __name__)

@views.route("/sign-up", methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        name = request.form.get('name')

        flash(name + " added...", category="success")
        new_User = User(name=name)
        database.session.add(new_User)
        database.session.commit()

        login_user(new_User)

        return redirect(url_for('views.homepage'))

    return render_template("signup.html", user=current_user)

@views.route("/login")
def login():
    return render_template("login.html")

@views.route("/")
def firstPage():
    return render_template("firstPage.html")

@views.route("/homepage")
def homepage():
    return render_template("home.html", stores=Store.query.all())

@views.route("/store-overview/<storeId>")
def store_overview(storeId):
    store = Store.query.get(storeId)
    return render_template("store-overview.html", categories=store.categories, storeId=store.id)

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

@views.route("/addStore", methods=['GET', 'POST'])
def addStore():
    if request.method == 'POST':
        store()
        return redirect(url_for('views.homepage'))

    return render_template("addStore.html")

@views.route("/<storeId>/category-overview/<catId>")
def category_overview(storeId, catId):
    store = Store.query.get(storeId)
    category = Category.query.get(catId)
    return render_template("category-overview.html", items=category.items, catId=category.id, storeId=store.id)

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

@views.route("/store-overview/<storeId>/addCategory", methods=['GET', 'POST'])
def addCategory(storeId):
    store = Store.query.get(storeId)
    storeId = store.id
    if request.method == 'POST':
        category(storeId)
        return redirect(request.referrer)

    return render_template("addCategory.html", storeId=store.id)

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

@views.route("/<storeId>/category-overview/<catId>/addItem", methods=['GET', 'POST'])
def addItem(storeId, catId):
    store = Store.query.get(storeId)
    category = Category.query.get(catId)
    catId = category.id

    if request.method == 'POST':
        item(catId)
        return redirect(request.referrer)

    return render_template("addItem.html", catId=category.id, storeId=store.id)

@views.route("/<storeId>/category-overview/<catId>/item/<itemId>", methods=['GET', 'POST'])
def item_overview(storeId, catId, itemId):
    store = Store.query.get(storeId)
    category = Category.query.get(catId)
    item = Item.query.get(itemId)

    if request.method == 'POST':
        new_price = int(request.form.get('price'))
        if new_price > item.price:
            item.price = new_price
            database.session.commit()
            flash("Bid accepted...", category="success")
            return redirect(request.referrer)
        else:
            flash("New Bid is lower than current bid...", category="error")

    return render_template("item-overview.html", item=item, catId=category.id, storeId=store.id)