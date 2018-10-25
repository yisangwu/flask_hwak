# coding=utf-8
'''
mysql 配置

使用pymysql数据库连接组件
SQLAlchemy是一个很强大的关系型数据库框架，支持多种数据库后台。其不但提供了高层ORM，而且也提供了使用数据库原生SQL的底层功能。
pip install pymysql
pip install flask-sqlalchemy
'''


DB_HOST = '192.168.101.215'
DB_USERNAME = 'mysql'
DB_PASSWORD = 123456


# mysql 连接资源符
# SQLAlchemy 把一个引擎的源表示为一个连同设定引擎选项的可选字符串参数的 URI。URI 的形式是:
# dialect+driver://username:password@host:port/database
DB_URI = 'mysql+pymsql://%s:%s@%s/' % (DB_USERNAME, DB_PASSWORD, DB_HOST)

# SQLAlchemy配置
# 单库
# app.config['SQLALCHEMY_DATABASE_URI']= 'flask_user': '%s/flask_user' % DB_URI
# 多库
mysql['SQLALCHEMY_BINDS'] = {
    'flask_user': '%s/flask_user' % DB_URI,
    'flask_friend': '%s/flask_friend' % DB_URI,
}
# 数据库连接池的大小。默认是数据库引擎的默认值 （通常是 5）。
mysql['SQLALCHEMY_POOL_SIZE'] = 5
# 指定数据库连接池的超时时间。默认是 10
mysql['SQLALCHEMY_POOL_TIMEOUT'] = 10

db = SQLAlchemy(db_app)
