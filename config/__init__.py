# -*- coding: utf-8 -*-
"""
APP 核心配置
"""
import os

# 环境
ENVIRONMENT = 'development'

# 参数签名KEY
SIGN_SECRET_KEY = 'Pqcfje5NL0sx@WbB9-drYVki'
# 分隔符
MOTHOD_SEPARATE = '#'

# 项目根目录，绝对路径
PATH_ROOT = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

# templates 目录
PATH_TEMPLATES = os.path.join(PATH_ROOT, 'templates')

# frontend 目录
PATH_FRONTEND = os.path.join(PATH_ROOT, 'frontend')

# backend 目录
PATH_BACKEND = os.path.join(PATH_ROOT, 'backend')

# log日志目录
PATH_LOG = os.path.join(PATH_ROOT, 'logs')


def load_settings():
    """
    根据环境变量，加载配置
    """
    if ENVIRONMENT in ['development']:
        from .setting_dev import SettingDev
        return SettingDev
    elif ENVIRONMENT in ['production']:
        from .setting_pro import SettingPro
        return SettingPro
    else:
        from .settings import BaseSettings
        return BaseSettings
