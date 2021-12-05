# def test_valid_registration(test_client, init_database):
#     response = test_client.post('/sign-up', data=dict(
#        name='USER'
#     ))
#     assert response.status_code == 200
#     assert b'ADMIN added...' in response.data