import pika

# 关键字发送 direct
# 发送者根据关键字将消息发送给交换机
# 交换机再根据关键字判定将消息发送给谁

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'
))
channel = connection.channel()

channel.exchange_declare(
    exchange='direct_logs',
    exchange_type='direct'
)
severity = 'info'
message = 'This is exchange direct message.'

channel.basic_publish(
    exchange='direct_logs',
    routing_key=severity,
    body=message
)
print('[x] Sent %r:%r' % (severity, message))
connection.close()