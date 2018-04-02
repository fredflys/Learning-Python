import memcache

# 必须加上cache_cas标识
mc = memcache.Client(['192.168.17.122:12301'], debug=True, cache_cas=True)

# mc.set('k1', 10)

# 获取和设置时，必须用gets和cas方法
# 不仅会取得值，还会拿到计数器
print(mc.gets('k1'))
input('>>>')
mc.cas('k1', 30)


