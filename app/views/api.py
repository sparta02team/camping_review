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


# 댓글작성 API
