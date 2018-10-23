# coding=utf-8
'''
group
'''
import flask
from flask import (Flask, Blueprint)
from helper.helper_class import import_views

# 注册蓝图
group_blueprint = Blueprint('group', __name__, url_prefix='/group', template_folder='templates')

# 动态加载目录中所有的views
import_views('backend', 'group', __file__)
