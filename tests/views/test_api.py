import hashlib

from pymongo import MongoClient

test_database_name = 'camping_review_test'
client = MongoClient('localhost', 27017)
db = client.get_database(test_database_name)


# 회원가입 API 테스트
def test_register(client):
    data = {
        'id_give': 'tester01',
        'pw_give': 'test',
        'nickname_give': 'testNickname',
        'email_give': 'test@test.com'

    }

    response = client.post(
        '/api/register',
        data=data
    )

    assert response.status_code == 200

    user = db.user.find_one({'id': 'tester01'}, {'_id': False})

    # 패스워드 평문저장하지 않음
    print(user['id'])
    assert user['pw'] != 'test'
    pw_hash = hashlib.sha256('test'.encode()).hexdigest()
    assert user['pw'] == pw_hash


# 리뷰 게시글 작성 api
def test_write_review(client):
    data = {
        'review_user_no': '1',
        'review_title': 'test',
        'review_no': '1',
        'review_write': 'reviewtest'

    }

    response = client.post(
        '/api/writeReview',
        data=data
    )

    assert response.status_code == 200
    assert response.json['result'] == 'success'

    review = db.reviews.find_one({'user_no': '1'})

    assert review['write'] == 'reviewtest'
