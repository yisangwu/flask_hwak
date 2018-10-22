# coding=utf-8
'''
user
'''
import flask
from flask import (Flask, Blueprint)

blue_user = Blueprint('user', __name__, url_prefix='/user', template_folder='templates')