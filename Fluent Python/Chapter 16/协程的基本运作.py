from inspect import getgeneratorstate


# 以生成器函数定义协程
def simple_routine():
    print('-> coroutine started')
    x = yield
    print('-> coroutine received: ', x)


my_coro = simple_routine()

# prime the coroutine
next(my_coro)  # my_coro.send(None)

# yield is a control flow device
# control flows off the end of coroutine body
# send方法的参数会变为yield表达式的值
try:
    my_coro.send(42)
except StopIteration:
    print('Error: end of iteration')


print('----------------------')


def simple_routine2(a):
    print('-> Started: a = ', a)
    b = yield a
    print('-> Received b = ', b)
    c = yield a + b
    print('-> Received:c = ', c)


my_coro2 = simple_routine2(14)
print(getgeneratorstate(my_coro2))  # GEN_CREATED

next(my_coro2)
print(getgeneratorstate(my_coro2))  # GEN_SUSPENDED

my_coro2.send(28)
try:
    my_coro2.send(99)
except StopIteration:
    print(getgeneratorstate(my_coro2))