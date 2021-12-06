from web.repository import businessRepo

def test_provision_with_fixture(new_item):
    price = int(new_item.price)
    provision = price * 0.1

    assert provision == 10