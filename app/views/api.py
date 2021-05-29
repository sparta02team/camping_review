import datetime
from flask import Blueprint, request, jsonify
import hashlib
from app import db

# 블루프린트
bp = Blueprint(
    'api',  # 블루프린트 이름
    __name__,  # 파일 등록(현재 파일)
    url_prefix='/api',  # 패스 접두사
)


# 데이터 베이스 연결

# 회원가입 API
@bp.route('/register', methods=['POST'])
def api_register():
    # register.html 에서 건내온 데이터 변수설정
    id = request.form['id_give']
    pw = request.form['pw_give']
    nickname = request.form['nickname_give']
    email = request.form['email_give']

    # password salting
    pw_hash = hashlib.sha256(pw.encode()).hexdigest()

    # db insert
    db.user.insert_one({'id': id, 'pw': pw_hash, 'nickname': nickname, 'email': email})
    return jsonify({'result': 'success'})


# 리뷰작성 API
# 추천수 api 따로 만들어야함
# 조회수는 리뷰 게시글 화면을 불러들이는 api 에서 조회수 증가기능 추가
@bp.route('/writeReview', methods=['POST'])
def api_write_review():
    # 리뷰 작성 페이지에서 건내온 데이터 변수 설정
    review_user_no = request.form['review_user_no_give']  # 게시글 번호
    review_title = request.form['review_title_give']  # 게시글 제목
    review_no = request.form['review_no_give']  # 회원번호
    review_write = request.form['review_write_give']  # 게시글 내용
    review_date = datetime.datetime.utcnow()  # 등록일자
    review_gets = 1  # 게시글 조회수
    review_hits = 0  # 게시글 추천수

    # db insert
    db.reviews.insert_one(
        {'user_no': review_user_no, 'title': review_title, 'date': review_date, 'review_no': review_no,
         'write': review_write, 'gets': review_gets, 'hits': review_hits})
    return jsonify({'result': 'success'})


# 댓글작성 API
@bp.route('/comment', methods=['POST'])
def api_comment():
    # 댓글 작성창에서 건내온 데이터 변수 설정
    comment_no = request.form['comment_no_give']  # 코멘트번호
    comment_review_no = request.form['comment_review_no_give']  # 게시글번호
    comment_user_no = request.form['comment_user_no_give']  # 회원번호
    comment_write = request.form['comment_write_give']  # 코멘트 내용
    comment_date = datetime.datetime.utcnow()  # 등록일자

    db.comment.insert_one({'comment_review_no': comment_review_no,
                           'comment_no': comment_no, 'comment_user_no': comment_user_no, 'comment_write': comment_write,
                           'comment_date': comment_date})

    return jsonify({'result': 'success'})
