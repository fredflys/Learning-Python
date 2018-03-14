class Foo:
    def __init__(self,name):
        self.name = name
# 创建对象时，会自动执行__init__方法（构造方法）

class Person:
    def __init__(self,name,age,weight):
        self.Name = name
        self.Age = age
        self.Weight = weight
    def eat(self):
        self.Weight += 2
    def exercise(self):
        self.Weight -= 1

# 游戏的存读档功能可用pickle实现
import pickle
if r:
    print(r.)
else:
    p1 = Person('Jack',21,100)
    p1.eat()
    p1.exercise()
    pickle.dump(p1,open('save.log','wb'))

r = pickle.load(open('save.log''rb')

###################继承##################
class Animals:
    def eat(self):
        pass
    def drink(self):
        pass
    def call(self):
        print('Call')
class Myanimals:
    def favor(self):
        print('I like it.')

class Cat(Animals):
    def __init__(self,name):
        self.Name = name
    def call(self):
        print('miaowww')

class Dog(Animals,Myanimals):
    def __init__(self,name):
        self.Name = name
    def call(self):
        print(self.name + 'bark')
#当父类和子类都有某种方法时，默认优先调用子类的方法
#python中子类可以继承多个父类，而java/c#则不行，是为了避免歧义
#多重继承的顺序
class A:
    def f1(self):
        print('A')
class B:
    def f1(self):
        print('B')
class C(A):
    def f1(self):
        print('C')
class D(B):
    def f1(self):
        print('D')
class E(C,D)
    def f1(self):
        print('E')
obj = E()
obj.f1()
#优先级：先子类后父类
############多态#######################

class Foo:
    def f1:
        print('Foo')

class Bar:
    def f1:
        print('Bar')
def func(arg):
    arg.f1()
f = Foo()
b = Bar()
func(f)
func(b)
# arg既可以是Foo类的对象，也可以是Bar类的对象。这就是多态。
# 强类型语言中的必须规定arg的类别，即 def func(Foo arg)
# 其它语言中通过继承来实现多态

