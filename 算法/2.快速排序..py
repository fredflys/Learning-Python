# 快速排序
# 1.基于递归
# 2.找到轴值，小于的放在左边，大于的放在右边


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

