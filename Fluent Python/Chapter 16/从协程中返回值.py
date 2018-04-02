from collections import namedtuple

Result = namedtuple('Result', 'count average')


def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield  # 注意这里也没有了average，每次执行都不会停在average
        if term is None:
            break  # 为了返回一个值，协程必须正常中止，因此这里添加了判断，以便跳出wihle循环
        total += term
        count += 1
        average = total/count
    return Result(count, average)  # 在python3.3之前，在生成器函数中返回值是不允许的


coro_avg = averager()
next(coro_avg)

coro_avg.send(10)
coro_avg.send(30)
coro_avg.send(80)
try:
    coro_avg.send(None)
except StopIteration as exc:  # 异常的value属性里储存了Result的值，也是为什么有yield from语法
    result = exc.value

print(result)
