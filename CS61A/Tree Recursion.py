def simple_cascade(n):
    print(n)
    if n > 10:
        print(n)
        cascade(n // 10)
        print(n)


# 虽然多了些代码，但更清晰，指出了base case，更易懂
def cascade(n):
    if n < 10:
        print(n)
    else:
        print(n)
        cascade(n // 10)
        print(n)


# cascade(129481)


def inverse_cascade(n):
    grow(n)
    print(n)
    shrink(n)


def f_then_g(f, g, n):
    if n:
        f(n)
        g(n)


grow = lambda n: f_then_g(grow, print, n // 10)
shrink = lambda n: f_then_g(print, shrink, n // 10)

# inverse_cascade(1234)


from CS61A import ucb
# @ucb.trace
def fib(n):
    """
    效率还比较糟糕，如计算fib(35)
    0 1 1 2 3 5 8 13 21
    >>> fib(0)
    0
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

# @ucb.trace
def count_partitions(n, m):
    """
    the number of partitions of a positive integer n, using parts up to size m, is the
    number of ways in which n can be expressed as the sum of positive integer parts up
    to m in an increasing order
    对n而言上限为m-1的可拆分数 + 对n而言一侧为m的可拆分数（即对n-m而言上限为m的可拆分数）
    >>> count_partitions(6, 4)
    9
    >>> count_partitions(5, 3)
    5
    """
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif m == 0:
        return 0
    else:
        with_m = count_partitions(n-m, m)
        without_m = count_partitions(n, m-1)
        return with_m + without_m


def count_paths(width, height):
    """
    In a rectangle grid of certain width and height, a caterpillar who can only
    move right or up is on the bottom left grid. In order to reach the exit at right
    top grid, How many different paths can the caterpillar take? 
    >>> count_paths(1,1)
    1
    >>> count_paths(1,9)
    1
    >>> count_paths(10,1)
    1
    >>> count_paths(3,3)
    6
    """
    if width == 1 and height == 1:
        return 1
    elif width == 1 and height > 1:
        return 1
    elif width > 1 and height == 1:
        return 1
    else:
        return count_paths(width-1, height) + count_paths(width, height-1)


def count_paths_simpler(width, height):
    """
    >>> count_paths(1,1)
    1
    >>> count_paths(1,9)
    1
    >>> count_paths(10,1)
    1
    >>> count_paths(3,3)
    6
    """
    if width == 1 and height == 1:
        return 1
    else:
        caterprie_goes_up = count_paths(width-1, height)
        caterprie_goes_right = count_paths(width, height-1)
        return caterprie_goes_right + caterprie_goes_up


def knapsack_count(weight, items):
    """
    :param weight: maximum weight of the knapsack
    :param items: [(worth, weight), (worth, weight)]
    :return: how many ways we can fill the knapsack without going over the weight limit
    >>> knapsack_count(-1, [(10, 2)])
    0
    >>> knapsack_count(3, [])
    1
    >>> knapsack_count(10, [(1, 4), (2, 5)])
    4
    """
    if weight < 0:
        return 0
    if len(items) == 0:
        return 1
    with_first_item = knapsack_count(weight - items[0][1], items[1:])
    without_first_item = knapsack_count(weight, items[1:])
    return with_first_item + without_first_item


def count_change(amount, kinds_of_coins):
    """
    >>> count_change(10, 2)
    3
    >>> count_change(100, 6)
    344
    """
    if amount == 0:
        return 1
    elif amount < 0 or kinds_of_coins == 0:
        return 0
    else:
        # 所有不适用第一种零钱的组合方式
        return (count_change(amount, kinds_of_coins - 1)
                # 所有使用第一种零钱的组合方式
                + count_change(amount - first_denomination(kinds_of_coins), kinds_of_coins))


# 为了总额中扣除当前种类中第一种零钱的面额，要返回当前种类中第一种货币的面值
def first_denomination(kinds_of_coins):
    if kinds_of_coins == 6:
        return 100
    elif kinds_of_coins == 5:
        return 50
    elif kinds_of_coins == 4:
        return 20
    elif kinds_of_coins == 3:
        return 10
    elif kinds_of_coins == 2:
        return 5
    elif kinds_of_coins == 1:
        return 1

import doctest
doctest.testmod(verbose=False)
# count_partitions(5, 3)