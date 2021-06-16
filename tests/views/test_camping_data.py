from pymongo import MongoClient

test_database_name = 'camping_review_test'
client = MongoClient('localhost', 27017)
db = client.get_database(test_database_name)

def test_list_result(client):
    data = {
        'region_give': '부산시'
    }
    response = client.get(
        '/camping_data',
        data=data
    )

    campsite = db.campsite.find_one(
        {'region': 'region_give'},
        {'_id': False}
    )

    assert response.status_code == 200
    assert response.json['result'] == 'success'

