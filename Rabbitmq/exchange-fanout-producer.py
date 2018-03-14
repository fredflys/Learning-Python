import pika
# 发布订阅和简单消息的区别在于发布的消息所有用户都将收到
# 但队列的消息消费一次便会消失
# 因此在发布者和队列间再加一层抽象，叫做exchange
# 发布者将消息放入交换机中，订阅发生时，会为每一个订阅者创建一个队列
# 将消息放入每一个队列中，保证一个消息可以被所用订阅者接收到

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'
))

channel = connection.channel()

# 创建交换机，名为logs，模式为fanout(订阅)
channel.exchange_declare(
    exchange='logs',
    exchange_type='fanout',
)

message = 'Mario'

# 信息放入交换机中，因此不用指定队列名
# 生产者只需将信息放入交换机中，不需要再创建队列，其它事情也不须操心
# 但消费者取消息时，必须建立队列
channel.basic_publish(
    exchange='logs',
    routing_key='',
    body=message
)

print('[x] Sent %r' % message)
connection.close()