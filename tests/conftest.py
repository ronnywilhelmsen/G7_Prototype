import pytest

from web import start, database
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
    item = Item("Producer", "Model", "Description", "123", "3", "A", "", "1")
    return item

@pytest.fixture(scope="module")
def new_bid():
    bid = Bid("1", "1", "150")
    return bid

@pytest.fixture(scope="module")
def new_sale():
    sale = Sale("1", "1")
    return sale

@pytest.fixture(scope="module")
def test_client():
    app = start()

    with app.test_client() as testing_client:
        with app.app_context():
            yield testing_client

@pytest.fixture(scope='module')
def init_database(test_client):
    # Create the database and the database table
    database.create_all()

    # Insert user data
    user1 = User('OWNER')
    database.session.add(user1)

    database.session.commit()

    yield

@pytest.fixture(scope='function')
def login_user(test_client):
    test_client.post('/login',
                     data=dict(name='ADMIN'),
                     follow_redirects=True)

    yield  # this is where the testing happens!

    test_client.get('/logout', follow_redirects=True)