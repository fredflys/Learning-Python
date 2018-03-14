from multiprocessing import Pool
import time

def foo(i):
    time.sleep(2)
    return i + 100

def end_call(arg):
    print('end call',arg)


#windows系统中执行，必须要有该判断，否则会报错
if __name__ == '__main__':
    #默认池子中并没有5个进程，只有真正用到时才会创建
    p = Pool(5)
    for i in range(10):
        #先执行5个进程，执行完后会返回到池中，然后再执行5个进程
        #p.apply(foo,(i,))
        #排队申请进程，运行完再自动被放回进程池
        #内有join方法
        #daemon=False
        #apply_async：
        #并发申请进程，执行target的方法，完成后将返回值传入callback的方法并执行
        #这就是回调函数
        #异步申请
        #没有join方法，daemon=True
        p.apply_async(func=foo,args=(i,),callback=end_call)

    print('end')
    #立即中止池中运行的进程
    '''p.terminate()'''
    #进程全部执行完后，再中止
    #不中止会有AssertionError
    p.close()
    #join方法中有断言：assert self._state in (CLOSE, TERMINATE)
    #检查进程池有没有中止，中止后才会执行join
    #进程池的join方法，与进程的join方法没有关系
    p.join()
