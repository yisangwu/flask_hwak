# -*- coding: utf-8 -*-

from flask import request
from helper.helper_ret import HelperRet


def getbaseinfo(request):
    '''
    获取下postdata的参数
    '''
    ret = dict()
    ret['x_public'] = request.x_public
    ret['x_request'] = request.x_request
    ret['x_extend'] = request.x_extend
    ret['version'] = request.x_public.get('version') or 0
    ret['uid'] = request.x_request.get('uid') or 0

    return HelperRet.ret_json(ret)
