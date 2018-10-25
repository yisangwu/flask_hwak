# coding=utf-8
'''
friend
'''
import flask
from flask import (Flask, Blueprint)
from config.app import get_templates_path
from helper.helper_class import import_views

friend_blueprint = Blueprint(
    'friend', __name__, url_prefix='/friend', template_folder='templates')

import os
extend_base = os.path.join(get_templates_path(), 'extend_base.html')

# 动态加载目录中所有的views
import_views('backend', 'friend', __file__)
