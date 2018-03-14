'''
成员
'''


class Foo:
    # 静态字段，存在类中
    static_filed = 'I am in class'
    # 内部修饰符（静态字段），只能被类的方法访问到，类和外部都不能访问
    __internal = 'only can be accessed by Foo class'

    # 构造方法
    def __init__(self,name):
        # 普通字段，在对象中
        self.name = name
    # 析构方法

    def __del__(self):
        print('Object is abondoned.')
    # 将类对象当作函数执行时（即在对象后加括号），会自动调用该方法

    def __call__(self):
        print('The object is callable.')

    # 对对象进行迭代时，会调用该方法
    def __iter__(self):
        yield 1
        yield 2
        yield 3

    # 静态方法。与对象无关，应该直接通过类来访问
    @staticmethod
    def static_show(arg1,arg2):
        print(arg1,arg2)

    # 类方法,必须有cls参数。执行时自动将类名传入cls
    @classmethod
    def class_show(cls):
        print('This is ' + cls)

    # 属性化，将普通方法伪造为字段的形式，直接通过访问字段的方式去执行方法
    # 即obj.pro_show，不用再加()
    # 因此要属性化的方法不能有self以外的参数
    @property
    def pro_show(self):
        return self.name

    # 设置属性化后的方法
    # obj.pro_show = setted_value
    # 当执行上一语句时，会找到被@pro_show.setter修饰的pro_show方法并执行
    # 结果将打印setted_value
    # python中并不常用
    @pro_show.setter
    def pro_show(self,arg1):
        print(arg1)

    # 普通方法，在类中。必须要有self参数，应该通过对象进行访问
    def show(self):
        print(self.name)
        self.__status = 'Already displayed'

    # 私有修饰过的方法，只能被类中的其它方法访问到，不能被对象直接访问到
    def __fetch(self):
        print('Fetched')
    # 通过类中的其它方法访问私有方法，对象可以通过调用这个方法来间接访问到私有方法

    def get_fetch(self):
        self.__fetch()

    # 对象加中括号时会自动调用。典型应用为字典取键位值和列表切片，d['k1']
    def __getitem__(self, item):
        pass
    # 为对象加中括号并赋值时会自动调用，典型应用为字典键位赋值，d['k1'] = 1

    def __setitem__(self, key, value):
        pass

    # 对加中括号的对象执行del语句时会自动调用。典型应用为删除字典键值，del d['k1']
    def __delitem__(self, key):
        pass

    # 将对象当作字符串处理时，会调用该方法。异常处理中捕获错误信息时有应用。
    def __str__(self):
        return 'Object info'


# 反射：以字符串形式去对象中操作其成员
r = hasattr(Foo,'show')

# 反射既可以找对象中的成员，也会找所属类的成员
# 对于类而言，反射就只能找类的成员
obj = Foo('yeff')
r2 = hasattr(obj,'show')


'''
静态字段的例子 
'''
# 将每个对象的共有值，可通过静态字段来存储，更为方便


class Province():
    country = '中国'

    def __init__(self,name):
        self.name = name


hebei = Province('河北')
henan = Province('河南')

# 通过对象去访问类中的方法
obj = Province()
obj.show()
# 尽量不要通过类去访问类中的方法
Province.show(obj)
