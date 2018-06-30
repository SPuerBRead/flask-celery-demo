# -*- coding: utf-8 -*-
# @Time   : 2018/6/30 下午11:32
# @author : Xmchx
# @File   : view.py

from flask import Blueprint
from .task import task_a, task_b

main = Blueprint('main', __name__)

@main.route('/task1',methods=['GET'])
def func_task_a():
    a = 1
    b = 2
    task_a.apply_async(args=[a, b])
    return str(True)


@main.route('/task2',methods=['GET'])
def func_task_b():
    a = 2
    b = 1
    task_b.apply_async(args=[a, b])
    return str(True)
