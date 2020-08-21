from flask import Flask, jsonify
from src import hello


def create_app():
    app = Flask(__name__)
    register_routes(app)
    register_blueprint(app)
    return app


def register_routes(app):
    @app.route('/')
    def hello_world():
        return jsonify('Hello')


def register_blueprint(app):
    app.register_blueprint(hello.handlers.blueprint, url_prefix='/hello')
