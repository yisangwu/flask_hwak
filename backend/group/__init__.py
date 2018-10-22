# coding=utf-8
'''
group
'''
import os
import flask
from flask import (Flask, Blueprint)

# 注册蓝图
group_blueprint = Blueprint('group', __name__, url_prefix='/group', template_folder='templates')

# 当前目录
path = os.path.dirname(os.path.realpath(__file__))
print(path)
# list当前目录文件
DIR_FILE_LIST = os.listdir(path)

# 开始导入
if DIR_FILE_LIST:
    from werkzeug.utils import import_string
    # 遍历导入
    for py_file in DIR_FILE_LIST:
        # 目录，忽略
        if os.path.isdir(py_file):
            continue
        # __init__ 忽略
        if py_file.startswith('_'):
            continue
        # 不是 .py 后缀的。忽略
        if '.' not in py_file or py_file.split('.')[-1] != 'py':
            continue
        # 导入
        import_string('%s.%s.%s' % ('backend', 'group', py_file.split('.')[0]))
