import memcache
import json

mc = memcache.Client(['192.168.17.122:12301'], debug=True, cache_cas=True)
# mc = memcache.Client(['127.0.0.1:2000'], debug=True, cache_cas=True)


mc.set('k1', json.dumps({'a': '1'}))
print(json.loads(mc.get('k1')))

# 不仅会取得值，还会拿到计数器
# print(mc.gets('k1'))



