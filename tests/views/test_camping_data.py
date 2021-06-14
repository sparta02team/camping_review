def test_list_result(client):
    response = client.get('/camping_data/crawling')
    assert response.status_code == 200


def test_list_result(client):
    data = {
        'region_give': '서울시'
    }
    response = client.get('/camping_data', data=data)
    assert response.status_code == 200
