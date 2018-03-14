# thread-safe, double-ended queue for inserting and removing from both ends
# and it can be bounded if you like
# removing and inserting from the left of a list is costly because the entire list must be shifted
from collections import deque

dq = deque(range(10), maxlen=10)
dq.rotate(3)  # 从右边拿三个元素放到左边，对自身生效
dq.rotate(4)  # 从左边拿四个放到右边
dq.appendleft(-1)  # 在左边插入-1，最右边的一个元素会被挤出
dq.extend([11, 12, 13])  # 在右边插入整个列表，因此顺序是依次11，12，13 最左边的三个元素会被挤出
dq.extendleft([10, 20, 30, 40])  # 迭代地将列表内的元素从左加入到deque中，因此顺序是40，30，20，10