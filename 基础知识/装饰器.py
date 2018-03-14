def say_english():
    print('Hello')


def say_chinese():
    print('你好')


# python中一切皆对象
# 将函数作为参数传入另外一个函数
def greet(say):
    say()
