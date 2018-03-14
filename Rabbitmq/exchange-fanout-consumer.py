import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'
))
channel = connection.channel()

channel.exchange_declare(
    exchange='logs',
    exchange_type='fanout'
)

# 订阅者不是直接从交换机取数据
# 无论何时，消费者都是从队列中取数据
# 因此，每一个订阅者都需要创建自己的队列
# 下面随机生成了一条独占队列，并获取队列名，以便与交换机绑定
result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

# 将队列与交换机绑定，这个动作就是 订阅
channel.queue_bind(
    exchange='logs',
    queue=queue_name
)

print('[*] Waiting for logs. To exit press CTRL+C.')


def callback(*args, body):
    print("[y] %r" % body)


channel.basic_consume(
    callback,
    queue=queue_name,
    no_ack=True
)

# 进程将阻塞，等待生产者将消息放入交换机中
# 监听到有消息后，会执行上面的basic_consume方法
channel.start_consuming()
