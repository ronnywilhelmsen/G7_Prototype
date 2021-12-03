import pytest

from web import database, start
from web.models import User, Item, Category, Store
from flask_login import login_user, current_user, logout_user

@pytest.fixture(scope="module")
def new_user():
    user = User("ADMIN")
    return user

@pytest.fixture(scope="module")
def new_item():
    item = Item("Test", "Test", "Test", "123", "1", "A", "", "1")
    return item

@pytest.fixture(scope="module")
def new_category():
    category = Category("Test", "Test", "1")
    return category

@pytest.fixture(scope="module")
def new_store():
    store = Store("Test", "Test", "")
    return store

@pytest.fixture(scope="module")
def test_client():
    app = start()

    with app.test_client() as testing_client:
        with app.app_context():
            yield testing_client

@pytest.fixture(scope="module")
def init_database(test_client):

    user1 = User(name="Test1")
    user2 = User(name="Test2")

    database.session.add(user1)
    database.session.add(user2)

    database.session.commit()

    yield

    database.delete(user1)
    database.delete(user2)