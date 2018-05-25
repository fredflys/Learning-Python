def trace(fn):
    def traced(x):
        print('Calling,', fn, 'on argument', x)
        return fn(x)
    return traced


@trace
def square(x):
    return x * x


@trace
def sum_squares_up_to(n):
    k = 1
    total = 0
    while k <= n:
        total, k = total + square(k), k + 1


sum_squares_up_to(5)
