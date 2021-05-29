from flask import Blueprint, current_app, request, render_template
import jwt
from app import db


bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('', methods=['GET'])  # 데코레이터 문법
def index():  # 함수 이름은 고유해야 한다
    token = request.cookies.get('loginToken')
    if token:
        try:
            payload = jwt.decode(token, current_app.config['JWT_SECRET'], algorithms=['HS256'])
            print(payload)
            articles = list(db.campsite.find({'id': payload['id']}, {'_id': False}))
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
    return render_template('login.html')