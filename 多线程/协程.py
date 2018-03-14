# 用生成器的yield方法的部分实现
import time
# 传统的生产者-消费者模型是一个线程写消息，一个线程取消息，
# 通过锁机制控制队列和等待，但一不小心就可能死锁。
# 如果改用协程，生产者生产消息后，直接通过yield跳转到消费者开始执行
# 待消费者执行完毕后，切换回生产者继续生产，效率极高


# consumer函数中有yield表达式， 是一个生成器
# consumer()将返回一个generator object，处于just-started状态
def consumer():
    # 用于初始化生成器
    # 第一次执行next()饭后后，yield表达式返回'',赋值给n，并执行到return语句
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        time.sleep(1)
        r = '200 OK'


def produce(gen):
    # next()方法使生成器运转起来
    next(gen)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        # send()方法将n作为yield表达式的值，并赋值给consumer作用域中的n
        # 继续向下执行，打印consuming语句，r = '200 OK'
        # 再次执行到yield表达式，并抛出r的值，在yield处暂停，此时yield表达式的值为None
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    # generator还实现了throw()和close()方法
    # 分别用于抛出异常和关闭生成器
    c.close()


if __name__ == '__main__':
    c = consumer()
    produce(c)