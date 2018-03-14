import threading
import time

def f0():
    pass
def f1(a,b):
    time.sleep(5)
    print('Child Thread Done')
    f0()

t = threading.Thread(target=f1,args=(1,2))
#必须在start() 方法调用之前设置，主线程中为子线程设置该属性为True，只要主线程执行完毕，则无论子线程状态，都会和主线程一并退出
t.setDaemon(True)
t.start()
t = threading.Thread(target=f1,args=(1,2))
t.setDaemon(True)
t.start()
t = threading.Thread(target=f1,args=(1,2))
t.setDaemon(True)
t.start()

print('Main Thread Done')
#daemon 守护神，和demon恶魔同音 *_*
