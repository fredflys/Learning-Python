import threading
import time


# 继承Thread类
class MyThread(threading.Thread):
    def __init__(self, id):
        threading.Thread.__init__(self)
        self.id = id
    # 重写了Thread的run方法

    def run(self):
        x = 0
        time.sleep(10)
        print(self.id)


if __name__ == '__main__':
    # 创建一个线程，ID为101
    t1 = MyThread(101)
    t1.start()
    # t1.join(timeout=11)
    print('----Intersection-----')
    for i in range(5):
        print(i)
# 不在start后加join方法：
# 线程创建并开始后，主线程并没有等待t1运行结束后再执行，而是先把循环执行完毕，等待10秒后，才把线程ID打印了出来

# 在start后加join方法:
# 线程t1开始后，主线程停在了join方法处，先执行了t1线程后，再继续执行主线程
# timeout参数设置主线程最大等待时间，或者说子线程超时限制，或者说主线程为子线程预留的最大时间数
# 也可以说是否设置为并发
