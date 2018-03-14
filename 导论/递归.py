# 阶乘的迭代和递归表达
def iter_factorial(n):
    result = 1
    while n > 1:
        result = n * result
        n -= 1
    return result


def recur_factorial(n):
    if n == 1:
        return n
    else:
        return n * recur_factorial(n-1)


# 汉诺塔问题
def print_move(fr, to):
    print('Move from ' + str(fr) + 'to ' + str(to))


def hanoi_tower(n, fr, to, spare):
    if n == 1:
        print_move(fr, to)
    else:
        hanoi_tower(n-1, fr, spare, to)
        hanoi_tower(1, fr, to, spare)
        hanoi_tower(n-1, spare, to, fr)


# 斐波那契数列
def fibonacci(x):
    assert type(x) == int and x >= 0
    if x == 0 or x == 1:
        return x
    else:
        return fibonacci(x-1) + fibonacci(x-2)


# 回文检测
def is_palindrome(s):
    def to_chars(s):
        s = s.lower()
        res = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwsyz':
                res = res + c
        return res

    def is_pal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and is_pal(s[1:-1])

    return is_pal(to_chars(s))
