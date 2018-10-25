# -*- coding: utf-8 -*-
'''
Helper
@sub_package HelperRet
参数解析，签名校验，响应返回
'''

import functools
import json

from flask import Response, request, jsonify
from config import MOTHOD_SEPARATE
from helper.helper_date import HelperDate
from helper.helper_ip import HelperIp


class HelperRet(object):

    def __init__(self):
        pass

    @staticmethod
    def wraps_parse_params(func):
        '''
        装饰器
        解析请求参数postdata
        '''
        @functools.wraps(func)
        def parse_params(*args, **kwargs):
            # 获取参数， 客户端以表单方式传参
            # content-type：application/x-www-form-urlencoded
            # postdata = json格式字符串
            json_str = request.form.get("postdata")
            if not json_str:
                return HelperRet.ret_json(rdata='POST参数为空!',
                                          rcode=-101)
            # 格式化为dict
            data_dict = json.loads(json_str)
            if not data_dict or not isinstance(data_dict, dict):
                return HelperRet.ret_json(rdata='POST参数格式错误,解析失败!',
                                          rcode=-102)
            # 公共参数
            d_public = data_dict.get('public') or dict()
            # 接口请求参数
            d_request = data_dict.get('request') or dict()
            # 附加参数
            d_extend = data_dict.get('extend') or dict()

            # 赋值到request里面
            request.x_public = d_public
            request.x_request = d_request
            request.x_extend = d_extend

            # 请求接口，返回中使用
            request.x_method = d_request.get('method') or None
            # 接口参数签名
            request.x_sig = data_dict.get('sig') or None
            # 是否为bebug请求
            request.x_debug = data_dict.get('debug') or None
            # 客户端IP
            request.x_client_ip = HelperIp.get_client_ip(request)

            # 公共参数不能为空
            if not d_public or not isinstance(d_public, dict):
                return HelperRet.ret_json(rdata='公共参数为空或格式错误!',
                                          rcode=-103)
            # 接口参数不能为空
            if not d_request or not isinstance(d_request, dict):
                return HelperRet.ret_json(rdata='接口请求参数为空或格式错误!',
                                          rcode=-104)
            # 附加参数不能为空
            if not d_extend or not isinstance(d_extend, dict):
                return HelperRet.ret_json(rdata='附加参数为空或格式错误!',
                                          rcode=-105)
            # 请求接口无效
            if not request.x_method or MOTHOD_SEPARATE not in request.x_method:
                return HelperRet.ret_json(rdata='无效的请求接口！', rcode=106)

            # debug 模式下，不校验签名
            if request.x_debug:
                # 执行使用装饰器的函数
                return func(*args, **kwargs)

            # 非debug模式下，校验签名
            if not request.x_debug:
                if not request.x_sig or len(request.x_sig) != 32:
                    return HelperRet.ret_json(rdata='签名为空或格式错误!',
                                              rcode=-107)
            # 校验参数签名
            sign_dict = dict()
            sign_dict['public'] = d_public
            sign_dict['request'] = d_request
            sign_dict['extend'] = d_extend

            if HelperRet.check_signature(sign_dict) != request.x_sig:
                return HelperRet.ret_json(rdata='参数签名错误!',
                                          rcode=-108)

            # 执行使用装饰器的函数
            return func(*args, **kwargs)

        return parse_params

    @staticmethod
    def check_signature(sign_dict=dict()):
        """
        检查参数签名
        @param sign_dict: dict 参与签名的参数
        @return boolean / string
        """
        if not sign_dict or not isinstance(sign_dict, dict):
            return False
        # 按照key升序排序
        keys = sorted(sign_dict.keys())

        import hashlib
        sign_str = ''
        # key=value格式的字符串，并拼接
        for k in keys:
            sign_str += '%s=%s' % (k, json.dumps(sign_dict.get(k)))

        if not sign_str:
            return False

        # 将密钥拼接到签名字符串最后面
        from config.app import SIGN_SECRET_KEY
        sign_str += SIGN_SECRET_KEY

        return hashlib.md5(sign_str.encode('utf-8')).hexdigest()

    @staticmethod
    def ret_json(rdata=None, rcode=1):
        '''
        统一的接口响应
        @param rdata： string/dict 响应数据， rcode<0 时为string
        @param rcode： int 错误码，默认为1, 正常返回， 小于0 为错误响应
        @return string  json格式字符串
        '''
        # 有无设置x_method
        if hasattr(request, 'x_extend'):
            method = request.x_method
        else:
            method = None

        # 默认值
        ret = dict(method=method,
                   code=rcode,
                   time=HelperDate.timestamp_now())

        # rcode 小于0 为错误，返回错误信息
        if rcode < 0:
            rdata = str(rdata) if rdata else '接口响应错误!'
        else:
            if not isinstance(rdata, dict):
                rdata = dict()

        ret['data'] = rdata
        # 可以 return Response(json.dumps(ret), content_type='application/json')

        return jsonify(ret)
