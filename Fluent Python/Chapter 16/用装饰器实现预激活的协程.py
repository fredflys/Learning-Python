from functools import wraps
from inspect import getgeneratorstate as ggs


def coroutine(func):
    """Decorator: primes 'func' by advancing to first 'yield"""
    @wraps(func)
    def primer(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)  # prime the generator
        return gen  # return it
    return primer


@coroutine
def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield average
        total += term
        count += 1
        average = total/count


coro_avg = averager()
print(ggs(coro_avg))  # 一经创建就已经是可用状态了，不需要首先使用next()
