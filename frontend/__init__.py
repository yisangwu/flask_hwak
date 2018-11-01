# coding=utf-8

from flask import Flask
from config import load_settings
from helper.Helper_log import HelperLog

# 实例化Flask对象
frontend_server = Flask(import_name='frontend')  # __name__

# Load config
frontend_server.config.from_object(load_settings())
# set logging
frontend_server.logger.addHandler(HelperLog.log_handler('frontend'))
