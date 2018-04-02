"""
将原函数的某些参数固定，从而构造出一个新函数
也就是在修改函数签名
"""
from functools import partial


def add(x, y):
    return x + y


partial_add = partial(add, y=2)  # 函数的y参数被固定为2
partial_add(3)   # 返回5
