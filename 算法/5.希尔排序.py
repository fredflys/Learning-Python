# 希尔排序是插入排序的改进版
# 不稳定


def shell_sort(alist):
    """希尔排序"""
    gap = len(alist) //  2
    while gap >= 1:
        for i in range(gap, len(alist)):
            while i > 0:
                if alist[i] < alist[i-gap]:
                    alist[i], alist[i-gap] = alist[i-gap], alist[i]
                    i -= gap
                else:
                    break
        gap //= 2


l = [10, 3, 5, 7, 8, 2, 4, 6, 1]
shell_sort(l)
print(l)