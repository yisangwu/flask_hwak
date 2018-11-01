# coding=utf-8
"""
table address
"""
from sqlalchemy import *
metadata = MetaData()


addresses = Table('addresses', metadata,
                  Column('address_id', Integer, primary_key=True,
                         comment='自增ID'),
                  Column('remote_user_id', Integer,
                         comment='用户ID', server_default=text('0')),
                  Column('email_address', String(20),
                         comment='邮件地址', nullable=False),
                  Column('create_time', DateTime,
                         comment='创建时间', nullable=False),
                  mysql_engine='InnoDB',
                  mysql_charset='utf8mb4',
                  autoload_replace=True,
                  extend_existing=false
                  )
