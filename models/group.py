# coding=utf-8
"""
group table
"""
from . import ModelBase
from sqlalchemy import *


class Group(ModelBase):
    """docstring for Group"""

    def __init__(self, arg):
        super(Group, self).__init__()
        self.arg = arg

    __tablename__ = 'group'
    __bind_key__ = 'flask_friend'
    # table_args__ = {'mysql_engine': 'InnoDB'}

    gid = Column(Integer, primary_key=True, comment='群ID')
    gname = Column(String(20), comment='群名称', nullable=False)
    gicon = Column(String(150), comment='群头像', nullable=False)
    garea = Column(String(100), comment='群地区', nullable=False)
    gtag = Column(String(150), comment='群标签', nullable=False)
    gintro = Column(String(200), comment='群简介', nullable=False)
    gowner = Column(Integer, comment='创建者', nullable=False)
    gadmin = Column(String(100), comment='管理员', nullable=False)
    gmember = Column(Text, comment='群成员', nullable=False)
    create_time = Column(DateTime, comment='创建时间', nullable=False)
