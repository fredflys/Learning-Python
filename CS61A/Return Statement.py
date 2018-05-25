def search(f):
    x = 0
    while True:
        if f(x):
            return x
        x += 1


def is_three(x):
    return x == 3


def square(x):
    return x * x


def positive(x):
    return max(0, square(x) - 100)


def inverse(f):
    return



print(search(positive))



"""
self reference
"""


def print_all(n):
    print(n)
    return print_all


a = print_all(1)(2)(3)
print(a)


# 永远停在返回一个函数这一步，所以不会不停地执行
def print_sums(x):
    print(x)

    def next_sum(y):
        return print_sums(x + y)
    return next_sum


print_sums(2)(3)