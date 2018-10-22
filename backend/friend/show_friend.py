# coding=utf-8
'''
show friend
'''
import flask
from flask import render_template
from . import blue_friend


@blue_friend.route('/show')
def show():
    # 渲染templates/index.html
    # return render_template('index.html')

    # 渲染templates/friend/index.html
    return render_template('friend/index.html')
