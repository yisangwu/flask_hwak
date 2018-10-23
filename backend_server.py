# -*- coding: utf-8 -*-
'''
请求入口文件

backend 使用 blueprint
使用动态注册蓝图的方式，根据url路由访问
'''


import os
import json
import importlib
from flask import Flask
from flask import request, url_for, redirect
from config.app import get_backend_path
from helper.helper_ret import HelperRet


backend_server = Flask(__name__)

# 遍历backend下面目录
# 按规则注册蓝图
BACKEN_PATH = get_backend_path()
try:
    backend_dir = os.listdir(BACKEN_PATH)
except Exception as e:
    raise 'backend_dir listdir failed!'

# 目录为空，或者不是list
if not backend_dir or not isinstance(backend_dir, list):
    raise 'backend_dir is empty!'


from werkzeug.utils import import_string
# 遍历注册 Blueprint
for blue_dir in backend_dir:
    # 不是目录，忽略
    if not os.path.isdir(os.path.join(BACKEN_PATH, blue_dir)):
        continue

    # 缓存目录，忽略
    if blue_dir.startswith('_'):
        continue

    # 导入并注册
    class_blueprint = import_string('%s.%s.%s_blueprint' % ('backend', blue_dir, blue_dir))
    backend_server.register_blueprint(class_blueprint, url_prefix='/%s' % blue_dir)


if __name__ == '__main__':
    '''
    运行server
    python backend_server.py
    '''
    backend_server.run(host='127.0.0.1',
            port=8577,
            threaded=True,
            debug=True)
