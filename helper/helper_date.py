# -*- coding: utf-8 -*-
"""
Helper
@sub_package HelperDate
"""

import datetime
import time

# 默认的日期Ymd-年月日格式
DEFAULT_DATE_Ymd = '%Y-%m-%d'


class HelperDate(object):

    def __init__(self):
        pass

    @staticmethod
    def timestamp_now():
        """
        当前时间戳
        """
        return int(time.time())

    @staticmethod
    def timestamp_today():
        """
        今天凌晨0点时间戳
        """
        return int(time.mktime(time.strptime(HelperDate.date_today(), DEFAULT_DATE_Ymd)))

    @staticmethod
    def date_today(date_format=DEFAULT_DATE_Ymd):
        """
        今天日期，默认为%Y%m%d格式
        :param date_format:
        :return:
        """
        return time.strftime(date_format, time.localtime())

    @staticmethod
    def date_before_today(days=1):
        """
        今天前几天，%Y-%m-%d格式
        :param days:  今天的前几天
        :return:
        """
        return str(datetime.date.today() - datetime.timedelta(days=days))

    @staticmethod
    def date_after_today(days=1):
        """
        今天后几天，%Y-%m-%d格式
        :param days:
        :return: %Y-%m-%d
        """
        return str(datetime.date.today() + datetime.timedelta(days=days))
