#未加锁的情况
'''

import threading
import time

def sub():
    global temp
    global num
    #该函数将全局变量num减去1
    # num -= 1
    temp=num
    #刻意将线程执行时间混淆，如果不加这一句，似乎python会依次执行（？）得到0
    time.sleep(0.0000000001)
    num=num-1
#num初始化为100
num =100

l=[]
#100个线程
for i in range(100):
    t=threading.Thread(target=sub)
    t.start()
    l.append(t)

for t in l:
    t.join()
print(num)
print(temp)
#temp的值并不固定
'''


# 加锁的作用：就是把多线程变成串行，结果就不会变

# !/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: nulige

import threading
import time


def sub():

    global num

    # num -= 1
    lock.acquire()  # 获取锁
    temp = num
    time.sleep(0.001)
    num = temp-1
    lock.release()  # 释放锁


num = 100

l = []
lock = threading.Lock()

for i in range(100):
    t = threading.Thread(target=sub)
    t.start()
    l.append(t)

for t in l:
    t.join()

print(num)
