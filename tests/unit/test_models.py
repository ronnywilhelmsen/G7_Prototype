from web.models import User, Store, Item, Category

def test_new_user_with_fixture(new_user):
    user = User("HEI")
    assert user.name == "HEI"

def test_new_category_with_fixture(new_category):
    category = Category("Test", "Test")
    assert category.name == "Test"
    assert category.description == "Test"

def test_new_item_with_fixture(new_item):
    item = Item("Test", "Test", "Test", "123")
    assert item.producer == "Test"
    assert item.model == "Test"
    assert item.description == "Test"
    assert item.price == "123"

def test_new_store_with_fixture(new_store):
    store = Store("Test", "Test")
    assert store.name == "Test"
    assert store.description == "Test"