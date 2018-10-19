# -*- coding: utf-8 -*-
'''
实例化 instantiation
redis
'''

from config import redis

from library.lib_redis import LibRedis

# master
obj_redis = LibRedis(host=redis.master_redis.get('host'),
                     port=redis.master_redis.get('port'),
                     prefix=redis.master_redis.get('prefix'))
