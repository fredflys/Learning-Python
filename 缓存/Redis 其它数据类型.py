import redis

# 建立连接池，从池中取连接
pool = redis.ConnectionPool(host='192.168.17.122', port=6379)
r = redis.Redis(connection_pool=pool)
# list
# set
# sort set
#
# list
r.lpush('ldata', 1, 2)
r.linsert('ldata', where='AFTER', refvalue=1, value=2)
r.lset('ldata', index=0, value=0)
r.lrem('ldata', value=3, num=-2)
r.lpop('ldata')
print(r.lindex('ldata', 2))
print(r.llen('ldata'))
print(r.lrange('ldata', start=0, end=-1))
r.ltrim('ldata', start=0, end=-2)
# r.rpoplpush()
# r.blpop()

# set
r.sadd("sd", 1, 2)
r.sadd("sd_2", 2,3)
print(r.scard("sd"))
print(r.sdiff("sd", "sd_2"))
r.sdiffstore("sd_3", "sd", "sd_2")

# sorted set
# value是要存储的值， 后面的分数是之后排序统计等操作的依据，类似成绩表
r.zadd("ssd", value1=10, value2=20)
print(r.zcard("ssd"))
print(r.zcount("ssd", 5, 15))
r.zincrby('value1', 3)
# withscores 是否值和分数都拿
# score_cast_func 拿来后会使用对应的函数，进行转换
rz = r.zrange(name="ssd", start=0, end=1, desc=True, withscores=True, score_cast_func=float)
print(rz)
# r.zrangebylex(name="ssd", min=, max=)


# 全局操作，针对name
r.delete('ldata')
r.exists('ldata')
print(r.keys(pattern='*sd'))
r.expire('sd', time=10)
# redis会在后台创建数据库（16个），自动完成存放
# 但用户也可以自己设置
r.move(name='ssd', db=2)
r.randomkey()
r.type("ssd")
