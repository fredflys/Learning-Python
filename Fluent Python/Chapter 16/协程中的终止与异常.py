from inspect import getgeneratorstate as ggs


class DemoException(Exception):
    """An exception type for the demonstration."""


def demo_exc_handling():
    print('-> coroutine started...')

    while True:
        try:
            x = yield
        except DemoException:
            print('*** DemoException handled. Continuing...')
        else:
            print('-> coroutine received: {!r}'.format(x))  # !r对应repr()
    raise RuntimeError('This line should never run.')


exc_coro = demo_exc_handling()
next(exc_coro)
exc_coro.send(10)
exc_coro.send(11)
exc_coro.close()
print(ggs(exc_coro))  # CLOSED

print('----------')

exc_coro = demo_exc_handling()
next(exc_coro)
exc_coro.send(20)
print(exc_coro.throw(DemoException))
print(ggs(exc_coro))  # SUSPENDED
exc_coro.send(21)

try:
    exc_coro.throw(ZeroDivisionError)
except ZeroDivisionError:
    print(ggs(exc_coro))  # CLOSED


def demo_finally():
    try:
        print('-> coroutine started...')
        while True:
            try:
                x = yield
            except DemoException:
                print('*** DemoException handled. Continuing...')
            else:
                print('-> coroutine received: {!r}'.format(x))  # !r对应repr()
    finally:
        print('-> coroutine ending.[cleanup code can be placed here]')