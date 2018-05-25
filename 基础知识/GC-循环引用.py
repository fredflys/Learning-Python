import gc
import sys


class A(object):
    def __init__(self):
        print('object creaetd, id:%s' % str(hex(id(self))))

    # 一般不要重写del方法，否则对该对象的垃圾回收不会正常执行
    # 需要的话，应该先将自己要做的事做完，然后调用父类的del方法
    # def __del__(self):
    #     pass
    #


def create_object():
    while True:
        obj1 = A()
        obj2 = A()
        obj1.ref = obj2
        obj2.ref = obj1
        del obj1
        del obj2
        gc.collect()  # 可以自行回收，即使被关闭


# 关闭GC后，注意内存使用会不断增长，直至崩溃
# 否则，内存占用一直很稳定，不断创建，不断被回收
gc.disable()
# create_object()
print('执行垃圾回收的计数器的当前值： %d %d %d' % gc.get_count())
# 新创建的对象个数减去已释放完的对象个数 > 700，就会触发0代链表的出来
# 每清理10次0代链表，清理1次1代链表，并顺便清理0代链表
print('执行清理0、01、012代链表的阈值： %d %d %d' % gc.get_threshold())
# 可以自己设置清除的阈值哦
gc.set_threshold(750, 11, 11)

# 获取对象的引用计数，会比实际计数多1,因为调用该函数时对象本身就作为参数被传入了，增加了1次
a = A()
print('实例a的引用计数：%d' % (sys.getrefcount(a) - 1))
print('类A的引用计数：%d' % (sys.getrefcount(A) - 1))
print('已经被回收的垃圾：%s ' % gc.garbage)