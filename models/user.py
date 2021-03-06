# coding=utf-8
'''
用户库
'''
from . import ModelBase
from sqlalchemy import Column, Integer, SmallInteger, String, DateTime, text


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
    # >>> from models.user import User
    # >>> User
    # <class 'models.user.User'>
    # >>> User()
    # <User(name='None', name='None', password='None')>
    # >>>
    # >>> print(User())
    我是一个字符串
    """
    __tablename__ = 'users'
    comment = '用户表'
    __bind_key__ = 'flask_user'
    string_table_name = 'type_a_strings'
    id = Column(Integer, comment='用户ID自增', primary_key=True)
    name = Column(String(10), comment='用户名', nullable=False)
    icon = Column(String(150), comment='头像', nullable=False)
    gender = Column(Integer, comment='性别', nullable=False, server_default=text("2"))
    phone = Column(String(15), comment='手机号', nullable=False, server_default=text("0"))
    address = Column(String(250), comment='地址', nullable=False, server_default=text("0"))
    create_time = Column(DateTime, comment='注册时间', nullable=False)
    login_time = Column(DateTime, comment='最后登陆时间', nullable=False)

    def __repr__(self):
        """
        __repr__: 返回一个可以用来表示对象的可打印字符串
        """
        return "User __repr__"

    def __str__(self):
        """
        __str__使用：被打印的时候需要以字符串的形式输出的时候，就会找到这个方法，并将返回值打印出来
        """
        return "我是一个字符串 __str__"
