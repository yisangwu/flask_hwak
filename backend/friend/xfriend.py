# coding=utf-8
"""
x friend
"""
import flask
from flask import render_template, Response
from . import friend_blueprint


@friend_blueprint.route('/x')
def x_friend():
    """
    http://127.0.0.1:8577/friend/x
    渲染templates/index.html
    :return:
    """
    data = dict(a=1, b=2, c=3)
    return render_template('index.html', data=data)
