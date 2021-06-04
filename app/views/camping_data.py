import pprint

import requests
from flask import Blueprint, current_app, request, jsonify
import time
import html.parser
import re
from app import db


bp = Blueprint('camping_data', __name__, url_prefix='/camping_data')

#lists = ["서울시", "부산시", "대구시", "인천시", "광주시", "대전시", "울산시", "세종시", "경기도", "강원도", "충청북도", "충청남도", "전라북도", "전라남도", "경상북도", "경상남도", "제주도"]

@bp.route('/get_result', methods=['GET'])
def get_naver_result():
    form = request.form
    region = form['region_give']

    time.sleep(0.1)
    url = f"https://openapi.naver.com/v1/search/local.json?query={region} 캠핑장&display=5&start=1&sort=random"
    headers = {'X-Naver-Client-Id': current_app.config['CLIENT_ID'],
               'X-Naver-Client-Secret': current_app.config['CLIENT_SECRET']}

    data = requests.get(url, headers=headers)

    data = data.json()['items']
    pprint.pprint(data)
    if data:
        for d in data:

            document = {

                'campsite_name': re.sub('<[^>]*>', ' ', html.unescape(d['title'])),
                'category' : d['category'],
                'address' : d['address'],
                'road_address': d['roadAddress'],
                'link' : d['link']
            }

            db.campsite.insert_one(document)

    return jsonify({'result': 'succcess'})


@bp.route('', methods=['GET'])
def list_result():
    data = list(db.campsite.find({}, {'_id': False}))
    result = {
        'result': 'success',
        'articles': data,
    }

    return jsonify(result)

