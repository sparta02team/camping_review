import pprint

from flask import Blueprint, Flask, request, jsonify, render_template
from app import db

bp = Blueprint(
    'review_page',  # 블루프린트 이름
    __name__,  # 파일 등록(현재 파일)
    url_prefix='/review_page',  # 패스 접두사
)
index = 0


@bp.route('', methods=['POST'])
def review_page():
    global index
    index = request.form['index']

    return jsonify({'result': 'success'})


@bp.route('/campingReview', methods=['POST'])
def get_camping_review():
    global index
    index = int(index)

    camping_data = db.review.find_one({'index': index}, {'_id': False})

    return jsonify({'result': 'success', 'camping_data': camping_data})
