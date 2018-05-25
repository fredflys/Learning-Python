"""
A methodology by which functions enforce an abstraction
barrier between representation and use

e.g.
numerator
_________
denominator

Constructor: rational(n, d) returns a rational number x
Selectors: numer(x) returns the numerator of x
           denom(x) returns the denominator of x
"""
from fractions import gcd


def mul_rational(x, y):
    return rational(numer(x) * numer(x),
                    denom(x) * denom(x))


def add_rational(x, y):
    nx, ny = numer(x), numer(y)
    dx, dy = denom(x), denom(y)
    return rational(nx * dy + ny * dx, dx * dy)


def equal_rational(x, y):
    return numer(x) * denom(y) == denom(x) * numer(y)


def print_rational(x):
    print(numer(x), '/', denom(x))

# Constructor and Selectors
"""
无需改变操作的函数（use），只需重构构造器（representation）
就可以改变所有功能（选择器）的结果
选择器只需要知道当做特定操作时，该返回什么，而无需关心如何返回

"""
# 初次定义
# def rational(n, d):
#     return [n, d]


# 以列表表示分数
def rational(n, d):
    g = gcd(n, d)
    return [n//g, d//g]


def numer(x):
    return x[0]


def denom(x):
    return x[1]


# 以函数表示分数
# Constructor
def rational(n, d):
    def select(name):
        if name == 'n':
            return n
        elif name == 'd':
            return d
    return select


# Selector
def numer(x):
    return x('n')


# Selector
def denom(x):
    return x('d')

