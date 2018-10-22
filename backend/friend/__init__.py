# coding=utf-8
'''
friend
'''
import flask
from flask import (Flask, Blueprint)

friend_blueprint = Blueprint('friend', __name__, url_prefix='/friend', template_folder='templates')

from . import show_friend