# coding=utf-8
"""
Helper Log
"""
import logging
from config import load_settings
from helper.helper_class import ObjSingleton


LOG_TYPE_DICT = dict(
    main='ERROR',
    frontend='INFO',
    backend='ERROR',
    model='ERROR',
    helper=None,
)


class HelperLog(ObjSingleton):
    logger = None
    settings = None

    def __init__(self):
        pass
    # def __init__(self, name='log'):
    #
    #     log_default_name = 'logs'
    #     settings = load_settings()
    #
    #     self.logger = logging.getLogger(__name__)
    #
    #     if name and name in LOG_TYPE_DICT:
    #         name = name.strip()
    #         log_name = name if name else log_default_name
    #         log_level = LOG_TYPE_DICT.get(name, settings.LOG_LEVEL)
    #     else:
    #         log_name = name
    #         log_level= settings.LOG_LEVEL
    #
    #     handler = logging.FileHandler(settings.LOG_FILE % log_name, encoding='UTF-8')
    #     handler.setLevel(log_level)
    #     logging_format = logging.Formatter(settings.LOG_FORMAT)
    #     handler.setFormatter(logging_format)
    #
    #     self.logger.addHandler(handler)

    @staticmethod
    def get_app_setting():
        """
        获取app的设置
        :return:
        """
        return load_settings()

    @staticmethod
    def log(name='log'):
        """
        自定义log名称，写log日志
        每天一个文件
        :param name: 名称
        :return:
        """
        log_default_name = 'logs'
        settings = HelperLog.get_app_setting()

        if name and name in LOG_TYPE_DICT:
            name = name.strip()
            log_name = name if name else log_default_name
            log_level = LOG_TYPE_DICT.get(name, settings.LOG_LEVEL)
        else:
            log_name = name
            log_level = settings.LOG_LEVEL

        logger = logging.getLogger(log_name)
        handler = logging.FileHandler(settings.LOG_FILE % log_name, encoding='UTF-8')
        handler.setLevel(log_level)
        logging_format = logging.Formatter(settings.LOG_FORMAT)
        handler.setFormatter(logging_format)

        logger.addHandler(handler)
        return logger

    @staticmethod
    def log_handler_all():
        """
        在 app 中注册，一次写入，LOG_TYPE_DICT的每个log
        每天一个文件
        :return:
        """
        settings = HelperLog.get_app_setting()
        if not settings:
            return False

        log_handler_list = list()
        for log_name, log_level in LOG_TYPE_DICT.items():
            handler = logging.FileHandler(settings.LOG_FILE % log_name, encoding='UTF-8')
            if not log_level:
                log_level = settings.LOG_LEVEL
            handler.setLevel(log_level)
            logging_format = logging.Formatter(settings.LOG_FORMAT)
            handler.setFormatter(logging_format)
            log_handler_list.append(handler)

        return log_handler_list

    @staticmethod
    def log_handler(app_name=None):
        """
        app 公用一个log文件
        每天一个文件
        :param app_name:  当前app名
        :return:
        """
        if not app_name:
            app_name = 'app'
        settings = HelperLog.get_app_setting()
        if not settings:
            return False

        handler = logging.FileHandler(settings.LOG_FILE % app_name, encoding='UTF-8')
        handler.setLevel(settings.LOG_LEVEL)
        logging_format = logging.Formatter(settings.LOG_FORMAT)
        handler.setFormatter(logging_format)
        return handler
