# -*- coding: utf-8 -*-
'''
Helper
@sub_package HelperIp
'''

import datetime
import time


class HelperIp(object):

    def __init__(self):
        pass

    @staticmethod
    def get_client_ip(request):
        client_ip = request.headers.get('HTTP_CDN_SRC_IP', '')
        # 没有
        if not client_ip:
            client_ip = request.headers.get('HTTP_WL_PROXY_CLIENT_IP', '')

        if not client_ip:
            client_x_ip = request.headers.get('HTTP_X_FORWARDED_FOR', '')
            if client_x_ip:
                client_ip = client_x_ip.split(',')[0]

        if not client_ip:
            client_ip = request.headers.get('HTTP_X_REAL_IP', '')

        if not client_ip:
            client_ip = request.remote_addr or ''

        return client_ip.strip()
