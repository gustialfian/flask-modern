from flask import Flask

from src.database import init_db
from src.items.blueprint import item_bp
from src.users.blueprint import user_bp


def create_app():
    app = Flask(__name__)
    init_db(app)
    register_blueprint(app)
    return app


def register_blueprint(app):
    app.register_blueprint(item_bp, url_prefix="/items")
    app.register_blueprint(user_bp, url_prefix="/users")
