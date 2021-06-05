# 리뷰 페이지

# 블루프린트
from flask import Blueprint, Flask, request, jsonify

bp = Blueprint(
    'review',  # 블루프린트 이름
    __name__,  # 파일 등록(현재 파일)
    url_prefix='/review',  # 패스 접두사
)

review_data = {'mapx': '', 'mapy': '', 'title': '', 'address': '', 'tel': '', 'description': ''}


@bp.route('', methods=['POST'])
def review_page():
    mapx = request.form['mapx']
    mapy = request.form['mapy']
    title = request.form['title']
    address = request.form['address']
    tel = request.form['tel']
    description = request.form['description']
    img = request.form['img']
    url = request.form['url']
    global review_data
    review_data = {'mapx': mapx, 'mapy': mapy, 'title': title, 'address': address, 'tel': tel,
                   'description': description, 'img': img, 'url': url}

    return jsonify({'result': 'success', 'data': review_data})


@bp.route('/load_data', methods=['POST'])
def load_page():
    global review_data
    print(review_data['mapx'], review_data['mapy'])
    return jsonify({'result': 'success', 'data': review_data})
