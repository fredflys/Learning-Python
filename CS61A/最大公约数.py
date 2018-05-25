import doctest


def gcd_a(x, y):
    """
    >>> gcd_a(12, 6)
    6
    >>> gcd_a(13, 7)
    1
    >>> gcd_a(4, 4)
    4
    >>> gcd_a(100, 40)
    20
    >>> gcd_a(0, 30)
    30
    >>> gcd_a(3, 0)
    3
    """
    if x == y:
        return x
    if x == 0:
        return y
    if y == 0:
        return x
    if x > y:
        return gcd_a(x % y, y)
    else:
        return gcd_a(x, y % x)


def gcd_b(x, y):
    """
    >>> gcd_b(12, 6)
    6
    >>> gcd_b(13, 7)
    1
    >>> gcd_b(4, 4)
    4
    >>> gcd_b(100, 40)
    20
    >>> gcd_b(0, 30)
    30
    >>> gcd_b(2, 0)
    2
    """
    if not x or y == 0:  # 优化
        return x or y
    if not x % y:  # 优化
        return y
    elif x > y:
        return gcd_b(x-y, y)
    else:
        return gcd_b(y, x)


def gcd_c(x, y):
    """
    >>> gcd_c(12, 6)
    6
    >>> gcd_c(13, 7)
    1
    >>> gcd_c(4, 4)
    4
    >>> gcd_c(100, 40)
    20
    >>> gcd_c(0, 30)
    30
    >>> gcd_c(2, 0)
    2
    """
    if x < y:
        x, y = y, x
    while y != 0:
        temp = y
        y = x % y
        x = temp
    return x


def gcd_d(x, y):
    """
    >>> gcd_d(12, 6)
    6
    >>> gcd_d(13, 7)
    1
    >>> gcd_d(4, 4)
    4
    >>> gcd_d(100, 40)
    20
    >>> gcd_d(0, 30)
    30
    >>> gcd_d(2, 0)
    2
    """
    result = 1
    if x == 0 or y == 0:
        # return abs(x-y)
        return x or y
    if x < y:
        smaller = x
    else:
        smaller = y
    for i in range(1, smaller + 1):
        if x % i == 0 and y % i == 0:
            result = i
    return result


if __name__ == "__main__":
    doctest.testmod(verbose=False)
