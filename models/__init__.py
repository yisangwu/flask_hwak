# coding=utf-8
from sqlalchemy.ext.declarative import declarative_base
from config.mysql import flask_user_engine

ModelBase = declarative_base()


def init_mysql():
    '''
    >>> from models import init_mysql
    >>> init_mysql()
    '''
    from .user import User
    User.metadata.create_all(flask_user_engine)
