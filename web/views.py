from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, current_user, login_required, logout_user

from web.models import Category, Item, Store
from web.repository import webrepository

views = Blueprint("views", __name__)

# ------- NOTHING SPECIAL ------- #
@views.route("/sign-up", methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        webrepository.sign_up()

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

 # ------- OVERVIEWS ------- #
@views.route("/store-overview/<storeId>")
def store_overview(storeId):
    store = Store.query.get(storeId)
    return render_template("store-overview.html", categories=store.categories, storeId=store.id)

@views.route("/<storeId>/category-overview/<catId>")
def category_overview(storeId, catId):
    store = Store.query.get(storeId)
    category = Category.query.get(catId)
    return render_template("category-overview.html", items=category.items, catId=category.id, storeId=store.id)

@views.route("/<storeId>/category-overview/<catId>/item/<itemId>", methods=['GET', 'POST'])
def item_overview(storeId, catId, itemId):
    store = Store.query.get(storeId)
    category = Category.query.get(catId)
    item = Item.query.get(itemId)

    if request.method == 'POST':
        webrepository.logick(itemId)

    return render_template("item-overview.html", item=item, catId=category.id, storeId=store.id)


# ------- ADDS ------- #
@views.route("/addStore", methods=['GET', 'POST'])
def addStore():
    if request.method == 'POST': # Need to add if statement to check if new shop has same name as old
        webrepository.store()
        return redirect(url_for('views.homepage'))

    return render_template("addStore.html")

@views.route("/store-overview/<storeId>/addCategory", methods=['GET', 'POST'])
def addCategory(storeId):
    store = Store.query.get(storeId)
    storeId = store.id
    if request.method == 'POST':
        webrepository.category(storeId)
        return redirect(request.referrer)

    return render_template("addCategory.html", storeId=store.id)

@views.route("/<storeId>/category-overview/<catId>/addItem", methods=['GET', 'POST'])
def addItem(storeId, catId):
    store = Store.query.get(storeId)
    category = Category.query.get(catId)

    if request.method == 'POST':
        webrepository.item(catId)
        return redirect(request.referrer)

    return render_template("addItem.html", catId=category.id, storeId=store.id)