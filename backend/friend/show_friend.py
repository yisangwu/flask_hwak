# coding=utf-8
"""
show friend
"""
import flask
from flask import render_template, Response
from . import friend_blueprint


@friend_blueprint.route('/show')
def show():
    """
    http://127.0.0.1:8577/friend/show
    :return:
    """
    # 渲染templates/index.html
    # return render_template('index.html')

    # 渲染templates/friend/index.html
    data = dict(aa=1, bb=2, cc=3)
    return render_template('friend/index.html', **data)


@friend_blueprint.route('/')
def index():
    """
    http://127.0.0.1:8577/friend/
    :return:
    """
    return Response('132465')
