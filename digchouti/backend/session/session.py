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
    def __init__(self, handler):
        pass


class MemcachedSession:
    session_id = "__sessionId__"
    mc = memcache.Client(['192.168.17.122:2000'], debug=True, cache_cas=True)

    def __init__(self, handler):
        import memcache
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


