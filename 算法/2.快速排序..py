# 快速排序
# 1.基于递归
# 2.找到轴值，小于的放在左边，大于的放在右边
# 不稳定
# nlog2n
"""
不再将无需序列视作两部分
直接找每个元素在有序序列中的位置
确定第一个元素的位置，以一个low游标和high游标分别指向第1个元素和最后一个元素
两个游标迎头移动，右侧先行（因为low从元素本身的下标开始）， low游标确保经过元素都比第一个元素小，high游标确保经过元素都比第一个元素大
不符合则停下，放到另一侧游标所指的位置，直到两个游标碰面，
最后则该位置就是第一个元素应该在的位置，将第一个元素交换到这里
再对元素左右两侧的子列表应用同一方法

"""
def quick_sort(l):
    def sort(listx, left, right):
        if left >= right:
            return
        pivot = listx[left]
        i = left
        j = right
        while i != j:
            # 当前设计中，j必须比i先动
            # 假如i先动，则i最后停止时指向的数字必定大于当前轴值
            # 因为i在先运动时，i < j是一直满足的，能让它停下来
            # 只可能是listx[i] > pivot
            # 那最后j停下来时，为了满足i < j的条件，和i一起停留的位置所指向的值一定是大于轴值的
            # 在将轴值和停留点的值交换后，就会发现比轴值大的数居然跑到左边去了
            while listx[j] >= pivot and i < j:
                j -= 1
            while listx[i] <= pivot and i < j:
                i += 1
            if i < j:
                listx[i], listx[j] = listx[j], listx[i]
        # 此时i和j相等，即i和j已碰头，将轴值与最左边的数交换
        listx[left] = listx[i]
        # 轴值的位置已经确定
        listx[i] = pivot
        # 在分别对轴值的左半边和右半边递归调用sort()方法
        sort(listx, left, i-1)
        sort(listx, i+1, right)

    start = 0
    end = len(l) - 1
    sort(l, start, end)


# 快速排序：更清晰的一种实现 #
def quickSort(alist):
    quickSortHelper(alist, 0, len(alist)-1)


def quickSortHelper(alist, first, last):
    if first < last:
        splitpoint = partition(alist, first, last)

        quickSortHelper(alist, first, splitpoint-1)
        quickSortHelper(alist, splitpoint+1, last)


def partition(alist, first, last):
    pivotvalue = alist[first]

    leftmark = first
    rightmark = last

    done = False
    while not done:
        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1
        while leftmark <= rightmark and alist[rightmark] >= pivotvalue:
            rightmark = rightmark - 1
        if leftmark > rightmark:
            done = True
        else:
            # 左右交换
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp
    # 右头交换
    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp
    return rightmark


# 又一种实现
def quick_sort_another(alist, first, last):
    if first >= last:
        return
    mid_value = alist[first]
    low = first
    high = last
    while low < high:
        # high游标左移
        # 将相等元素都放在一边处理更好
        # while low < high and alist[high] >= mid_value:
        #     high -= 1
        # alist[low] = alist[high]
        # low += 1
        # # low游标右移
        # while low < high and alist[low] < mid_value:
        #     low += 1
        # alist[high] = alist[low]
        # high -= 1

        # 保证移动的条件都是在low < high的条件下进行的
        # low和碰面时的位置不会被错过
        while low < high and alist[high] >= mid_value:
            high -= 1
        alist[low] = alist[high]

        while low < high and alist[low] < mid_value:
            low += 1
        alist[high] = alist[low]
    # 循环退出时low和high相等
    alist[low] = mid_value
    # quick_sort_another(alist[:low-1])
    # quick_sort_another(alist[low+1:])
    quick_sort_another(alist, first, low-1)
    quick_sort_another(alist, low+1, last)

l = [10, 3, 5, 7, 8, 2, 4, 6, 1]
quick_sort_another(l, 0, len(l)-1)
print(l)


