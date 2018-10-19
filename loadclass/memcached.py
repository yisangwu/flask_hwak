# -*- coding: utf-8 -*-
'''
实例化 instantiation
memcached
'''
from config import memcached

from library.lib_memcached import LibMemcached

# master
obj_memcached = LibMemcached(host=memcached.master_memcache.get('host'),
                             port=memcached.master_memcache.get('port'),
                             prefix=memcached.master_memcache.get('prefix'))
