#导入first.py模块
m = __import__('first',fromlist=True)

#从first模块中导入Foo类
class_name = getattr(m,'Foo')
#创建Foo类的对象
obj = class_name('yeff')
n = getattr(obj,'name')
print(n)
