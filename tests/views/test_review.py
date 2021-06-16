def test_review_page(client):
    data = {
        'camping_site': '난지캠핑장',
        'user_id': 'test'
        # 'mapx': '100',
        # 'mapy': '100',
        # 'address': '서울시',
        # 'road_address': '구로구',
        # 'category': '카테고리',
        # 'image': 'image',
        # 'tag': 'tag',
        # 'phone': '010-1111-1111',
        # 'description': '좋은 곳입네다',
        # 'link': 'www.naver.com',
        # 'user_id': 'test_id'
    }

    response = client.post(
        '/review',
        data=data
    )
    assert response.status_code == 200


def test_load_page(client):
    data = {
        'mapx': '100',
        'mapy': '100',
        'camping_site': 'camping_site',
        'address': '서울시',
        'road_address': '구로구',
        'category': '카테고리',
        'image': 'image',
        'tag': 'tag',
        'phone': '010-1111-1111',
        'description': '좋은 곳입네다',
        'link': 'www.naver.com',
        'user_id': 'test_id'
    }
    response = client.post(
        '/review/load_data',
        data=data
    )
    assert response.status_code == 200


def test_make_review(client):
    data = {
        'mapx': '100',
        'mapy': '100',
        'camping_site': 'camping_site',
        'address': '서울시',
        'road_address': '구로구',
        'category': '카테고리',
        'image': 'image',
        'tag': 'tag',
        'phone': '010-1111-1111',
        'description': '좋은 곳입네다',
        'link': 'www.naver.com',
        'user_id': 'test_id',
        'review_text':'review_text',
        'index':1
    }
    response = client.post(
        '/review/make_review',
        data=data
    )
    response.status_code == 200
