#!/usr/bin/env python
# -*- coding:utf-8 -*-
import config
from hashlib import sha1
import os
import time
import memcache
import json


create_session_id = lambda: sha1(bytes('%s%s' % (os.urandom(16), time.time()), encoding='utf-8')).hexdigest()


class SessionFactory:

    @staticmethod
    def get_session_obj(handler):
        obj = None

        if config.SESSION_TYPE == "cache":
            obj = CacheSession(handler)
        elif config.SESSION_TYPE == "memcached":
            obj = MemcachedSession(handler)
        elif config.SESSION_TYPE == "redis":
            obj = RedisSession(handler)
        return obj


class CacheSession:
    session_container = {}
    session_id = "__sessionId__"

    def __init__(self, handler):
        self.handler = handler
        client_random_str = handler.get_cookie(CacheSession.session_id, None)
        if client_random_str and client_random_str in CacheSession.session_container:
            self.random_str = client_random_str
        else:
            self.random_str = create_session_id()
            CacheSession.session_container[self.random_str] = {}

        expires_time = time.time() + config.SESSION_EXPIRES
        handler.set_cookie(CacheSession.session_id, self.random_str, expires=expires_time)

    def __getitem__(self, key):
        ret = CacheSession.session_container[self.random_str].get(key, None)
        return ret

    def __setitem__(self, key, value):
        CacheSession.session_container[self.random_str][key] = value

    def __delitem__(self, key):
        if key in CacheSession.session_container[self.random_str]:
            del CacheSession.session_container[self.random_str][key]


class RedisSession:
    session_id = "__sessionId__"
    import redis
    import json
    pool = redis.ConnectionPool(host='192.168.17.122', port=6379)
    r = redis.Redis(connection_pool=pool)

    def __init__(self, handler):
        self.handler = handler
        client_random_str = handler.get_cookie(RedisSession.session_id, None)
        if client_random_str and RedisSession.r.exists(client_random_str):
            self.random_str = client_random_str
        else:
            self.random_str = create_session_id()
            RedisSession.r.hset(self.random_str, None, None)
        RedisSession.r.expire(self.random_str, config.SESSION_EXPIRES)

        expires_time = time.time() + config.SESSION_EXPIRES
        handler.set_cookie(RedisSession.session_id, self.random_str, expires=expires_time)

    def __getitem__(self, key):
        bytes_ret = RedisSession.r.hget(self.random_str, key)
        if bytes_ret:
            try:
                return json.loads(str(bytes_ret, encoding='utf-8'))
            except json.decoder.JSONDecodeError:
                return str(bytes_ret, encoding='utf-8')
        else:
            return None

    def __setitem__(self, key, value):
        # 直接以字典形式的值使用hset方法时，会自动转换成字符串写入
        # 但变成字符串时会把字典内部的字符串加上单引号，形如"{'k1':'v1'}"
        # 这样使用loads()时就会报错，字符串内部必须是双引号才可以不会出错
        # 因此需要使用dumps()，显式地让json预处理为字符串再出传入
        if isinstance(value, dict):
            print('1234', type(value))
            RedisSession.r.hset(self.random_str, key, json.dumps(value))
        else:
            RedisSession.r.hset(self.random_str, key, value)

    def __delitem__(self, key):
        RedisSession.r.hdel(self.random_str, key)


class MemcachedSession:
    session_id = create_session_id()
    mc = memcache.Client(['192.168.17.122:12301'], debug=True, cache_cas=True)

    def __init__(self, handler):
        self.handler = handler
        client_random_str = handler.get_cookie(MemcachedSession.session_id, None)
        # 客户端和服务端都存在
        if client_random_str and client_random_str in MemcachedSession.mc.get(client_random_str):
            self.random_str = client_random_str
        else:
            self.random_str = create_session_id()
            # memcache只支持字符串一种类型，因此需要将字典转换为json字符串
            MemcachedSession.mc.set(self.random_str, json.dumps({}), config.SESSION_EXPIRES)

        # 每一次有新的请求都更新过期时间
        MemcachedSession.mc.set(self.random_str, MemcachedSession.mc.get(self.random_str), config.SESSION_EXPIRES)

        expires_time = time.time() + config.SESSION_EXPIRES
        handler.set_cookie(MemcachedSession.session_id, self.random_str, expires=expires_time)

    def __getitem__(self, key):
        ret_dict = json.loads(MemcachedSession.mc.get(self.random_str))
        return ret_dict.get(key, None)

    def __setitem__(self, key, value):
        ret_dict = json.loads(MemcachedSession.mc.get(self.random_str))
        ret_dict[key] = value
        MemcachedSession.mc.set(self.random_str, json.dumps(ret_dict), config.SESSION_EXPIRES)

    def __delitem__(self, key):
        ret_dict = json.loads(MemcachedSession.mc.get(self.random_str))
        del ret_dict[key]
        MemcachedSession.mc.set(self.random_str, json.dumps(ret_dict), config.SESSION_EXPIRES)


