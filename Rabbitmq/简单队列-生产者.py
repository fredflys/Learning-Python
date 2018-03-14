import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'
))
channel = connection.channel()

# durable参数与下面的delivery_mode搭配使用
channel.queue_declare(queue='Games', durable=False)  # 将消息保存到磁盘中，就算rabbitmq崩溃，消息也得以保存


channel.basic_publish(
    exchange='',
    # 这里指的是队列名称
    routing_key='Games',
    # 这里是消息内容
    body='Mario',

)

print('[x] Sent "Mario."')
connection.close()