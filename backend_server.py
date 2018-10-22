# -*- coding: utf-8 -*-
'''
请求入口文件

frontend 不用 blueprint
使用动态加载模块、函数的方式，根据请求接口动态调用
'''

import json
import importlib
from flask import Flask
from flask import request, url_for, redirect
from helper.helper_ret import HelperRet

backend_server = Flask(__name__)


from backend.friend import blue_friend

backend_server.register_blueprint(blue_friend, url_prefix='/friend')

if __name__ == '__main__':
    '''
    运行server
    python backend_server.py
    '''
    backend_server.run(host='127.0.0.1',
            port=8577,
            threaded=True,
            debug=True)
