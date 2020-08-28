from flask import Blueprint, jsonify, request

from src.database import db_session
from src.models.user import User

blueprint = Blueprint('users', __name__)


@blueprint.route("/", methods=["GET", "POST"])
@blueprint.route("/<id>", methods=["GET", "PUT", "DELETE"])
def methods(id=None):
	if request.method == "GET" and id:
		return get_id_methods(id)

	if request.method == "POST":
		return post_methods()

	if request.method == "PUT":
		return put_methods(id)

	if request.method == "DELETE":
		return delete_methods(id)

	return get_methods()


def get_methods():
	user = User.query.all()
	print(user)
	return jsonify({
		"msg": "hit get",
		"args": request.args,
		"data": [],
	})


def get_id_methods(id):
	return jsonify({
		"msg": "hit get",
		"id": id,
	})


def post_methods():
	u = User('admin', 'admin@localhost')
	db_session.add(u)
	db_session.commit()
	return jsonify({
		"msg": "hit post",
		"get_json": request.get_json(),
	})

def put_methods(id):
	return jsonify({
		"msg": "hit put",
		"id": id,
		"get_json": request.get_json(),
	})

def delete_methods(id):
	return jsonify({
		"msg": "hit delete",
		"id": id,
	})
