import os
import requests
from selenium import webdriver
from selenium.webdriver import ActionChains
import time
import html.parser
import re
from pymongo import MongoClient
import random
import os


client = MongoClient(os.environ['MONGODB_HOST'])
rest_api = os.environ['REST_API']
db = client.get_database('camping_review')
db.campsite.remove({})


lists = ["서울시", "부산시", "대구시", "인천시", "광주시", "대전시", "울산시", "세종시", "경기도", "강원도", "충청북도", "충청남도", "전라북도", "전라남도",
         "경상북도", "경상남도", "제주도"]

try:
    for region in lists:
        url = "https://dapi.kakao.com/v2/local/search/keyword.json?query={} 캠핑장&size=9".format(region)
        headers = {"Authorization": "KakaoAK " + rest_api}

        time.sleep(0.1)

        data = requests.get(url, headers=headers)
        data = data.json()['documents']

        documents = []
        if data:
            for d in data:

                document = {
                    'region': region,
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

        print(documents)

        for document in documents:
            place_id = document['link'].split('/')[-1]
            document['tag'] = []
            document['image'] = ''
            document['description'] = ''

            URL_DETAILS_PAGE = "https://place.map.kakao.com/main/v/"
            place_details = requests.get(URL_DETAILS_PAGE + place_id).json()

            try:
                tags = place_details['basicInfo']['metaKeywordList']
                for tag in tags:
                    document['tag'].append(tag)

                photo_list = place_details['photo']

                time.sleep(0.1)

                for p in photo_list['photoList'][0]['list']:
                    if 'daum' in p['orgurl'] or 'kakao' in p['orgurl']:
                        document['image'] = p['orgurl']
                    else:
                        document['image'] = '../static/assets/img/bg-showcase-' + str(random.randint(1, 5)) + '.jpg'
                # document['image'] = photo_list['photoList'][0]['list'][0]['orgurl']
                document['description'] = place_details['basicInfo']['introduction']

            except:
                pass

        db.campsite.insert_many(documents)

except Exception as e:
    print(e)
