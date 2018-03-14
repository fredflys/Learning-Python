import threading

def do(event):
    print('Start')
    #亮灯
    event.wait()
    print('Execute')

#创建一个事件对象
event_obj = threading.Event()
for i in range(10):
    #讲事件对象传入函数，
    t = threading.Thread(target=do,args=(event_obj,))
    t.start()

#让灯变红
event_obj.clear()
#输入true时，才继续执行
inp = input('>>>')
if inp == 'true':
    #类似变成绿灯
    event_obj.set()

#事件处理的机制：全局定义了一个“Flag”，如果“Flag”值为 False，那么当程序执行 event.wait 方法时就会阻塞，如果“Flag”值为True，那么event.wait 方法时便不再阻塞。
# clear：将“Flag”设置为False
# set：将“Flag”设置为True
