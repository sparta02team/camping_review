def test_review_page(client):
    data = {
        'mapx' : '100',
        'mapy' : '100',
        'title' : 'test',
        'address' : '서울시',
        'tel' : '010-1111-1111',
        'description' : '좋은 곳입네다',
        'img' : '',
        'url' : 'www.naver.com'
    }
    response = client.post(
        '/review',
        data = data
    )
    assert response.status_code == 200

def test_load_page(client):
    data = {
        'mapx' : '100',
        'mapy' : '100',
        'title' : 'test',
        'address' : '서울시',
        'tel' : '010-1111-1111',
        'description' : '좋은 곳입네다',
        'img' : '',
        'url' : 'www.naver.com'
    }
    response = client.post(
        '/load_data',
        data = data
    )
    assert response.status_code == 200

def test_make_review(client):
    data = {
        'user_id' : 'test_user',
        'review_content' : '테스트',
        'camping_review' : '캠핑은 좋으나 돈이 없도다'
    }
    response = client.post(
        '/make_review',
        data = data
    )
    response.status_code == 200