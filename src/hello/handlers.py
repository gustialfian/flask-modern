from flask import Blueprint, jsonify
blueprint = Blueprint('hello', __name__)


@blueprint.route('/')
def index():
    return jsonify({'status': 'success', 'data': 'Hello modern-flask'})
