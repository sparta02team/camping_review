def test_get_result(client):
    response = client.get('/camping_data')
    assert response.status_code == 200