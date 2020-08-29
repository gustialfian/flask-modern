from flask import Blueprint, jsonify, request

from src.database import db_session

from .models import Item
from .serializer import item_schema, items_schema

item_bp = Blueprint('Item', __name__)


@item_bp.route('/', methods=["GET", "POST"])
@item_bp.route('/<id>', methods=["PUT", "DELETE"])
def item_index(id=None):
    if request.method == "GET" and id is None:
        items = Item.query.all()
        items_json = items_schema.dump(items)
        return jsonify({"status": "GET", "data": items_json})

    if request.method == "POST":
        request_json = request.get_json()
        item = Item(name=request_json['name'])
        db_session.add(item)
        item_json = item_schema.dump(item)
        return jsonify({"status": "POST", "data": item_json})

    if request.method == "PUT" and id is not None:
        request_json = request.get_json()
        item = Item.query.get(id)
        item.name = request_json['name']
        item_json = item_schema.dump(item)
        return jsonify({"status": "PUT", "data": item_json})

    if request.method == "DELETE" and id is not None:
        item = Item.query.get(id)

        if item is None:
            return jsonify({"status": "DELETE", "data": "notfound"})

        db_session.delete(item)
        item_json = item_schema.dump(item)
        return jsonify({"status": "DELETE", "data": item_json})

    return jsonify({"status": "not found"})
