# coding=utf-8
'''
x friend
'''
import flask
from flask import render_template, Response
from . import friend_blueprint, extend_base


@friend_blueprint.route('/x')
def x_friend():
    '''
    http://127.0.0.1:8577/friend/x
    # 渲染templates/index.html
    '''
    print(extend_base)
    return render_template('index.html', extend_base=extend_base)
