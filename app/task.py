# -*- coding: utf-8 -*-
# @Time   : 2018/6/30 下午11:32
# @author : Xmchx
# @File   : task.py

from app.extensions import celery


@celery.task(bind = True, name='task_a')
def task_a(self, a, b):
    pass

@celery.task(bind = True, name='task_b')
def task_b(self, a, b):
    pass