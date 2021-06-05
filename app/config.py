import os
from dotenv import load_dotenv

# .env 파일을 환경변수로 설정
load_dotenv()

# 환경변수 읽어오기
JWT_SECRET = os.environ['JWT_SECRET']
CLIENT_ID = os.environ['CLIENT_ID']
CLIENT_SECRET = os.environ['CLIENT_SECRET']
