import unittest
from unittest import mock
from flask import current_app
from flask_login import current_user
from web.__init__ import start, database
from web.models import User, Item, Category, Store, Bid, Sale
from flask_login import login_user, logout_user


class TestUsers(unittest.TestCase):

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


    def test_if_user_login_works_ID1_2(self):
        with self.app.test_request_context():

            user = User('ADMIN')
            login_user(user)

            assert current_user == user
            assert current_user.is_authenticated
            assert current_user.is_active

            logout_user()

    def test_if_user_logout_works_ID1_2(self):
        with self.app.test_request_context():

            user = User('ADMIN')
            login_user(user)

            assert current_user == user

            logout_user()

            assert current_user != user