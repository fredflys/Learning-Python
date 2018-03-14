import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'
))
channel = connection.channel()

channel.exchange_declare(
    exchange='direct_logs',
    exchange_type='direct'
)
result = channel.queue_declare(exclusive=True)
queue_name = result.method_queue

severities = ['info', 'warning', 'error']

for severity in severities:
    channel.queue_bind(
        exchange='direct_logs',
        queue=queue_name,
        routing_key=severity
    )
print('[*] Waiting for logs.')


def callback(channel, method, properties, body):
        print('[x] %r:%r' % (method.routing_key, body))


channel.basic_consume(
    callback,
    queue=queue_name,
    no_ack=True
)

channel.start_consuming()
connection.close()

