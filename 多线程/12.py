#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author: nulige

import threading
import time

def sub():
    global num

    # num -= 1
    temp=num
    #不加等待语句，则得到的值始终为0。因为下文的
    time.sleep(0.00000000001)
    num=temp-1

num =100

l=[]

#创建100个线程，且并发执行。
  for i in range(100):
    t=threading.Thread(target=sub)
    t.start()
    l.append(t)
    print(time.ctime())

for t in l:
    t.join()

print(num)

