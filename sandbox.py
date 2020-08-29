from flask import Blueprint, Flask, jsonify, request
from flask_marshmallow import Marshmallow
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

DB_URI = 'postgresql://sandbox:sandbox@localhost:6543/sandbox'
engine = create_engine(DB_URI, convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    print('database.init_db(app)')
    Base.metadata.create_all(bind=engine)


class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))

    def __init__(self, name=None):
        self.name = name

    def __repr__(self):
        return "<Item {}>".format(self.name)


app = Flask(__name__)
init_db()

ma = Marshmallow(app)


class ItemSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Item

    id = ma.auto_field()
    name = ma.auto_field()


item_schema = ItemSchema()
items_schema = ItemSchema(many=True)


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.commit()
    db_session.remove()


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


app.register_blueprint(item_bp, url_prefix="/items")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
