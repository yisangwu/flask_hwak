# coding=utf-8
'''
friend
'''
import flask
from flask import (Flask, Blueprint)
from helper.helper_class import import_views

friend_blueprint = Blueprint(
    'friend', __name__, url_prefix='/friend', template_folder='templates')

# 动态加载目录中所有的views
import_views('backend', 'friend', __file__)
