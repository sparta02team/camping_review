from flask import Flask
from pymongo import MongoClient
import os

client = MongoClient('localhost', 27017)
db = None


def create_app(database_name='camping_review'):
    # 플라스크 웹 서버 생성하기
    app = Flask(__name__)
    app.debug = True
    app.config.from_pyfile('config.py')

    global db
    db = client.get_database(database_name)

    from app.views import main, api, camping_data
    app.register_blueprint(main.bp)
    app.register_blueprint(api.bp)
    app.register_blueprint(camping_data.bp)

    return app
