# coding=utf-8
'''
frontend server
对接client请求
请求入口文件

frontend 不用 blueprint
使用动态加载模块、函数的方式，根据请求接口动态调用
'''

import json
import importlib
from flask import Flask, request
from config import MOTHOD_SEPARATE
from helper.helper_ret import HelperRet
from frontend import frontend_server


# 添加入口路由
@frontend_server.route('/', methods=['POST'])
@HelperRet.wraps_parse_params
def index():
    '''
    请求地址：http://127.0.0.1:8577/
    客户端content-type：application/x-www-form-urlencoded
    post参数格式：
    postdata={
                "public":{"version":"208","packid":"100"},
                "request":{"method":"userinfo#getbaseinfo","uid":"66","field":"nickname"},
                "extend":{"net":"wifi","device":"iphone 10 plus","macid":"1"},
                "sig":"c4ca4238a0b923820dcc509a6f75849b",
                "debug":1
            }
    '''
    # 分割出module，function
    module, function = request.x_method.split(MOTHOD_SEPARATE)
    if not module or not function:
        return HelperRet.ret_json(rdata='请求接口%s格式错误！' % request.x_method, rcode=-200)

    # # 动态加载接口模块
    # try:
    #     interface_file = importlib.import_module('frontend.%s.%s' % (module,function))
    # except Exception as e:
    #     # 找不到接口文件
    #     return HelperRet.ret_json(rdata='请求接口%s不存在!' % request.x_method,
    # rcode=-201)

    # # 动态导入接口函数
    # try:
    #     x_function = getattr(interface_file, function)
    # except Exception as e:
    #     # 找不到接口函数
    #     return HelperRet.ret_json(rdata='请求接口%s异常!' % request.x_method, rcode=-202)
    #
    # 执行接口
    # return x_function(request)

    # 或者使用import_string
    from werkzeug.utils import import_string
    try:
        x_function = import_string('frontend.%s.%s.%s' %
                                   (module, function, function))
    except Exception as e:
        return HelperRet.ret_json(rdata='请求接口%s异常!' % request.x_method, rcode=-202)

    # 执行接口
    return x_function(request)


if __name__ == '__main__':
    '''
    启动服务器
    python frontend_server.py
    '''
    frontend_server.run(host=frontend_server.config.get('HOST'),
                        port=frontend_server.config.get('PORT'),
                        threaded=frontend_server.config.get('THREADED'),
                        debug=frontend_server.config.get('DEBUG'))
