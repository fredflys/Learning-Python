# 函数也是对象
def greeter(a,b,c):
    print('Hello', a)
    print('How are you', b)
    print('Bye', c)


def repeat(fn, times):
    for i in range(times):
        fn()
# 函数可以在其它函数内部声明，即函数可以嵌套函数，用来隐藏实用函数的实现细节


def print_integers(values):
    def is_integer(value):
        try:
            return value == int(value)
        except
            return False
    for v in values:
        if is_integer(v):
            print (v)
# 函数可以被包装在其它函数中，向已构建好的函数增加新的行为,即函数参数化
def print_call(fn):
    def wrapper(*args, **kwargs):
        print('Calling %s' % fn.__name__)
        return fn(*args,**kwargs)
    # wrapper.__name__ = fn.__name__ #如此可使原函数名不改变
    return wrapper
greeter = print_call(greeter)
greeter(1, 2, 3)
print(greeter.__name__) #函数名字已经改变

# 一个完整的装饰函数的函数演示(其实和上面的函数是一样的
def another_print_call(fn):
    def wrapper(*args, **kwargs):
        print('Calling %s with argument: \n\targs: %s\n\tkwargs:%s' % (fn.__name__,args,kwargs))
        result = fn(*args, **kwargs)
        print('%s returning %s' % (fn.__name__, result))
        return result # 这里取得原函数的返回值
    wrapper.__name__ = fn.__name__
    return wrapper

'''
闭包
'''
#函数可以取得a的值，并且可以读取更新后的值
#函数从它的#闭合范围#内捕获变量，但不能写入，因为会优先写入本地变量
a = 0
def get_a():
    print(a)
    return a
get_a()
a = 3
get_a()
#被捕获的变量不能被写入
def set_a(value):
    #该语句其实是写入了本地变量a,从而隐藏了模块级别的a
    a = value
    print(a)
set_a(4)
get_a()
#可以通过一个中间容器越过这个限制（加一层抽象）
class B(object):
    def __init__(self):
        self.value = None
b = B()
b.value = 0
def get_b():
    print (b.value)
    return b.value
def set_b(value):
    b.value = value
    print(b.value)
    return b.value
get_b()
set_b(5)

'''
偏函数
把一个函数的某些参数固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单
'''
def get_stuff(user,pw,stuff_id):
    print('get_stuff called with user: %s, pw: %s, stuff_id: %s' % (user,pw,stuff_id))
def partial(fn, *args, **kwargs):
    def fn_part(*fn_args, **fn_kwargs):
        kwargs.update(fn_kwargs)
        return fn(*args + fn_args, **kwargs)
    return fn_part
my_stuff = partial(get_stuff, 'myuser','mypwd')
my_stuff(5)

#一个更简单的例子
