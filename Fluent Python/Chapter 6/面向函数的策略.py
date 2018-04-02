from abc import ABC, abstractmethod
from collections import namedtuple

Customer = namedtuple('Customer', 'name fidelity')


class LineItem:
    # 物品类：产品，数量，价格
    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.quantity * self.price


class Order:
    # 订单类：购买人，物品列表，应用的促销种类
    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion

    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total

    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            # 不再依赖抽象类，转而以函数为第一类对象
            discount = self.promotion(self)
        return self.total() - discount

    def __repr__(self):
        fmt = '<Order total: {:.2f} due: {:.2f}>'
        return fmt.format(self.total(), self.due())


# 每种策略都对应一个函数
def fidelity_promo(order):
    pass


def bulk_item_promo(order):
    pass


def large_order_promo(order):
    pass


# 将promotion方法一个个加入到列表中
# 笨方法，以后每添加一个方法都要自己更新
promos = []


def best_promo(order):
    """Select the best discount available
    """
    return max(promo(order) for promo in promos)


# 从全局变量中获取以_promo结尾的方法
# 可实现在同文件内自动找到所有的promotion方法
# 不足之处是方法命名必须统一，且都要在同一文件中
promos = [
    globals()[name] for name in globals()
    if name.endswith('_promo')
    and name != 'best_promo'
]


# 还可将promotion相关方法都写入promotions文件中，用inspect获得其中的函数
# 分块管理，且方法名可自定义
# 不足在于promotions文件中要注意不可有其它方法
# 之后还有用装饰器改进过的版本
import inspect
promos = [
    func for name, func in inspect.getmembers(promotions, inspect.isfunction)
]

joe = Customer('joe', 0)
ann = Customer('ann', 500)
cart = [
    LineItem('banana', 10, .5),
    LineItem('apple', 5, 3)
]
Order(joe, cart, fidelity_promo)