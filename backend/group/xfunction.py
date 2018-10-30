# coding=utf-8
"""
group
"""

import flask
from flask import Flask, Response
from . import group_blueprint


@group_blueprint.route('/xx')
def xx():
    """

    :return:
    """
    return Response('xfunction -0-0 xx!')
