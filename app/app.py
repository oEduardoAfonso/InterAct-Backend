from flask import Flask
from flask_sqlalchemy import SQLAlchemy

def create_app(config_class = None):
    app = Flask(__name__)
    app.config.from_object(config_class)
    app.db = SQLAlchemy(app)
    init_app(app)
    return app

def init_app(app):
    @app.route('/')
    @app.route('/index')
    def index():
        return "Hello World"