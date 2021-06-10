import os
from dotenv import load_dotenv

# .env 파일을 환경변수로 설정
load_dotenv()

# 환경변수 읽어오기
JWT_SECRET = os.environ['JWT_SECRET']

# Daum 검색 API
KAKAO_REST_API = os.environ['KAKAO_REST_API']


# Naver 검색 API
NAVER_LOGIN_CLIENT_ID = os.environ['NAVER_LOGIN_CLIENT_ID']
NAVER_LOGIN_CLIENT_SECRET = os.environ['NAVER_LOGIN_CLIENT_SECRET']

# CALLBACK_URL
NAVER_LOGIN_SERVICE_URL = os.environ['NAVER_LOGIN_SERVICE_URL']
NAVER_LOGIN_CALLBACK_URL = os.environ['NAVER_LOGIN_CALLBACK_URL']

