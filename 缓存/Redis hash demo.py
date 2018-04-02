import redis

# 建立连接池，从池中取连接
pool = redis.ConnectionPool(host='192.168.17.122', port=6379)
r = redis.Redis(connection_pool=pool)

# 默认取得是bytes，并非str
print(r.hget(name='n1', key='k1'))

# r.hget(name='n1', key='k1')
# r.hlen(name='n1')
# r.hkeys(name='n1')
# r.hvals(name='n1')
# r.hexists(name='n1', key='k1')
# r.hdel('n1', 'k1', 'k2')
# r.hincrby(name='n1', key='k1', amount=2)
# r.hincrbyfloat(name='n1', key='k1', amount=1.2)

# redis服务器通常内存都很大，假如某次要取的内容大于客户机器的内存，就不能一次全部取过来了，需要分片
# 不支持迭代
# count 每次分片最少获取个数
# 两个返回值，一个是游标位置，另一个是取到的数据,下一次再执行scan就从上一次停下的位置开始
# 如果cur变为0，则表示已经取完了
# hscan会扫描name对应的哈希表
# scan则会循环全部name
# cur, data = r.hscan(name='n1', cursor=None, match='k*', count=None)
# r.scan(cursor=13, match=None)
# #
# for item in r.scan_iter():
#     print(item)


# r.hset('n1', 'k1','v1')
# r.expire('n1', 30)
