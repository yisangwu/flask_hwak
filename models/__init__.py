# coding=utf-8
from sqlalchemy.ext.declarative import declarative_base, declared_attr
from config.mysql import DB_DATABASES, mysql_create_engine


class ModelBase(object):

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    __table_args__ = {'mysql_engine': 'InnoDB'}

# 创建对象的基类
ModelBase = declarative_base(cls=ModelBase)

from .user import User
from .group import Group
from .address import addresses

'''
flask_hwak>alembic revision --autogenerate -m "create user"
flask_hwak>alembic upgrade head
'''
MAP_DATABASE = [User, Group]  # , address


def init_mysql():
    """
    创建表， 但是不能修改表
    用此方法创建表，可以增加字段注释
    alembic 不能动态修改字段属性, 只可以增加字段
    # >>> from models import init_mysql
    # >>> init_mysql()
    :return:
    """
    for model in MAP_DATABASE:
        mysql_engine = None
        if not model.__bind_key__ or model.__bind_key__ not in DB_DATABASES:
            bind_db = 'flask_user'
        else:
            bind_db = model.__bind_key__
        # 创建engine连接
        try:
            mysql_engine = mysql_create_engine(bind_db)
        except:
            print('mysql engine error!')
            raise
        if not mysql_engine:
            continue
        # 执行建表操作
        model.metadata.create_all(bind=mysql_engine)

    # print(flask_user_engine)
    # User.metadata.create_all(flask_user_engine)
    # print(flask_friend_engine)
    # Group.metadata.create_all(flask_friend_engine)
