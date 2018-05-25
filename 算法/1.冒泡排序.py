# 稳定
def bubble_sort(lst):
    count = 0
    for i in range(len(lst)-1):
        for j in range(len(lst)-1-i):
            count += 1
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst, count


if __name__ == '__main__':
    l = [2, 3, 4, 5342, 2, 3, 5, 3, 1]
    a, c = bubble_sort(l)
    print(a, c)