"""
其实就是修饰器版的update_wrapper
update_wrapper本来也就是在返回wrapper_func之前执行的
wraps就是通过装饰器简化了这一步而已
"""

from functools import wraps


def wrapper(func):
    @wraps(func)
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