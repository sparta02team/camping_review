from flask import Flask
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = None


def create_app(database_name='sparta'):
    # 플라스크 웹 서버 생성하기
    app = Flask(__name__)
    app.debug = True
    # app.config.from_pyfile('config.py')

    global db
    db = client.get_database(database_name)

    from .views import main
    app.register_blueprint(main.bp)

    return app
