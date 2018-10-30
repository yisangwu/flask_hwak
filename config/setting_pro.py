# coding=utf-8
"""
正式配置
"""
from .settings import BaseSettings


class SettingPro(BaseSettings):
    """
    正式配置
    """
    def __init__(self, arg):
        super(SettingPro, self).__init__()
        self.arg = arg

    DEBUG = True

    TESTING = True

    HOST = '127.0.0.1'

    PORT = 8588

    SQLALCHEMY_ECHO = False
