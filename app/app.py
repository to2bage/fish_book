"""
Project name: fish_book
Description:
Create Time: 2020/7/31 08:14
Author: to2bage
Email: to2bage@hotmail.com
Version: 0.1
"""
from flask import Flask

from app.web import web
from app.models.base import db

def create_app():
    app = Flask(__package__)  # app = Flask(__package__, template_folder="web/templates")

    app.config.from_object("app.config.secret")
    app.config.from_object("app.config.settings")

    register_blueprint(app)
    register_plugin(app)

    print(app.url_map)
    return app

def register_blueprint(app: Flask):
    app.register_blueprint(web)

def register_plugin(app: Flask):
    db.init_app(app)

    with app.app_context():
        db.create_all()
