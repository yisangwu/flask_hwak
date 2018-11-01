# coding=utf-8
"""
Helper Log
"""
import logging
from config import load_settings


class HelperLog(object):

    @staticmethod
    def log_handler():
        settings = load_settings()
        if not settings:
            return False

        handler = logging.FileHandler(settings.LOG_FILE, encoding='UTF-8')
        handler.setLevel(settings.LOG_LEVEL)
        handler.setFormatter(settings.LOG_FORMAT)

        return handler
