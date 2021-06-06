import requests
from selenium import webdriver
from selenium.webdriver import ActionChains
from flask import Blueprint, current_app, request, jsonify
import time
import html.parser
import re
# from app import db


bp = Blueprint('camping_data', __name__, url_prefix='/camping_data')

#lists = ["서울시", "부산시", "대구시", "인천시", "광주시", "대전시", "울산시", "세종시", "경기도", "강원도", "충청북도", "충청남도", "전라북도", "전라남도", "경상북도", "경상남도", "제주도"]


@bp.route('', methods=['GET'])
def get_result():
    # form = request.form
    # region = form['region_give']
    region = request.args.get('region_give')

    time.sleep(0.1)

    url = "https://dapi.kakao.com/v2/local/search/keyword.json?query={} 캠핑장&size=10".format(region)
    headers = {"Authorization": "KakaoAK " + current_app.config['REST_API']}

    data = requests.get(url, headers=headers)
    data = data.json()['documents']

    documents = []
    if data:
        for d in data:

            document = {
                'campsite_name': re.sub('<[^>]*>', ' ', html.unescape(d['place_name'])),
                'category' : d['category_name'],
                'address' : d['address_name'],
                'road_address' : d['road_address_name'],
                'phone': d['phone'],
                'link' : d['place_url'],
                'x' : d['x'],
                'y' : d['y']
            }

            documents.append(document)



    return jsonify({'result': 'success',
                    'articles': documents})


# @bp.route('', methods=['GET'])
# def list_result():
#     data = list(db.campsite.find({}, {'_id': False}))
#     result = {
#         'result': 'success',
#         'articles': data,
#     }
#
#     return jsonify(result)