# coding=utf-8
from sqlalchemy.ext.declarative import declarative_base
from config.mysql import flask_user_engine

# 创建对象的基类
ModelBase = declarative_base()

from . import user


def init_mysql():
    '''
    创建表， 但是不能修改表
    >>> from models import init_mysql
    >>> init_mysql()
    '''
    User.metadata.create_all(flask_user_engine)
