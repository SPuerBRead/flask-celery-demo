# -*- coding: utf-8 -*-
# @Time   : 2018/6/30 下午11:04
# @author : Xmchx
# @File   : web.py

from gevent.pywsgi import WSGIServer
from app import create_app

app = create_app()

if __name__ == '__main__':
    http_server = WSGIServer(('',5000),app)
    http_server.serve_forever()