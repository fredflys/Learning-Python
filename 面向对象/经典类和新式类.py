#经典类
class Foo:
    def display(self):
        print('Display Foo.')

    @property
    def prop(self):
        return 'My Property'


f = Foo()
print(f.prop)


class Goods(object):
    '''
    This is the document.
    '''
    # 类私有变量
    __privateone = 'private'

    def __init__(self, value):
        self.value = value
        self.amount = 0

    @property
    def price(self):
        print('Goods Property')
        return self.value

    @price.setter
    def price(self, value):
        print('Setting price...')
        if value > 100:
            self.value = value
            print('Setting done.')
        else:
            print('Setting undone.')

    @price.deleter
    def price(self):
        if int(self.price) > 100:
            del self.value
            print('Price deleted')


cigar = Goods(13)
# 调用被@property装饰的price方法
cigar.price
# 调用被@price.setter装饰的price方法
cigar.price = 101
# 调用被@price.deleter装饰的price方法
print(cigar.price)
print(type(cigar.price))
print(cigar.price)
# 以反射操作对象属性
print(getattr(cigar, 'amount', 100))
print(hasattr(cigar, 'price'))
print(delattr(cigar, 'amount'))
print(dir(cigar))
print(cigar.__dict__)
print(Goods.__dict__)
print(cigar.__doc__)
print(Goods.__name__) #只能用类名调用
print(cigar._Goods__privateone)
# 属性扩展了字段的功能，可以在赋值和删除时额外做别的操作


# 实现常量类
class _const:
    class ConstError(TypeError):
        pass

    def __setattr__(self, name, value):
        if self.__dict__.has_key(name):
            print('Can''t rebind const (%s)' %name)
            raise self.ConstError
        self.__dict__[name] = value

