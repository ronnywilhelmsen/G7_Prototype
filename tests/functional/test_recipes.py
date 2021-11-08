from web import start

def test_homepage(test_client):
    app = start()

    with app.test_client() as test_client:
        response = test_client.get('/homepage')
        assert response.status_code == 200
        assert b"Insert awesome name" in response.data
        assert b"Insert an even more awesome slogan" in response.data

def test_store_overview(test_client):
    app = start()

    with app.test_client() as test_client:
        response = test_client.get('/store-overview/1')
        assert response.status_code == 200
        assert b"Insert awesome name" in response.data
        assert b"Insert an even more awesome slogan" in response.data
        assert b"Add new category (STORE)" in response.data
        assert b"Categories" in response.data

def test_category_overview(test_client):
    app = start()

    with app.test_client() as test_client:
        response = test_client.get('/1/category-overview/1')
        assert response.status_code == 200
        assert b"Back" in response.data
        assert b"List new Item for Auction" in response.data
        assert b"Show Item" in response.data

def test_item_overview(test_client):
    app = start()

    with app.test_client() as test_client:
        response = test_client.get('/1/category-overview/1/item/1')
        assert response.status_code == 200
        assert b"Back" in response.data
        assert b"Submit Bid" in response.data

def test_add_new_store(test_client):
    app = start()

    with app.test_client() as test_client:
        response = test_client.get('/addStore')
        assert response.status_code == 200
        assert b"Add new store" in response.data
        assert b"Store name" in response.data
        assert b"Store description" in response.data
        assert b"Store picture url" in response.data
        assert b"Submit" in response.data

def test_add_new_category(test_client):
    app = start()

    with app.test_client() as test_client:
        response = test_client.get('/store-overview/1/addCategory')
        assert response.status_code == 200
        assert b"Back" in response.data
        assert b"Add new category" in response.data
        assert b"Category name" in response.data
        assert b"Category description" in response.data
        assert b"Submit" in response.data

def test_add_new_item(test_client):
    app = start()

    with app.test_client() as test_client:
        response = test_client.get('/1/category-overview/1/addItem')
        assert response.status_code == 200
        assert b"Back" in response.data
        assert b"Item producer" in response.data
        assert b"Item model" in response.data
        assert b"Item description" in response.data
        assert b"Item Price" in response.data
        assert b"End time" in response.data
        assert b"Item Url" in response.data
        assert b"Submit" in response.data
