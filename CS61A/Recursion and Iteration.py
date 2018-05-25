def split(n):
    return n // 10, n % 10


def sum_digits_original(n):
    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        # Figure out what must be maintained by the iterative function
        # this one
        return sum_digits_original(all_but_last) + last


def sum_digits_iter(n):
    # the digit sum so far and unsumed digits is what we should maintain
    digit_sum = 0
    while n > 0:
        n, last = split(n)
        digit_sum = digit_sum + last
    return digit_sum


def sum_digits_recur(n, digit_sum):
    if n == 0:
        return digit_sum
    else:
        n, last = split(n)
        return sum_digits_recur(n, digit_sum + last)