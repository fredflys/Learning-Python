#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author: nulige

import threading
import time

#自己定制一个MyThread的类
class MyThread(threading.Thread):
    def __init__(self, num):
        threading.Thread.__init__(self)
        self.num = num

    def run(self):  # 定义每个线程要运行的函数

        print("running on number:%s" % self.num)

        time.sleep(3)


if __name__ == '__main__':
    t1 = MyThread(1)  #继承这个类，把1这个参数，传给num ,t1就是个线程对象
    t2 = MyThread(2)
    t1.start()
    t2.start()

    print("ending......")
