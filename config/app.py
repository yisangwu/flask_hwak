# -*- coding: utf-8 -*-
'''
APP 核心配置
'''
# 参数签名KEY
SIGN_SECRET_KEY = 'Pqcfje5NL0sx@WbB9-drYVki'

# 分隔符
MOTHOD_SEPARATE = '#'

import os


def get_root_path():
    '''
    项目根目录，绝对路径
    '''
    return os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


def get_templates_path():
    '''
    公共模板目录
    '''
    return get_root_path() + os.sep + 'templates'


def get_frontend_path():
    '''
    frontend 路径
    '''
    return get_root_path() + os.sep + 'frontend'


def get_backend_path():
    '''
    backend 路径
    '''
    return get_root_path() + os.sep + 'backend'
