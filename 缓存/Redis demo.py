# redis存储的value支持类型更多，包括string, list, set, zset, hash
# 且支持的操作更为丰富，如push/pop, add/remove及集合操作
# 支持持久化

import redis

# 建立连接池，从池中取连接
pool = redis.ConnectionPool(host='192.168.17.122', port=6379)
r = redis.Redis(connection_pool=pool)

# 过期秒数，过期毫秒数，不存在时才进行操作（添加）， 只有存在时才进行操作（修改）
r.set('foo', 'bar', ex=None, px=None, nx=False, xx=False)
r.mset({})
r.mset(k1='v1',)
r.get()
r.mget([])
# 获取旧值，并设置新值
r.getset('foo', 'bar')
r.getrange(key=, start=, end=)
r.setrange()
r.setbit()
# operation destination *names
r.bitop('AND', 'n4', 'n1','n2','n3')
r.strlen()
r.incr()
r.incrbyfloat()
r.append()
print(r.get('foo'))