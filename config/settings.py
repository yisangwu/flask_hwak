# coding=utf-8
"""
Flask APP配置
app = Flask(__name__)
1. 直接设置
  	app.config['TESTING'] = True
	某些配置值还转移到了 Flask 对象中，可以直接通过 Flask 来操作:
	app.testing = True
	一次更新多个配置值可以使用 dict.update() 方法:
	    app.config.update(
	        TESTING=True,
	        SECRET_KEY=b'aaa'
	    )

2. 通过对象加载
    app.config.from_object('yourapplication.default_settings')
3. 通过环境变量加载配置
    export MyAppConfig=/path/to/settings.cfg
    app.config.from_envvar('MyAppConfig')
4. 通过配置文件
   app.config.from_pyfile('dev_config.py') #  这里dev_config.py是文件
"""
import os
from config import PATH_LOG
from helper.helper_date import HelperDate


class BaseSettings(object):
    """
    基本配置
    不同环境的配置都继承此类
    """
    # 密钥用于会话 cookie 的安全签名，并可用于应用或者扩展的其他安全需求。import os; print(os.urandom(24))
    SECRET_KEY = b'A\x9fP\x12\xc6\x9c\xa0P/z\x80\xe8\xb4Tk\x94\xafa\xa6br\x96H\xa4'

    FLASK_ENV = 'development'

    # 是否开启调试模式
    DEBUG = False

    # 开启测试模式
    TESTING = False

    HOST = '127.0.0.1'

    PORT = 5000

    THREADED = True

    # 如果设置成 True，SQLAlchemy 将会记录所有 发到标准输出(stderr)的语句
    SQLALCHEMY_ECHO = False

    #from .mysql import SQLALCHEMY_DATABASE_URI

    # SQLAlchemy配置
    #SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI
    # 多库
    #SQLALCHEMY_BINDS = MYSQL_BINDS
    # 数据库连接池的大小。默认是数据库引擎的默认值 （通常是 5）。
    SQLALCHEMY_POOL_SIZE = 5
    # 指定数据库连接池的超时时间。默认是 10
    SQLALCHEMY_POOL_TIMEOUT = 10
    # 如果设置成 True (默认情况)，Flask-SQLAlchemy 将会追踪对象的修改并且发送信号。这需要额外的内存， 如果不必要的可以禁用它。
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # logging
    LOG_LEVEL = 'DEBUG'
    LOG_FILE = os.path.join(PATH_LOG, '%s_'+HelperDate.date_today() + '.log')
    LOG_FORMAT = os.linesep.join(
        (
            '%(asctime)s-【%(levelname)s】:[%(filename)s-%(module)s]=>[%(funcName)s:%(lineno)d]',
            '%(pathname)s',
            '    %(message)s',
            '-' * 80
         )
    )


