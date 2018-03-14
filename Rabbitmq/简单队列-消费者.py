import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'
))

channel = connection.channel()

channel.queue_declare(queue='Games')

# 并发时消费者获取消息的顺序就不再按照默认方式进行，而是谁需要就给谁
# 该设置放在消费者中
channel.basic_qos(prefetch_count=1)


# 回掉函数
def callback(ch, method, properties, body):
    print('[y] Received %r' % body)
    import time
    time.sleep(3)
    print('ok')
    ch.basic_ack(delivery_tag=method.delivery_tag)


# 有应答，牺牲一部分效率换取更强的安全性
channel.basic_consume(
    callback,
    queue='Games',
    no_ack=False
)

print(' [*] Waiting for messages. To exit press CTRL+C.')
channel.start_consuming()