# coding=utf-8
'''
测试配置
'''
from .settings import BaseSettings


class SettingDev(BaseSettings):
    """
    测试配置
    """

    def __init__(self, arg):
        super(SettingTest, self).__init__()
        self.arg = arg

    HOST = '127.0.0.1'

    PORT = 8577

    DEBUG = True

    SQLALCHEMY_ECHO = True
