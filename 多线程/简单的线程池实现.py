#python没有定义，需要自己编写
#线程池：如果有就直接取出，没有就需要等待
#基于queue

import queue
import threading
import time

class ThreadPool(object):
    def __init__(self,max_num=20):
        #创建一个长度为max_num的序列
        self.queue = queue.Queue(max_num)
        for i in range(max_num):
            #将Thread类名传入队列
            #缺陷：1.不能像进程此一样，只是创建了池子，并没有实际创建进程，而是等着程序去申请
            #这是可改进之处
            #2.缺乏回调函数
            #3.使用成本高，每次函数中还要调用add_thread方法和start方法
            self.queue.put(threading.Thread)
    def get_thread(self):
        return self.queue.get()
    def add_thread(self):
        self.queue.put(threading.Thread)

def foo(pool,a):
    time.sleep(1)
    print(a)
    #如不添加新线程，会进入等待状态，队列的特性
    pool.add_thread()

p = ThreadPool(10)
#返回的是Thread类名,取到了一个线程，即threading.Thread
for i in range(100):
    ret = p.get_thread()
    #为线程指定函数和参数

    thread = ret(target=foo,args=(p,i,))
    #启动线程
    #执行完后被销毁
    thread.start()
