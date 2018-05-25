# 不稳定

def selection_sort_right(alist):
    # 每次比较都假设最大值位是第一位，并从第二个值开始依次与它比较
    # 一旦发现哪一位的值比假设位的大，就把假设最大值位设置为哪一位
    # 内层循环结束后，就可以获得列表无序部分最大值的位置
    # fillslot永远是列表中无序部分的最高位
    # 将fillslot和positionOfMax位置上的值交换
    # 这样列表无序部分的最大值就归位了

    # 从列表最后一位循环到第二位（因为每次都假设第一位是最大的）
    for fillslot in range(len(alist)-1, 0, -1):
        positionOfMax = 0
        # 从列表第二位循环到end/end-1/end-2
        # 每次循环都会排出列表中的最大值
        for location in range(1, fillslot + 1):
            # 循环位是否大于假设最大值
            if alist[location] > alist[positionOfMax]:
                # 将最大位设置为循环位
                positionOfMax = location
        temp = alist[fillslot]
        alist[fillslot] = alist[positionOfMax]
        alist[positionOfMax] = temp
    return alist


def selection_sort_left(alist):
    """
    假设最小元素的下标为0，让其与之后的每一个元素比较，如遇更小值，则下标变动为该元素
    全部比较完成后，将最小元素下标处的值与第0个元素替换（也就是选出右边无序序列部分中最小的一个，放到左边，故名选择排序）
    重复该过程，可知列表从左侧开始逐渐有序，直到整个列表变为有序序列
    """
    length = len(alist)
    for j in range(0, length-1):
        min_index = j
        for i in range(j+1, length):
            if alist[min_index] > alist[i]:
                min_index = i
        alist[j], alist[min_index] = alist[min_index], alist[j]
    return alist


print(selection_sort_right([6, 1, 4, 7, 5, 9, 2, 9, 10, 3]))
print(selection_sort_left([6, 1, 4, 7, 9, 5, 2, 9, 10, 3]))