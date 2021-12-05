import unittest
from flask import current_app
from web.__init__ import start, database
from web.models import User, Item, Category, Store, Bid, Sale

class TestWebApp(unittest.TestCase):
    def setUp(self):
        self.app = start()
        self.appctx = self.app.app_context()
        self.appctx.push()
        database.create_all()
        self.client = self.app.test_client()

    def tearDown(self):
        database.drop_all()
        self.appctx.pop()
        self.app = None
        self.appctx = None

    def populate_db(self):
        user = User(name="ADMIN")
        store = Store("Test", "Test", "")
        category = Category("Test", "Test", "1")
        item = Item("Producer", "Model", "Description", "123", "3", "A", "", "1")
        bid = Bid("1", "1", "150")
        sale = Sale("1", "1")
        database.session.add(user, store, category, item, bid, sale)
        database.session.commit()

    def test_app(self):
        assert self.app is not None
        assert current_app == self.app

    def test_registration_form(self):
        response = self.client.get('/sign-up')
        assert response.status_code == 200
        html = response.get_data(as_text=True)

        assert 'name="name"' in html

    def test_login_form(self):
        response = self.client.get('/login')
        assert response.status_code == 200
        html = response.get_data(as_text=True)

        assert 'name="name"' in html

    def test_store_form(self):
        response = self.client.get('/addStore')
        assert response.status_code == 200
        html = response.get_data(as_text=True)

        assert 'name="name"' in html
        assert 'name="description"' in html

    def test_category_form(self):
        response = self.client.get('/store-overview/1/addCategory')
        assert response.status_code == 200
        html = response.get_data(as_text=True)

        assert 'name="name"' in html
        assert 'name="description"' in html

    def test_item_form(self):
        response = self.client.get('/1/category-overview/1/addItem')
        assert response.status_code == 200
        html = response.get_data(as_text=True)

        assert 'name="producer"' in html
        assert 'name="model"' in html
        assert 'name="description"' in html
        assert 'name="price"' in html
        assert 'name="duration"' in html
        assert 'name="type"' in html
        assert 'name="picture_url"' in html

    def test_register_user(self):
        response = self.client.get('/sign-up', data={
            'name': "ADMIN"
        }, follow_redirects=True)
        assert response.status_code == 200
        response = self.client.get('/login', data={
            'name': "ADMIN"
        }, follow_redirects=True)
        assert response.status_code == 200