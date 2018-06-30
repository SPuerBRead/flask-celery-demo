# -*- coding: utf-8 -*-
# @Time   : 2018/6/30 下午6:21
# @author : Xmchx
# @File   : worker.py


from celery import Celery

celery = Celery('worker', broker='amqp://celery:123456@192.168.199.133/celery_vhost', backend='amqp://')

@celery.task(bind = True, name='task_a')
def task_a(self, x, y):
    return x + y

@celery.task(bind = True, name='task_b')
def task_b(self, x, y):
    return x - y
