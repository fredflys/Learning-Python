# 如收到好友动态
# 发布-订阅
import redis


class RedisHelper:

    def __init__(self):
        self.__conn = redis.Redis(host='192.168.17.122')
        self.chan_sub = 'fm104.5'
        self.chan_pub = 'fm104.5'

    def publish(self, msg):
        self.__conn.publish(self.chan_pub, msg)
        return True

    def subscribe(self):
        pub = self.__conn.pubsub()
        pub.subscribe(self.chan_sub)
        pub.parse_response()
        return pub


obj = RedisHelper()
obj.publish('hello')