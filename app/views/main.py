from flask import Blueprint, current_app, request, render_template, session
import jwt
from app import db


bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('', methods=['GET'])  # 데코레이터 문법
def index():  # 함수 이름은 고유해야 한다
    token = request.cookies.get('loginToken')

    if token:
        try:
            payload = jwt.decode(
                token, current_app.config['JWT_SECRET'], algorithms=['HS256'])
            articles = list(db.campsite.find(
                {'id': payload['id']}, {'_id': False}))
        except jwt.exceptions.ExpiredSignatureError:
            articles = []
    else:
        articles = []
    return render_template('index.html', articles=articles)


@bp.route('/register', methods=['GET'])
def register():
    return render_template('register.html')


@bp.route('/login', methods=['GET'])
def login():
    NAVER_LOGIN_CLIENT_ID = current_app.config['NAVER_LOGIN_CLIENT_ID']
    NAVER_LOGIN_SERVICE_URL = current_app.config['NAVER_LOGIN_SERVICE_URL']
    NAVER_LOGIN_CALLBACK_URL = current_app.config['NAVER_LOGIN_CALLBACK_URL']
    return render_template('login.html', NAVER_LOGIN_CLIENT_ID=NAVER_LOGIN_CLIENT_ID, NAVER_LOGIN_SERVICE_URL=NAVER_LOGIN_SERVICE_URL, NAVER_LOGIN_CALLBACK_URL=NAVER_LOGIN_CALLBACK_URL)

@bp.route('/review',methods=['GET'])
def review():
    return render_template('review.html')
