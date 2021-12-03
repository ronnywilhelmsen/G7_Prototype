from web import start

def test_homepage(test_client):
    app = start()
    with app.test_client() as test_client:
        response = test_client.get('/')
        assert response.status_code == 200

def test_store_overview(test_client):
    app = start()
    with app.test_client() as test_client:
        response = test_client.get('/store-overview/1')
        assert response.status_code == 200

def test_category_overview(test_client):
    app = start()

    with app.test_client() as test_client:
        response = test_client.get('/1/category-overview/1')
        assert response.status_code == 200

def test_item_overview(test_client):
    app = start()

    with app.test_client() as test_client:
        response = test_client.get('/1/category-overview/1/item/1')
        assert response.status_code == 200

def test_add_new_store(test_client):
    app = start()

    with app.test_client() as test_client:
        response = test_client.get('/addStore')
        assert response.status_code == 200

def test_add_new_category(test_client):
    app = start()

    with app.test_client() as test_client:
        response = test_client.get('/store-overview/1/addCategory')
        assert response.status_code == 200

def test_add_new_item(test_client):
    app = start()

    with app.test_client() as test_client:
        response = test_client.get('/1/category-overview/1/addItem')
        assert response.status_code == 200