# 리뷰 페이지

# 블루프린트
from flask import Blueprint, Flask, request, jsonify

bp = Blueprint(
    'review',  # 블루프린트 이름
    __name__,  # 파일 등록(현재 파일)
    url_prefix='/review',  # 패스 접두사
)

review_data = {'mapx': '', 'mapy': '', 'title': '', 'address': '', 'tel': '', 'description': '', 'url': ''}


@bp.route('', methods=['POST'])
def review_page():
    mapx = request.form['mapx']
    mapy = request.form['mapy']
    camping_site = request.form['camping_site']
    address = request.form['address']
    road_address = request.form['road_address']
    category = request.form['category']
    image = request.form['image']
    tag = request.form['tag']
    phone = request.form['phone']
    description = request.form['description']
    link = request.form['link']

    global review_data
    review_data = {'mapx': mapx, 'mapy': mapy, 'camping_site': camping_site, 'address': address,
                   'road_address': road_address, 'phone': phone, 'tag': tag, 'image': image, 'category': category,
                   'description': description, 'link': link}

    return jsonify({'result': 'success', 'data': review_data})


@bp.route('/load_data', methods=['POST'])
def load_page():
    global review_data
    print(review_data['mapx'], review_data['mapy'])
    return jsonify({'result': 'success', 'data': review_data})


@bp.route('/make_review', methods=['POST'])
def make_review():
    # review.html -> review.py로 가져온 데이터 파싱
    user_id = request.form['user_id']
    review_content = request.form['review_content']
    camping_review = request.form['camping_review']

    print(camping_review)
    # 데이터들을 review게시글 db에 삽입

    return jsonify({'result': 'success'})
