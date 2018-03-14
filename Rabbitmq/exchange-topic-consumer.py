import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'
))
channel = connection.channel()

channel.exchange_declare(
    exchange='topic_logs',
    exchange_type='topic'
)

result = channel.queue_declare(exclusive=True)
queue_name = result.method_queue

identity = 'vip.yifei'
channel.queue_bind(
    exchange='topic_logs',
    queue=queue_name,
    routing_key=identity
)
print('[vip.yifei] Waiting for logs.')


def callback(channel, method, properties, body):
    print('[x] %r:%r' % (method.routing_key, body))


channel.basic_consume(
    callback,
    queue=queue_name,
    no_ack=True
)

channel.start_consuming()
connection.close()



