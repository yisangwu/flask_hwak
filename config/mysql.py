# coding=utf-8
"""
mysql 配置

使用pymysql数据库连接组件
SQLAlchemy是一个很强大的关系型数据库框架，支持多种数据库后台。其不但提供了高层ORM，而且也提供了使用数据库原生SQL的底层功能。
pip install pymysql
pip install flask-sqlalchemy
"""
from sqlalchemy import create_engine


DB_HOST = '192.168.101.215'
DB_PORT = 3306
DB_USERNAME = 'mysql'
DB_PASSWORD = 123456
DB_CHARSET = 'utf8mb4'

# 多库
DB_DATABASES = ['flask_user', 'flask_friend']

# mysql 资源连接符
DB_URI = 'mysql+pymysql://%s:%s@%s:%s/{database}?charset=%s' % (
    DB_USERNAME, DB_PASSWORD, DB_HOST, DB_PORT, DB_CHARSET)


def mysql_create_engine(dbname=None):
    """
    创建engine
    :param dbname:
    :return:
    """
    if not dbname:
        return None
    dbname = dbname.strip()
    if dbname not in DB_DATABASES:
        return None

    # echo= True 会打印操作数据库的信息
    return create_engine(DB_URI.format(database=dbname), echo=True)


# echo= True 会打印操作数据库的信息
# flask_user_engine = create_engine(
#     DB_URI.format(database='flask_user'), echo=True)

# flask_friend_engine = create_engine(
#     DB_URI.format(database='flask_friend'), echo=True)


'''
mysql 连接资源符
SQLAlchemy 把一个引擎的源表示为一个连同设定引擎选项的可选字符串参数的 URI。URI 的形式是:
dialect+driver://username:password@host:port/database
SQLAlchemy无法修改表结构，如果需要可以使用SQLAlchemy开发者开源的另外一个软件Alembic来完成

MYSQL_DB_URI = 'mysql+pymysql://%s:%s@%s' % (
    DB_USERNAME, DB_PASSWORD, DB_HOST)

# SQLAlchemy配置
# 单库
SQLALCHEMY_DATABASE_URI = '%s/flask_user' % MYSQL_DB_URI

# 多库
# SQLALCHEMY_BINDS = {
#     'flask_user': '%s/flask_user' % MYSQL_DB_URI,
#     'flask_friend': '%s/flask_friend' % MYSQL_DB_URI,
# }
'''
