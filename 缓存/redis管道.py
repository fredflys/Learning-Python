# 事务 原子性操作（如银行转账）
# redis中通过管道实现
import redis

pool = redis.ConnectionPool(host='192.168.17.122', port=6379)
r = redis.Redis(connection_pool=pool)

# pipe = r.pipeline(transaction=False)
pipe = r.pipeline(transaction=True)

# 虽有set，但不会立即执行，而是写到内存中
r.set('name', 'yeff')
r.set('age', '24')

# 直到execute，才会真正写入redis，且必须所有操作都成功，否则就回滚
# 是所谓原子性操作
pipe.execute()