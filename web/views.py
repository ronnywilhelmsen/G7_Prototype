from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, current_user, logout_user

from web.models import Category, Item, Store, User, Bid, Sale
from web.repository import webrepository
from web.repository import buisnesslogic
from web.repository import authrepo

views = Blueprint("views", __name__)

# ------- NOTHING SPECIAL ------- #
@views.route("/sign-up", methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        authrepo.sign_up()

        return redirect(url_for('views.homepage'))

    return render_template("signup.html", user=current_user)

@views.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        authrepo.login()

    return render_template("login.html")

@views.route("/logout", methods=['GET', 'POST'])
def logout():
    logout_user()
    flash("You logged out", category="success")
    return redirect(url_for('views.homepage'))

@views.route("/")
def homepage():
    return render_template("home.html", stores=Store.query.all(), user=current_user)

 # ------- OVERVIEWS ------- #
@views.route("/store-overview/<storeId>")
def store_overview(storeId):
    store = Store.query.get(storeId)
    categories = store.categories
    return render_template("store-overview.html", categories=categories, store=store, user=current_user)

@views.route("/cart-overview")
def cart_overview():

    user = current_user
    cart = user.cart
    items = Item.query.all()

    return render_template("cart-overview.html", user = user, cart=cart, items=items)

@views.route("/bid-history")
def bid_history():

    user = current_user
    bid = user.bid
    items = Item.query.all()

    return render_template("bid-history.html", user=user, bid=bid, items=items)

@views.route("/<storeId>/category-overview/<catId>")
def category_overview(storeId, catId):
    store = Store.query.get(storeId)
    category = Category.query.get(catId)
    items = category.items

    return render_template("category-overview.html", items=items, category=category, store=store, user=current_user)

@views.route("/<storeId>/category-overview/<catId>/item/<itemId>", methods=['GET', 'POST'])
def item_overview(storeId, catId, itemId):
    store = Store.query.get(storeId)
    category = Category.query.get(catId)
    item = Item.query.get(itemId)

    if request.method == 'POST':
        if item.type == "A":
            buisnesslogic.bid(itemId)
        else:
            buisnesslogic.sale(itemId)
            flash("You bought " + item.model, category="success")

    return render_template("item-overview.html", item=item, category=category, store=store, user=current_user)

# ------- ADDS ------- #
@views.route("/addStore", methods=['GET', 'POST'])
def addStore():
    if request.method == 'POST': # Need to add if statement to check if new shop has same name as old
        webrepository.store()
        return redirect(url_for('views.homepage'))

    return render_template("addStore.html", user=current_user)

@views.route("/store-overview/<storeId>/addCategory", methods=['GET', 'POST'])
def addCategory(storeId):
    store = Store.query.get(storeId)
    storeId = store.id
    if request.method == 'POST':
        webrepository.category(storeId)
        return redirect(request.referrer)

    return render_template("addCategory.html", storeId=storeId, user=current_user)

@views.route("/<storeId>/category-overview/<catId>/addItem", methods=['GET', 'POST'])
def addItem(storeId, catId):
    store = Store.query.get(storeId)
    category = Category.query.get(catId)

    if request.method == 'POST':
        webrepository.item(catId)
        return redirect(request.referrer)

    return render_template("addItem.html", category=category, store=store, user=current_user)