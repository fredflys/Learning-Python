class BIRD(object):
    def __init__(self, category):
        self.category = category

    def get_name(self):
        return 'BIRD'

    @classmethod
    def get_age(cls):
        return 20

    @staticmethod
    def get_sex():
        return 'Male'

    def get_sound(self):
        return 'gaga'


class CHINA_BIRD(BIRD):
    # 没有构造方法，会自动调用父类的构造方法
    def __init__(self):
        print('子类初始化一个实例')
        # super(CHINA_BIRD,self).__init__('CHINA and WORLD')
        BIRD.__init__(self, 'CHINA and WORLD')

    def parent_method(self):
        # 以父类之名直接调用父类方法
        # 把上一个函数返回的值再用return接收一下，否则就会丢失
        return BIRD.get_age()

    def my_method(self):
        # 以子类之名调用父类方法
        return self.get_name()

    # 有和父类重名的方法，就近原则
    def get_sound(self):
        return 'haha'


cb = CHINA_BIRD()

print(cb.parent_method())
print(cb.my_method())
print(cb.category)
print(cb.get_sound())
# 判断类类之间以及类与对象之间的关系
print(issubclass(CHINA_BIRD, BIRD))
print(isinstance(cb, CHINA_BIRD))
