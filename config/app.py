# -*- coding: utf-8 -*-
'''
APP 核心配置
'''
# 参数签名KEY
SIGN_SECRET_KEY = 'Pqcfje5NL0sx@WbB9-drYVki'

# 分隔符
MOTHOD_SEPARATE = '#'

import os

# 项目根目录，绝对路径
PATH_ROOT = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

# templates 目录
PATH_TEMPLATES = os.path.join(PATH_ROOT, 'templates')

# frontend 目录
PATH_FRONTEND = os.path.join(PATH_ROOT, 'frontend')

# backend 目录
PATH_BACKEND = os.path.join(PATH_ROOT, 'backend')
