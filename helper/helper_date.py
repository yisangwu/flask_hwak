# -*- coding: utf-8 -*-
'''
Helper
@sub_package HelperDate
'''

import datetime
import time


class HelperDate(object):

    def __init__(self):
        pass

    @staticmethod
    def timestamp_now():
        '''
        当前时间戳
        '''
        return int(time.time())

    @staticmethod
    def timestamp_today():
        '''
        今天凌晨0点时间戳
        '''
        return int(time.mktime(time.strptime(str(HelperDate.date_today()),
                               '%Y-%m-%d')))

    @staticmethod
    def date_today():
        '''
        今天日期，%Y-%m-%d格式
        '''
        return datetime.date.doday()

    @staticmethod
    def date_delta_today(day=1):
        '''
        几天前的凌晨零点时间戳
        '''
        return HelperDate.date_today() - datetime.timedelta(days=day)
