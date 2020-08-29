from flask import Blueprint, jsonify, request

from src.database import db_session

from .models import User
from .serializer import user_schema, users_schema

user_bp = Blueprint('User', __name__)


@user_bp.route('/', methods=["GET", "POST"])
@user_bp.route('/<id>', methods=["PUT", "DELETE"])
def index(id=None):
    if request.method == "GET" and id is None:
        users = User.query.all()
        users_json = users_schema.dump(users)
        return jsonify({"status": "GET", "data": users_json})

    if request.method == "POST":
        request_json = request.get_json()
        user = User(username=request_json['username'],
                    password=request_json['password'])
        db_session.add(user)
        user_json = user_schema.dump(user)
        return jsonify({"status": "POST", "data": user_json})

    if request.method == "PUT" and id is not None:
        request_json = request.get_json()
        user = User.query.get(id)
        user.username = request_json['username']
        user_json = user_schema.dump(user)
        return jsonify({"status": "PUT", "data": user_json})

    if request.method == "DELETE" and id is not None:
        user = User.query.get(id)

        if user is None:
            return jsonify({"status": "DELETE", "data": "notfound"})

        db_session.delete(user)
        user_json = user_schema.dump(user)
        return jsonify({"status": "DELETE", "data": user_json})

    return jsonify({"status": "not found"})
