def xrange():
    print('a')
    yield 1

    print('b')
    yield 2

    print('c')
    yield 3

    print('d')
    yield 4


x = xrange()
# 执行函数，寻找下一个yield
r1 = x.__next__()
r2 = x.__next__()
r3 = x.__next__()
r4 = x.__next__()
# yield已全部执行完，再次调用__next__方法，则会报错
# r_error = x.__next__()
print(r1,r2,r3,r4)


# 直接调用生成器，则会不断生成新的生成器，只会执行第一个yield
rr1 = xrange().__next__()
rr2 = xrange().__next__()   #rri和rr2的值相同


# 一个最大值为n的自然数生成器
def numerator(n):
    start = 0
    while True:
        if start > n:
            return
        yield start
        start += 1


# 生成器仅仅是具有一种生成能力。
# 还需要一种能力，叫做访问能力，这就是迭代器
n = numerator(10)
n0 = n.__next__() #0
n1 = n.__next__() #1
# 可用for循环进行迭代访问

# 例子
a = iter([1, 2, 3, 4])
a.__next__()
print('------------------------------------')

'''实现一个迭代器类'''

