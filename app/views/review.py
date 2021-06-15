# 리뷰 페이지

# 블루프린트
from flask import Blueprint, Flask, request, jsonify, render_template
from app import db


bp = Blueprint(
    'review',  # 블루프린트 이름
    __name__,  # 파일 등록(현재 파일)
    url_prefix='/review',  # 패스 접두사
)

review_data = {'mapx': '', 'mapy': '', 'camping_site': '', 'address': '',
               'road_address': '', 'phone': '', 'tag': '', 'image': '', 'category': '',
               'description': '', 'link': '', 'user_id': ''}


@bp.route('', methods=['POST'])
def review_page():
    camping_site = request.form['camping_site']
    # mapx = request.form['mapx']
    # mapy = request.form['mapy']
    # address = request.form['address']
    # road_address = request.form['road_address']
    # category = request.form['category']
    # image = request.form['image']
    # tag = request.form['tag']
    # phone = request.form['phone']
    # description = request.form['description']
    # link = request.form['link']
    # user_id = request.form['user_id']

    data = list(db.campsite.find({'campsite_name': camping_site}, {'_id': False}))

    global review_data
    for d in data:
        review_data = {'mapx': d['x'], 'mapy': d['y'], 'camping_site': d['campsite_name'], 'address': d['address'],
                       'road_address': d['road_address'], 'phone': d['phone'], 'tag': d['tag'], 'image': d['image'], 'category': d['category'],
                       'description': d['description'], 'link': d['link'], 'user_id': 'user_id'}

    return jsonify({'result': 'success', 'data': review_data})


@bp.route('/load_data', methods=['POST'])
def load_page():
    global review_data
    return jsonify({'result': 'success', 'data': review_data})


@bp.route('/make_review', methods=['POST'])
def make_review():
    review_text = request.form['review_text']

    review_data['review_text'] = review_text

    if db.review.count() == 0:
        review_data['index'] = 1
    else:
        # 인덱싱 필드 작업 필요 일단 삭제 기능 없이 구현
        index = int(db.review.find_one({'index': db.review.count()})['index'])
        review_data['index'] = index + 1

    db.review.insert(review_data)

    return jsonify({'result': 'success'})


@bp.route('/count_review', methods=['GET'])
def count_review():
    camping_site = request.args.get('camping_site')

    data = db.review.count({'camping_site': camping_site})
    result = {
        'result': 'success',
        'articles': data,
    }

    return jsonify(result)

