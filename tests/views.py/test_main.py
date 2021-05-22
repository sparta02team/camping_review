def test_메인_페이지(client):
    response = client.get('/')

    # assert 조건을 만족하는 것이 테스트 통과 조건
    assert response.status_code == 200
