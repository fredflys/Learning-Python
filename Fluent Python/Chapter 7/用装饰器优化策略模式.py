promos = []


def promotion(promo_func):
    promos.append(promo_func)
    return promo_func


@promotion
def fidelity(order):
    pass


@promotion
def bulk_item(order):
    pass


# 只需装饰想要加入promos列表的函数，就可以完成注册
# 无需使用特殊函数名
# 清晰地为被装饰函数提供了说明，可随时将其移出
# promotion一类的函数可被定义在任意模块内，随时添加
def best_promo(order):
    return max(promo(order) for promo in promos)