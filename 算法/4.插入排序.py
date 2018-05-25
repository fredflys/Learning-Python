"""
将列表的第一个元素视作有序序列，取剩余元素的第一个，以倒序和有序序列中的每一个元素比较(while loop)，
如前者更小，则交换，（也就是插入到前面有序列表的合适位置中，故得名插入排序）
全部比较完成后，则前面的有序序列长度有增加了一位
重复以上过程(for loop)，直到整个列表都变为有序序列
"""
# 稳定
def insertionSort(alist):
    for index in range(1, len(alist)):
        # currentvalue在一次循环内是一直不变的，它就是待插入的值
        currentvalue = alist[index]
        # 指针赋予初始值为index
        position = index

        # 如果指针没有拨到0，而且指针前一位置的值大于currentvalue，则把前一位置的值拿到当前位置，并将指针向列表前推进一位
        while position > 0 and alist[position-1] > currentvalue:
            alist[position] = alist[position - 1]
            position = position - 1
        # 现在指针前面的值都已经排列整齐，就将currentvalue放到指针所在位置上
        alist[position] = currentvalue


def insertion_sort(alist):
    # 从右边的无序列表中依次取出与左边的
    for i in range(1, len(alist)):
        # 从右边的无序列表中取第一个元素，将其插入到正确的位置中
        while i:
            if alist[i] < alist[i-1]:
                alist[i], alist[i-1] = alist[i-1], alist[i]
                i -= 1
            # 只要大于前一个位置的值，则大于前面所有的值，因为左侧一直维持着有序序列
            # 加上break，可优化算法
            else:
                break
        """
        # 也可用for循环实现
        for j in range(i, 0, -1):
            if alist[j] < alist[j - 1]:
                alist[j], alist[j - 1] = alist[j - 1], alist[j]
        """
    return alist


l = [10, 3, 5, 7, 8, 2, 4, 6, 1]
# insertionSort(l)
insertion_sort(l)
print(l)