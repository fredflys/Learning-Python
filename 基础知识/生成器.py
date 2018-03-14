# 普通的斐波那契数列，返回到第n个数的完整数列，也可以返回第n个斐波那契数
import random
import time

def  fib(num):
    first = 0
    second = 1
    index = 0
    fib_list = [0,1]
    while index < num-1:
        fib_list.append(second)
        first,second= second,first+second
        index += 1
    return fib_list,fib_list[-1]

#一个生成器版本的斐波那契数计算
def gen_fib(num):
    first = 0
    second = 1
    index = 0
    while index < num-1:
        yield second
        first,second = second, first + second
        index += 1
#生成一个生成器对象
g = gen_fib(10)
#print(g.__next__())


def sti_fib(num):
    first = 0
    second = 1
    index = 0
    while index < num - 1:
        sleep_count = yield second
        print('Let me think {0} second.'.format(sleep_count))
        time.sleep(sleep_count)
        first,second = second, first + second
        index += 1

gg = sti_fib(20)
result = next(gg)

while True:
    print(result)
    try:
        ret = gg.send(random.uniform(0, 0.5))
    except StopIteration:
        break


