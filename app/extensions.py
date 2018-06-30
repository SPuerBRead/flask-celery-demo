# -*- coding: utf-8 -*-
# @Time   : 2018/6/30 下午11:05
# @author : Xmchx
# @File   : extensions.py

from flask import Blueprint
from celery import Celery
from celery_config import CELERY_BROKER_URL, CELERY_RESULT_BACKEND

celery = Celery('app', broker = CELERY_BROKER_URL, backend = CELERY_RESULT_BACKEND,include=['app.task'])