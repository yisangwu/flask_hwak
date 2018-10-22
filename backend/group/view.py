# coding=utf-8
'''
group
'''

import flask
from flask import Flask, Response
from . import group_blueprint


@group_blueprint.route('/hello')
def hello():
    '''
    http://127.0.0.1:8577/group/hello
    '''
    return Response('group hello!')
