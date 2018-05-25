"""
菱形
分组拆分，再分组合并
将列表进行二等份切分，直到单个元素为止，再从单个元素开始，逆向合并，合并过程中
对进行合并的两组进行比较，因此每一层级合并的结果总是有序的。
最后得到的新列表即是有序列表
空间有额外开销
nlog2n
"""
def merge_sort(alist):
    n = len(alist)
    mid = n // 2
    # 分到不可再分，则最后的alist只有1个元素
    # 返回alist，以让递归最底层的left_list接收到
    if n <= 1:
        return alist

    left_list = merge_sort(alist[:mid])
    right_list = merge_sort(alist[mid:])
    # merge(left_part, right_part)
    left_pointer, right_pointer = 0, 0
    result = []
    while left_pointer < len(left_list) and right_pointer < len(right_list):
        if left_list[left_pointer] <= right_list[right_pointer]:
            result.append(left_list[left_pointer])
            left_pointer += 1
        else:
            result.append(right_list[right_pointer])
            right_pointer += 1
    result += left_list[left_pointer:]
    result += right_list[right_pointer:]
    return result


l = [10, 3, 5, 7, 8, 2, 4, 6, 1]
print(merge_sort(l))
