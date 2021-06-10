import jwt
from flask import Blueprint, request, current_app, jsonify

bp = Blueprint('user', __name__, url_prefix='/user')


@bp.route('', methods=['POST'])
def user_info():
    token_receive = request.headers['authorization']
    token = token_receive.split()[1]
    # print(token)

    try:
        payload = jwt.decode(token, current_app.config['JWT_SECRET'], algorithms=['HS256'])
        print(payload)
        return jsonify({'result': 'success', 'id': payload['id']})
    except jwt.exceptions.ExpiredSignatureError:
        return jsonify({'result': 'fail'})