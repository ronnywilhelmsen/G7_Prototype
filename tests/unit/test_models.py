def test_new_user_with_fixture(new_user):
    assert new_user.name == "ADMIN"

def test_new_store_with_fixture(new_store):
    assert new_store.name == "Test"
    assert new_store.description == "Test"
    assert new_store.picture_url == ""

def test_new_category_with_fixture(new_category):
    assert new_category.name == "Test"
    assert new_category.description == "Test"
    assert new_category.store_id == "1"

def test_new_item_with_fixture(new_item):
    assert new_item.producer == "Producer"
    assert new_item.model == "Model"
    assert new_item.description == "Description"
    assert new_item.price == "100"
    assert new_item.duration == "3"
    assert new_item.type == "A"
    assert new_item.picture_url == ""
    assert new_item.category_id == "1"

def test_new_bid_with_fixture(new_bid):
    assert new_bid.userId == "1"
    assert new_bid.itemId == "1"
    assert new_bid.price == "150"

def test_new_sale_with_fixture(new_sale):
    assert new_sale.userId == "1"
    assert new_sale.itemId == "1"