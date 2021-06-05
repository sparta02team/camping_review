import pytest
from pymongo import MongoClient
import app as flask_app
test_database_name = 'camping_review_test'
client = MongoClient('localhost', 27017)
db = client.get_database(test_database_name)


@pytest.fixture
def app():
    test_app = flask_app.create_app(database_name=test_database_name)

    # 제네레이터 문법(중고급 문법이라 패스)
    yield test_app
    # 모든 테스트를 마치고 정리하는 부분
    client.drop_database(test_database_name)
    print('테스트 DB 제거 완료')
