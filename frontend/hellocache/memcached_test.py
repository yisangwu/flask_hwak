# -*- coding: utf-8 -*-
'''
缓存测试模块
memcached 测试
'''
from flask import request
from loadclass.memcached import obj_memcached
from helper.helper_ret import HelperRet


def memcached_test(request):
	'''
	测试下memcached的操作
	postdata={
				"public":{"version":"208","packid":"100"},
				"request":{"method":"hellocache#memcached_test","uid":"66","field":"nickname"},
				"extend":{"net":"wifi","device":"iphone  10  plus","macid":"aaaaaaaaaaaa"},
				"sig":"4ef43e75ad799f7775ed366d8c3fc8b8", 
				"debug":1
				}
	'''
	ret = dict()
	ret['host'] = request.host
	ret['host_url'] = request.host_url

	key = 'x_mem'

	obj_memcached.set(key, '12345')

	ret.update(str_get=dict(
			key=key,
			get_value=obj_memcached.get(key))
		)

	obj_memcached.append(key, 'append')

	ret.update(str_append=dict(
			key=key,
			get_value=obj_memcached.get(key))  # 12345append
		)

	obj_memcached.prepend(key, 'prepend')

	ret.update(str_prepend=dict(
			key=key,
			get_value=obj_memcached.get(key))  # prepend12345append
		)

	return HelperRet.ret_json(ret)
