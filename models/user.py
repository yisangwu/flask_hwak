# coding=utf-8
'''
用户库
'''
from . import ModelBase
from sqlalchemy import Column, Integer, SmallInteger, String, DateTime


# class UserInfo(ModelBase):
#     _mapper = {}
#     tpl_table_name = 'userinfo%d'

#     @staticmethod
#     def model(user_id):
#         table_index = user_id % 10
#         class_name = 'UserInfo%d' % table_index

#         ModelClass = UserInfo._mapper.get(class_name, None)
#         if ModelClass is None:
#             ModelClass = type(class_name, (Model,),
#                               {
#                 '__module__': __name__,
#                 '__name__': class_name,
#                 '__tablename__': tpl_table_name % table_index,
#                 '__bind_key__': 'flask_user',
#                 'id': Column(Integer, primary_key=True),
#                 'nick': Column(String(20), nullable=False),
#                 'gender': Column(SmallInteger, default=2, nullable=False),
#                 'create_time': Column(DateTime, nullable=False),
#                 'login_time': Column(DateTime, nullable=False)
#             }
#             )

#             UserInfo._mapper[class_name] = ModelClass
#             cls = ModelClass()
#             cls.user_id = user_id

#         return cls


class User(ModelBase):
	"""
	>>> from models.user import User
	>>> User
	<class 'models.user.User'>
	>>> User()
	<User(name='None', name='None', password='None')>
	>>>
	>>> print(User())
	我是一个字符串
	"""

    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(10))
    password = Column(String(32), nullable=False)
    create_time = Column(DateTime, nullable=False)

    def __repr__(self):
        """
        __repr__: 返回一个可以用来表示对象的可打印字符串

        """
        return "<User(name='%s', name='%s', password='%s')>" % (self.name, self.name, self.password)

    def __str__(self):
        """
        __str__使用：被打印的时候需要以字符串的形式输出的时候，就会找到这个方法，并将返回值打印出来
        """
        return "我是一个字符串"
