import threading
import time


def process(arg):
    time.sleep(1)
    print(arg)


# for i in range(10):
#    process(i)
# 创建了10个线程，同时处理
for i in range(10):
    t = threading.Thread(target=process, args=(i,))
    t.start()


# 如果线程是按照生成顺序执行的，那完全没问题
# 但是线程调度是由操作系统完成的，不可预测
# 定义的函数里先暂停一秒再打印结果，分两步执行，执行该函数的线程就随时可能在中间中断
# 如果是简单的赋值语句，虽然只有一句