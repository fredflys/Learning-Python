"""
用被修饰函数的一些属性来代替修饰函数的属性
也就是在修改函数属性
在装饰后仍能保持原来的函数属性
"""


def wrapper(func):
    def wrapper_func(*args, **kwargs):
        """这个是修饰器函数哦！"""
        return func(*args, **kwargs)
    return wrapper_func


@wrapper
def wrapped():
    """这个是被修饰的函数？"""
    print('wrapped')


print(wrapped.__doc__)  # 可以看到被修饰函数的doc属性已被替代
print(wrapped.__name__)  # 函数的name属性也被替代


from functools import update_wrapper


def new_wrapper(func):
    def wrapper_func(*args, **kwargs):
        """这个是修饰函数！"""
        return func(*args, **kwargs)
    update_wrapper(wrapper_func, func)  # 这里使用了update_wrapper函数
    return wrapper_func


@new_wrapper
def wrapped():
    """这个是被修饰的函数？"""
    print('wrapped')


print(wrapped.__doc__)  # 可以看到被修饰函数的doc属性未被修改
print(wrapped.__name__)  # 函数的name属性同样未被修改