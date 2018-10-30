# -*- coding: utf-8 -*-
"""
Helper
String
"""


class HelperString(object):

    def __init__(self):
        pass

    @staticmethod
    def make_percentage(radio=None):
        """
        处理百分比
        :param radio: 要处理的数值
        :return:
        """
        pre_format = '%s%%'
        if not radio:
            return pre_format % 0

        if isinstance(radio, int):
            return pre_format % radio
        elif isinstance(radio, float):
            str_radio = '{:.2f}'.format(radio)
            if '.00' in str_radio:
                return pre_format % str_radio.replace('.00', '')
            return pre_format % str_radio
        else:
            return pre_format % radio
