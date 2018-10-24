# -*- coding: utf-8 -*-

from flask import request
from helper.helper_ret import HelperRet


def getheader(request):
    '''
    获取下request里面的信息
    '''
    ret = dict()
    ret['host'] = request.host
    ret['host_url'] = request.host_url
    ret['scheme'] = request.scheme
    ret['user_agent'] = str(request.user_agent)
    ret['remote_addr'] = request.remote_addr

    return HelperRet.ret_json(ret)
