# coding=utf-8

'''
Helper
@subpackage Helper_Singleton
单例模式
'''
class HelperSingleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(HelperSingleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance