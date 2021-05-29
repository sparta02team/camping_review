from flask import Blueprint, render_template

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('', methods=['GET'])  # 데코레이터 문법
def index():  # 함수 이름은 고유해야 한다
    return render_template('index.html')


@bp.route('register', methods=['GET'])
def register():
    return render_template('register.html')
