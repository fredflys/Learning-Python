def selectionSort(alist):
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


print(selectionSort([6, 1, 4, 7, 9, 2, 9, 10, 3]))