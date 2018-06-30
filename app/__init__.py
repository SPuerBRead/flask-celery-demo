# -*- coding: utf-8 -*-
# @Time   : 2018/6/30 下午11:05
# @author : Xmchx
# @File   : __init__.py


from flask import Flask, Blueprint
from .extensions import celery
from .view import main

def create_app():
    app = Flask(__name__)
    app.config.from_object('flask_config')
    app.register_blueprint(main)
    return app
