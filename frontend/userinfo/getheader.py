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

    from flask import current_app
    current_app.logger.error('this is a error')
    current_app.logger.info('this is a info')
    current_app.logger.warning('this is a wraning')
    current_app.logger.debug('this is a debug')

    from helper.Helper_log import HelperLog
    HelperLog('main').log.error('dsadsadsadsasad')
    HelperLog('aaaa').log.info('infoinfoinfoinfo')
    HelperLog('aaaa').log.debug('debugdebugdebugdebug')
    HelperLog('aaaa').log.warning('warningwarningwarning')
    return HelperRet.ret_json(ret)
