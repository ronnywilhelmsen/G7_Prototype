import unittest
from unittest import mock
from flask import current_app
from flask_login import current_user
from web.__init__ import start, database
from web.models import User, Item, Category, Store, Bid, Sale
from flask_login import login_user, logout_user

class TestRecipes(unittest.TestCase):
    def setUp(self):
        self.app = start()
        self.appctx = self.app.app_context()
        self.appctx.push()
        self.client = self.app.test_client()

    def tearDown(self):
        self.appctx.pop()
        self.app = None
        self.appctx = None

    def test_app(self):
        assert self.app is not None
        assert current_app == self.app

    def test_to_see_if_stores_get_added_to_systemoversikt_ID_2(self):
        response = self.client.get('/')
        assert response.status_code == 200
        html = response.get_data(as_text=True)

        assert 'HIOF' in html

    def test_to_see_if_categories_get_added_to_butikkoversikt_ID_3(self):
        response = self.client.get('/store-overview/1')
        assert response.status_code == 200
        html = response.get_data(as_text=True)

        assert 'Bøker' in html

    def test_to_see_if_items_get_added_to_kategorioversikt_ID_4(self):
        response = self.client.get('/1/category-overview/1')
        assert response.status_code == 200
        html = response.get_data(as_text=True)

        assert 'For Auction' in html
        assert 'Producer: Matematikk' in html

    def test_to_see_if_a_item_has_it_own_vareoversikt_ID_4_5(self):
        response = self.client.get('/1/category-overview/1/item/1')
        assert response.status_code == 200
        html = response.get_data(as_text=True)

        assert 'This Item is for Auction' in html
        assert 'Producer: Matematikk' in html

    def test_if_signup_form_contains_right_parameters_ID1_1(self):
        response = self.client.get('/sign-up')
        assert response.status_code == 200
        html = response.get_data(as_text=True)

        assert 'name="name"' in html

    def test_if_login_form_contains_right_parameters_ID_1_2(self):
        response = self.client.get('/login')
        assert response.status_code == 200
        html = response.get_data(as_text=True)

        assert 'name="name"' in html

    def test_if_store_form_contains_right_parameters_ID_2_1(self):
        response = self.client.get('/addStore')
        assert response.status_code == 200
        html = response.get_data(as_text=True)

        assert 'name="name"' in html
        assert 'name="description"' in html

    def test_if_category_form_contains_right_parameters_form_ID_3_2(self):
        response = self.client.get('/store-overview/1/addCategory')
        assert response.status_code == 200
        html = response.get_data(as_text=True)

        assert 'name="name"' in html
        assert 'name="description"' in html

    def test_if_item_form_contains_right_parameters_ID_4_2(self):
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

    def test_if_possible_to_visit_added_store_ID_2_3(self):
        response = self.client.get('/store-overview/1')
        assert response.status_code == 200

    def test_if_possible_to_visit_added_category_ID_3_3(self):
        response = self.client.get('/1/category-overview/1')
        assert response.status_code == 200

    def test_if_possible_to_visit_added_item_ID_4_4(self):
        response = self.client.get('/1/category-overview/1/item/1')
        assert response.status_code == 200