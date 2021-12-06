import pytest

# from web.__init__ import start, database
from web.models import User, Item, Category, Store, Bid, Sale

@pytest.fixture(scope="module")
def new_user():
    user = User("ADMIN")
    return user

@pytest.fixture(scope="module")
def new_store():
    store = Store("Test", "Test", "")
    return store

@pytest.fixture(scope="module")
def new_category():
    category = Category("Test", "Test", "1")
    return category

@pytest.fixture(scope="module")
def new_item():
    item = Item("Producer", "Model", "Description", "100", "3", "A", "", "1")
    return item

@pytest.fixture(scope="module")
def new_bid():
    bid = Bid("1", "1", "150")
    return bid

@pytest.fixture(scope="module")
def new_sale():
    sale = Sale("1", "1")
    return sale