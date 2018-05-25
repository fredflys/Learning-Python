# iterative


def iterative_fibonacci(n):
    pred, curr = 1, 0
    k = 1
    while k < n:
        pred, curr = curr, pred + curr
        k = k + 1
    print(curr)
    return curr


iterative_fibonacci(0)