import pika

# 其实就是在direct的基础上变成了模糊匹配
connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'
))
channel = connection.channel()

channel.exchange_declare(
    exchange='topic_logs',
    exchange_type='topic'
)
routing_key = 'vip.#'
message = 'This is a topic message.'
channel.basic_publish(
    exchange='topic_logs',
    # 这里是话题匹配的模式
    # #代表0个或多个单词
    # *代表1个单词
    routing_key=routing_key
)
print('[x] Sent %r:%r' % (routing_key, message))
connection.close()