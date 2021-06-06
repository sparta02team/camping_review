import os
from dotenv import load_dotenv

# .env 파일을 환경변수로 설정
load_dotenv()

# 환경변수 읽어오기
JWT_SECRET = os.environ['JWT_SECRET']

# Naver 검색 API
CLIENT_ID = os.environ['CLIENT_ID']
CLIENT_SECRET = os.environ['CLIENT_SECRET']

# Daum 검색 API
REST_API = os.environ['REST_API']

# 크롬 드라이버
CHROME_DRIVER = os.environ['CHROME_DRIVER']

# CALLBACK_URL
CALLBACK_URL = os.environ['CALLBACK_URL']
SERVICE_URL = os.environ['SERVICE_URL']

