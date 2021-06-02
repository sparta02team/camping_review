import hashlib

from pymongo import MongoClient

test_database_name = 'camping_review_test'
client = MongoClient('localhost', 27017)
db = client.get_database(test_database_name)


def test_login(client):
    user = db.user.find_one({'id': 'tester01'}, {'_id': False})
    data = {
        'id_give': 'test',
        'pw_give': 'test1'
    }
    response = client.post(
        '/api/login',
        data=data
    )
    assert response.status_code == 200  # 회원가입 API 테스트


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


# 리뷰 게시글 작성 테스트 api
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


# 댓글 작성 테스트 api
def test_comment(client):
    data = {
        'comment_no_give': '3',
        'comment_review_no_give': '2',
        'comment_user_no_give': '4',
        'comment_write_give': 'test'
    }

    response = client.post(
        '/api/comment',
        data=data
    )
    assert response.status_code == 200
    assert response.json['result'] == 'success'

    comment = db.comment.find_one({'comment_no': '3'})
    assert comment['comment_write'] == 'test'
