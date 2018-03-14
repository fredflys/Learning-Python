#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author: nulige

import threading
import time

def music():
    print("begin to listen %s"%time.ctime())
    time.sleep(3)
    print("stop to listen %s" %time.ctime())

def game():
    print("begin to play game %s"%time.ctime())
    print('wait')
    print("stop to play game %s" %time.ctime())

if __name__ == '__main__':

    t1=threading.Thread(target=music)
    t2=threading.Thread(target=game)

    t1.start()  #运行实例的方法
    t2.start()

    t1.join()   #子线程对象调用join()方法
    t2.join()

    print("ending")  #在主线程中
