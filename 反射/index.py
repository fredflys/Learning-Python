'''
import test
#根据用户输入内容，导入模块
inp = input('Enter the module name:')
#根据字符串形式来导入模块
T = __import__('test') #等同于import test as TT
#在模块中寻找函数并执行
f = getattr(TT,'f1')
f()                     #等同于T.f1()

#getattr(module_name,func_name_in_str)
f = getattr(test,'f1')  #f指向test模块中的f1函数
'''

#实现一个类web请求
'''
from lib import account
url = input('Enter a url:')
if url.endswith('login'):
    r = account.login()
elif url.endswith('logout'):
    r = account.logout()'''
# 缺陷：页面下如有千百个功能，则每个功能都要如此判断，效率低下。

# 基于反射实现类web框架的路由系统
# 定义输入为模块名/函数名
inp = url.split('/')[-1]
# 常为web框架所用
if hasattr(m,target_func):
    target_func = getattr(account,inp)
    r = target_func()
else:
    print('404')
