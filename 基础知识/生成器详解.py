from collections import Iterable,Iterator

a = [x for x in range(10)]
b = iter(a)  # 通过iter方法，由iterable对象得到一个iterator对象

'''
list是Iterable对象，却不是Iterator对象，因为实现了__iter__方法，但没有实现__next__方法
'''
print(isinstance(a,Iterable)) #list是Iterable对象
print(isinstance(a,Iterator))
print(dir(a))

'''
b既是iterable，也是iterator对象，因为两个方法都实现了 
'''
print(isinstance(b,Iterable))
print(isinstance(b,Iterator))
print(dir(b))

'''
iterator对象是消耗型的，用一次少一次
c是完整的列表，而d已经为空，因为赋值时会循环到每一个元素
'''
c = list(b)
d = list(b)
print(c,d)

'''
但空iterator并不等于None
'''
print(d is None)

'''
for循环的实质：
对一个iterable用for循环进行迭代时，
1-调用iter方法得到一个iterator
2-循环调用iterator的next方法，直到为空
3-返回StopIeration异常作为循环的结束标志
4-自动处理异常
'''
# for _ in a:
#     print(_)

'''
生成器：带有yield的函数
generator iterator（生成迭代器，即一个generator对象）是generator function（生成器函数）的返回值
生成器是迭代器的一种，优雅地实现了迭代器协议（用yield做了__next__和__iter__的方法）
'''
g = (x for x in [1,2,3,4,5,6,7,8,9,10])
print(g) #一个生成器对象
print(next(g))
print(next(g))
'''
generator保存的是中断服务子程序，yield是中断服务子程序的断点
generator的第二种调用方法，即send(value)将value作为yield表达式的值'''

print('------------')
def gen():
    while True:
        s = yield
        print(s)

gg = gen()
print(gg)         #在开始状态的生成器对象
print(next(gg))   #generator必须是在yield处暂停的状态，如此才能向yield传值，否则会报错
                  #执行到yield处，暂停，返回值为None
gg.send('kiss')  #将send的参数value作为yield的返回值，则s = 'kiss'，继续执行到yield，暂停
gg.send('me')    #重复上一步
next(gg)         #目前停留在yield处，开始执行,yield没有值传入，s = None，则打印None
                 #又停留到yield
'''
yield更为复杂的用法'''

def echo(value=None):
    while 1:
        value = (yield value)
        print('The value is ',value)
        if value:
            value += 1
print('-----------------')
ggg = echo(1) #value=1传入，生成器产生,执行到yield value处，yield返回值被value接到
print(ggg) #打印的是生成器对象
next(ggg) #执行到yield value表达式，保存上下文返回1
print(ggg.send(2))#第二次调用yield方法，从value = yield处开始，再次遇到yield value返回
next(ggg) #返回值为None
print(ggg.send(3))
next(ggg)
print(ggg.send(4))
