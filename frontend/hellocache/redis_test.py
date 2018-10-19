# -*- coding: utf-8 -*-
'''
缓存测试模块
redis 测试
'''
from flask import request
from loadclass.redis import obj_redis
from helper.helper_ret import HelperRet


def redis_test(request):
	'''
	测试下redis的操作
	postdata={
				"public":{"version":"208","packid":"100"},
				"request":{"method":"hellocache#redis_test","uid":"66","field":"nickname"},
				"extend":{"net":"wifi","device":"iphone  10  plus","macid":"aaaaaaaaaaaa"},
				"sig":"4ef43e75ad799f7775ed366d8c3fc8b8", 
				"debug":1
				}	
	'''
	ret = dict()
	ret['host'] = request.host
	ret['host_url'] = request.host_url

	key_string = 'x_string'
	obj_redis.set(key_string, 123)

	# string
	ret.update(redis_get=dict(key=key_string, 
							  get_value=obj_redis.get(key_string)))

	# hash
	key_hash = 'x_hash'
	for k in range(1, 5):
		obj_redis.hSet(key_hash, 'k_%s' % k, 1)

	ret.update(redis_hash=dict(key=key_hash, hash_value=list(obj_redis.hGetAll(key_hash))))

	# list
	key_list = 'x_list'
	for i in range(1,5):
		obj_redis.rPush(key_list, i)

	ret.update(redis_list=dict(key=key_list, list_value=list(obj_redis.lGetRange(key_list))))

	# set
	key_set = 'x_set'
	for i in range(1, 5):
		obj_redis.sAdd(key_set, i)

	ret.update(redis_set=dict(key=key_set, set_value=list(obj_redis.sMembers(key_set))))

	#zset
	key_zset = 'x_zset' 
	import random
	obj_redis.zAdd(key_zset, a=random.randint(0, 9))
	obj_redis.zAdd(key_zset, b=random.randint(0, 9))
	obj_redis.zAdd(key_zset, c=random.randint(0, 9))

	ret.update(redis_zset=dict(key=key_zset, zset_value=list(obj_redis.zRange(key_zset, 0, -1))))

	return HelperRet.ret_json(ret)
