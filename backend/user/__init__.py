# coding=utf-8
'''
user
'''
import flask
from flask import (Flask, Blueprint)

user_blueprint = Blueprint('user', __name__, url_prefix='/user', template_folder='templates')