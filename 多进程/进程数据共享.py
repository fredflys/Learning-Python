'''
from multiprocessing import Process
from multiprocessing import Manager
import time

li = []
def foo(i):
    li.append(i)
    print('say hi',li)

if __name__ == '__main__':
    #每个进程都为自己新建一个列表，进程间并不共享资源，只有进程内不同线程共享资源
    for i in range(10):
        #这样就能得到1到10的列表
        #p = Thread(target=foo,args=(i,))
        p = Process(target=foo,args=(i,))
        p.start()
    print('End',li)
'''

'''
#方法一：数组（Array）
#创建数组时，必须提前声明大小 -> 为了利用连续的内存地址
#数组内的数据必须是同一类型 -> 数字和字符串占用的内存大小不一致
#直接调用C中的对象
from multiprocessing import Array,Process
temp =  Array('i',[11,22,33,44,])

def bar(i):
    temp[i] = 100 + i
    for item in temp:
        print(i,'--->',item)
if __name__ == '__main__':
    for i in range (2):
        p = Process(target=bar,args=(i,))
        p.start()
'''

#方法二：manager共享数据（推荐）
from multiprocessing import Process,Manager
#其实就是特殊的字典,用于进程间共享资源


def foo(i,dic):
    dic[i] = 100 + i
    for k,v in dic.items():
        print(k,v)
        print(len(dic))

if __name__ == '__main__':
    manager = Manager()
    #在主进程中创建
    dic = manager.dict()
    for i in range(2):
        p = Process(target=foo,args=(i,dic,))
        p.start()
        #要阻塞当前进程，挨个执行进程
        #不如此，主进程执行到此已经结束，其它进程无法连接到主进程获取资源
        #因此要保证主进程不会中止，而要保持运行状态
        #进程间通信类似socket
        #不加此句，看报错信息即可知之，有PipeClient,self.run,self._connect()等句
        #p.join()

