from flask import Flask, jsonify

from src.database import db_session
from src import hello, users

app = Flask(__name__)
app.register_blueprint(hello.handlers.blueprint, url_prefix='/hello')
app.register_blueprint(users.views.blueprint, url_prefix='/users')


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()
