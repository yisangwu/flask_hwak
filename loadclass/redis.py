# -*- coding: utf-8 -*-
'''
实例化 instantiation
redis
'''

from config import redis
from library.lib_redis import LibRedis
from helper.helper_singleton import HelperSingleton


class LoadRedis(HelperSingleton):

    @staticmethod
    def obj_redis():
        '''
        master redis
        '''
        return LibRedis(host=redis.master_redis.get('host'),
                     port=redis.master_redis.get('port'),
                     prefix=redis.master_redis.get('prefix'))