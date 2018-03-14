def insertionSort(alist):
    for index in range(1,len(alist)):
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


l = [1, 3, 5, 7, 8, 2, 4, 6]
insertionSort(l)
print(l)