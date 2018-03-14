import memcache

mc = memcache.Client(['192.168.17.122:2000'], debug=True, cache_cas=True)

mc.set('k1', 10)

# 不仅会取得值，还会拿到计数器
print(mc.gets('k1'))



