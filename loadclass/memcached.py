# -*- coding: utf-8 -*-
'''
实例化 instantiation
memcached
'''
from config import memcached

from library.lib_memcached import LibMemcached
from helper.helper_singleton import HelperSingleton


class LoadMemcached(HelperSingleton):

    def obj_memcached():
        '''
        master memcached
        '''
        return LibMemcached(host=memcached.master_memcache.get('host'),
                             port=memcached.master_memcache.get('port'),
                             prefix=memcached.master_memcache.get('prefix'))
