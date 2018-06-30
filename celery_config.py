# -*- coding: utf-8 -*-
# @Time   : 2018/6/30 下午11:11
# @author : Xmchx
# @File   : celery_config.py

RABBITMQ_USERNAME = 'celery'
RABBITMQ_PASSWORD = '123456'
RABBITMQ_HOST = 'localhost'
RABBITMQ_VHOST = 'celery_vhost'


CELERY_BROKER_URL = 'amqp://{username}:{password}@{host}/{vhost}'.format(
    username = RABBITMQ_USERNAME,
    password = RABBITMQ_PASSWORD,
    host = RABBITMQ_HOST,
    vhost = RABBITMQ_VHOST)

CELERY_RESULT_BACKEND = 'amqp://'