from flask import request, flash, redirect
from flask_login import login_user

from web.models import User

from web import database

def sign_up():
    name = request.form.get('name')

    flash(name + " added...", category="success")
    new_User = User(name=name)
    database.session.add(new_User)
    database.session.commit()

    login_user(new_User, remember=True)

def login():
    name = request.form.get('name')

    user = User.query.filter_by(name=name).first()
    if user:
        login_user(user, remember=User)
        flash("Successfully logged in as " + user.name, category="success")
        return redirect("/")
    else:
        flash("Username does not exist", category="error")