registry = []


def register(func):
    print('running register(%s)' % func)
    registry.append(func)
    return func


@register
def f1():
    print('running f1()')


@register
def f2():
    print('running f2()')


@register
def f3():
    print('running f3()')


# 程序运行后，装饰器在定义时就会被执行，因此会看到register执行了3遍，其次才是main()函数
def main():
    print('running main()')
    print('registry ->', registry)
    f1()
    f2()
    f3()

main()