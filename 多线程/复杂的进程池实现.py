#-*coding:utf-8*-
'''
诸如web服务器、数据库服务器、文件服务器和邮件服务器等许多服务器应用都面向处理来自某些远程来源的大量短小的任务。构建服务器应用程序的一个过于简单的模型是：每当一个请求到达就创建一个新的服务对象，然后在新的服务对象中为请求服务。但当有大量请求并发访问时，服务器不断的创建和销毁对象的开销很大。所以提高服务器效率的一个手段就是尽可能减少创建和销毁对象的次数，特别是一些很耗资源的对象创建和销毁，这样就引入了“池”的概念，“池”的概念使得人们可以定制一定量的资源，然后对这些资源进行复用，而不是频繁的创建和销毁。
线程池是预先创建线程的一种技术。线程池在还没有任务到来之前，创建一定数量的线程，放入空闲队列中。这些线程都是处于睡眠状态，即均为启动，不消耗CPU，而只是占用较小的内存空间。当请求到来之后，缓冲池给这次请求分配一个空闲线程，把请求传入此线程中运行，进行处理。当预先创建的线程都处于运行状态，即预制线程不够，线程池可以自由创建一定数量的新线程，用于处理更多的请求。当系统比较闲的时候，也可以通过移除一部分一直处于停用状态的线程。

'''

import queue
import threading
import time
import contextlib
#队列：放任务
#线程：一一次次取任务，而不是执行完后被销毁

#与任务包不同即可
StopEvent = object()

class ThreadPool(object):
    def __init__(self,max_num):
        #创建队列，不限制大小
        self.q = queue.Queue()
        #可创建的最大线程数（线程池最大容量）
        self.max_num = max_num
        self.terminal = False
        #实际创建的线程列表（线程虽多，但当任务少且执行速度很块，可能实际用到的并不是全部）
        self.generate_list = []
        #空闲的线程数（线程池中实际分配到任务的线程之外的线程）
        self.free_list = []
    def run(self,func,args,callback=None):
        #将任务打包到一个元组中
        w = (func,args,callback)
        #将任务包放到队列中
        self.q.put(w)

        #如果没有空闲线程，并且已创建线程未达到最大限制数，则新建线程
        if len(self.free_list) ==  0 and len(self.generate_list) < self.max_num:
            self.generate_thread()


    def generate_thread(self):
        #新建一个线程
        t = threading.Thread(target=self.call)
        t.start()

    def call(self):
        '''循环获取任务函数并执行任务函数'''
        #获取当前活跃线程
        current_thread = threading.currentThread
        #将活跃线程添加到实际创建线程列表中
        self.generate_list.append(current_thread)
        #取任务并执行
        event = self.q.get()

        #如果从任务队列中取出的不是停止标志（即是元组，也就是任务包）：
        while event != StopEvent:
            #是任务包，则解任务包
            func,args,callback = event
            status = True
            try:
                result = func(args)
            except Exception as e:
                status = False
                result = e

            #回调函数有参数则执行，无参数则不执行
            if callback is not None:
                try:
                    callback(status,result)
                except Exception as e:
                    pass

            #默认是False
            if self.terminal:
                event = StopEvent
            else:
                self.free_list.append(current_thread)
                #event重新赋值，依次是下一个任务
                event = self.q.get()
                self.free_list.remove(current_thread)

        else:
            #不是任务包,将当前线程从实际创建线程列表中移除
            self.generate_list.remove(current_thread)
            #再队列中添加停止符
            #让正在从队列中取任务的线程挂掉

    def close(self):
        threads = len(self.generate_list)
        while threads:
            self.q.put(StopEvent)
            threads-=1

    #中止线（不清空队列）
    def terminate(self):
        self.terminal = True
        max_num = len(self.generate_list)
        while max_num:
            self.q.put(StopEvent)
            max_num -= 1

def action(_):
    print(_)
pool = ThreadPool(5)
#有300个任务
for i in range(100):
    #将任务放在队列中
    #开始处理任务
    #   -> 创建线程
    #       有空闲线程则直接去取，不再创建
    #       不能高于线程池的限制
    #       根据任务个数判断
    #  -> 线程去队列中取任务
    ret = pool.run(action,(i,))
    #print(len(pool.generate_list))
#各个线程仍在运行，在从generate_list中取任务
#这时传入停止符，使其中止

pool.terminate()
