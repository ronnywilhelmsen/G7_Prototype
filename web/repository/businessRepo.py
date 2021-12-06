from flask import request, flash, redirect
from flask_login import current_user

from web.models import Item, Bid, Sale

from web import database

def bid(itemId):
    new_price = int(request.form.get('price'))
    if current_user.is_authenticated:
        item = Item.query.get(itemId)
        itemid = item.id

        user = current_user
        userid = user.id
        if new_price > item.price:
            new_bid = Bid(userId = itemid, itemId = userid, price = new_price)
            item.price = new_bid.price
            database.session.add(new_bid)
            database.session.commit()
            flash("You successfully bid on " + item.model, category="success")
            return redirect(request.referrer)
        else:
            flash("New Bid is lower than current bid...", category="error")
    else:
        flash("You need to be logged in to make a bid...", category="error")

def sale(itemId):

    if current_user.is_authenticated:
        item = Item.query.get(itemId)
        itemid = item.id

        user = current_user
        userid = user.id

        new_sale = Sale(userId = userid, itemId = itemid)
        database.session.add(new_sale)
        database.session.commit()
        flash("You added " + item.model + " to cart", category="success")
        return redirect(request.referrer)
    else:
        flash("You need to be logged in to add item to cart...", category="error")