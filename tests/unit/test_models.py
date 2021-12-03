from web.models import User, Store, Item, Category

def test_new_user_with_fixture(new_user):
    user = User("HEI")
    assert user.name == "HEI"

def test_new_store_with_fixture(new_store):
    store = Store("Test", "Test", "")
    assert store.name == "Test"
    assert store.description == "Test"
    assert store.picture_url == ""

def test_new_category_with_fixture(new_category):
    category = Category("Test", "Test", "1")
    assert category.name == "Test"
    assert category.description == "Test"
    assert category.store_id == "1"

def test_new_item_with_fixture(new_item):
    item = Item("Producer", "Model", "Description", "123", "3", "A", "", "1") # Producer, Model, Description, Price, Duration, Type, PicURL, CatId
    assert item.producer == "Producer"
    assert item.model == "Model"
    assert item.description == "Description"
    assert item.price == "123"
    assert item.duration == "3"
    assert item.type == "A"
    assert item.picture_url == ""
    assert item.category_id == "1"