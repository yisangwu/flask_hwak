# coding=utf-8
'''
Mysql 实例化
'''
from sqlalchemy.orm import sessionmaker
from helper.helper_class import ObjSingleton


class LoadMysql(ObjSingleton):
    """docstring for LoadMysqli"""
    session_user = None

    def db_user():
        from config.mysql import flask_user_engine
            Session = sessionmaker(bind=flask_user_engine)
            return Session_User()
