'''
*意味着解包字典外的集合类型
'''
# 拆开集合的值，并把这些值当作位置参数传给函数，供其调用
def fun(a,b,c):
    print(a,b,c)
l = [1,2,3]
s = (1,2,3)
l2 = [2,3]
fun(1,2,3)
fun(*l)
fun(*s)  #可以是各种集合类型
fun(1,*l2) #可以和单个位置参数并用

'''
*args 在函数形参位置上意味着‘0个或多个位置参数’,在函数体中则意味着解包元组，代表着一个个参数
此时args在函数体中是若干个参数的元组，是单个可迭代对象
*args代表任何多个无名参数，是一个tuple
'''
print('------------------------')
# *args接收位置参数之外的参数作为元组，


def funa(a,*args):
    print('a is ',a)
    print('args is',args)
    print('*args are',*args)
funa(1,[2,3])
funa(1,2,3,4)
funa(1)
# 计算除一个参数外其它参数的和


def ignore_first_calculate_sum(a, *iargs):
    def calculate_sum(*args):
        return sum(args)  # sum(iterable[,start])
    # sum接收的参数是可迭代对象，而calculate_sum接收的参数是若干个位置参数
    # 因此这里传入参数时需要用*解包，传入除第一个之外的位置参数
    required_sum = calculate_sum(*iargs)
    print('Sum is ',required_sum)
ignore_first_calculate_sum(1,2,3,4)

'''
**意味着解包字典
'''
print('----------------------------')
def funb(a,b,c):
    print(a,b,c)
funb(1,2,3)
funb(a=1,b=2,c=3)
d = {'b': 2,'c': 3}
funb(a=1,**d)

'''
**kwargs接收常规参数外的键值参数字典，kwargs在函数体中是一个字典
**kwargs表示关键字参数，是一个dict
'''


def func(a,**kwargs):
    print(a,kwargs)
func(1, b=2, c=3)

# *args必须在**kwargs之前
