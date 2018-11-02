# -*- coding: utf-8 -*-
from helper.helper_ret import HelperRet
from helper.Helper_log import HelperLog


def getheader(request):
    """
    获取下request里面的信息
    :param request:
    :return:
    """
    ret = dict()
    ret['host'] = request.host
    ret['host_url'] = request.host_url
    ret['scheme'] = request.scheme
    ret['user_agent'] = str(request.user_agent)
    ret['remote_addr'] = request.remote_addr

    HelperLog.log('aaa').error('aaa')
    HelperLog.log('bbb').error('bbb')
    HelperLog.log('ccc').error('ccc')
    HelperLog.log('ddd').warning('ddd')

    return HelperRet.ret_json(ret)
