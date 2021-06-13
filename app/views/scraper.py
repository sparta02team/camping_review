import os
import requests
from selenium import webdriver
from selenium.webdriver import ActionChains
import time
import html.parser
import re
from pymongo import MongoClient
import os

client = MongoClient(os.environ['MONGODB_HOST'])
db = client.get_database('camping_review')
db.campsite.remove({})

lists = ["서울시", "부산시", "대구시", "인천시", "광주시", "대전시", "울산시", "세종시", "경기도", "강원도", "충청북도", "충청남도", "전라북도", "전라남도",
         "경상북도", "경상남도", "제주도"]

try:
    for region in lists:
        url = "https://dapi.kakao.com/v2/local/search/keyword.json?query={} 캠핑장&size=9".format(region)
        headers = {"Authorization": "KakaoAK " + os.environ['REST_API']}

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

        for document in documents:
            url = document['link']
            document['tag'] = []
            document['image'] = ''
            document['description'] = ''

            # chrome_driver = os.path.join('chromedriver')
            options = webdriver.ChromeOptions()
            options.add_argument("start-maximized")
            options.add_argument("headless")
            options.add_argument("disable-gpu")
            options.add_argument("--no-sandbox")

            driver = webdriver.Chrome('chromedriver', options=options)
            driver.get(url)
            driver.implicitly_wait(0.3)

            try:
                tags = driver.find_elements_by_xpath("//a[contains(text(),'#') and @class='link_tag']")
                for tag in tags:
                    document['tag'].append(tag.text)

                image = driver.find_element_by_css_selector('a.link_photo').get_attribute('style')
                # action = ActionChains(driver)
                # action.move_to_element(image).perform()
                document['image'] = image.split('background-image: url("')[1][:-3]

                description = driver.find_element_by_css_selector('p.txt_introduce')
                document['description'] = description.text

            except:
                pass

            driver.close()

            print(documents)
        db.campsite.insert_many(documents)

except Exception as e:
    print(e)
