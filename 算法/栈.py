# 先进后出
# 以列表实现的简单栈

class SimpleStack:
    # 特殊属性，用以限制class可添加的属性
    __slots__ = ('__items',)

    def __init__(self):
        self.__items = []

    def is_empty(self):
        return self.__items == []

    def peek(self):
        return self.__items[len(self.__items)-1]

    def size(self):
        return len(self.__items)

    def push(self, item):
        self.__items.append(item)

    def pop(self):
        self.__items.pop()


class StackFullException(Exception):  # 满栈时要抛出的异常
    pass


class StackEmptyException(Exception):  # 空栈时要抛出的异常
    pass


class Node:
    def __init__(self, val=None, nxt=None):
        self.value = val  # 信息域
        self.next = nxt   # 指针域

    def __str__(self):
        return str(self.value)


class Stack:
    # 初始化一个空栈
    def __init__(self, max=0):
        self._top = None  # 栈的顶部元素
        self._max = 0  # 栈的最大高度
        self.max = max  # 用户将设置的最大栈高度

    @property
    def length(self):
        if self._top is None:
            return 0
        node = self._top
        count = 1  # 只要不为空，就至少有一个节点，因此由1开始
        # 借由节点内的指针来判断是否有下一个元素，只要就由当前节点跳到下一个节点，并将计数加1
        while node.next:
            node = node.next
            count += 1
        return count

    @property
    def is_empty(self):
        return self._top is None

    @property
    def is_full(self):
        # 满栈的条件是栈的最大高度不是无限的（设置最大值时会将负数也转为0，0就代表了无限大小）
        # 而且当前栈高等于允许的最大栈高
        return bool(self._max and self.length == self._max)

    @property
    def max(self):
        return self._max

    @max.setter
    def max(self, m):
        m = int(m)  # 可能传入值是str或float
        if m < self.length:  # 设置值是否小于当前栈的高度，是则要抛出异常
            raise Exception('Stack resize failed, please pop some elements first.')
        self._max = 0 if m < 0 else m  # 输入值又是否是负数或0，是则都设置为0，当作无限大小

    # 通过逐个压入传入的iterable，由空栈构建出一个栈
    def init(self, iterable=()):
        if not iterable:  # 传入一个可迭代对象
            return
        self._top = Node(iterable[0])  # 将其起始元素设置为栈顶
        for item in iterable[1::]:  # 将之后的元素也依次压入栈中,每一次压入栈定元素都会被替换
            node = self._top  # 原栈顶元素先储存起来
            self._top = Node(item)  # 将当前元素设置为栈顶
            self._top.next = node  # 将设置过的栈定的指针指向原来的栈顶

    """
    |   5   |
    |   4   |
    |   3   |
    |   2   |
    |   1   |  显示的样板
    """
    def show(self):
        # 定义的子函数是为了遍历栈，这里用到了生成器
        def _traversal(self):
            node = self._top
            while node and node.next:
                yield node
                node = node.next
            # 这里如果不yield，则栈底的元素会无法被遍历到，因为最后一个元素并不满足while循环的条件，会中止迭代
            yield node
        # <>^ 左/右/居中对齐
        # 生成器也是可迭代的，这里用高阶函数将字符串格式方法映射到每一个元素上
        print('\n'.join(map(lambda x: '|{:^7}|'.format(str(x)), _traversal(self))) + '\n ' + 7 * '-')

    def push(self, item):
        # 如果栈已满，则抛出异常
        if self.is_full:
            raise StackFullException('Error: trying to push an item into a full stack.')
        # 如果栈是空的，则直接将item设置为栈顶，返回即可，因为不需要设置指针
        if not self._top:
            self._top = Node(item)
            return
        node = self._top  # 先取到原栈顶
        self._top = Node(item)  # 设置item为栈顶
        self._top.next = node  # 将设置过的栈顶的指针指向原栈顶

    def pop(self):
        if self.is_empty:
            raise StackEmptyException('Error: trying to pop from an empty stack.')
        node = self._top  # 先取到原栈顶
        self._top = self._top.next  # 将栈顶设置为原栈顶的下一个元素
        return node.value  # 返回原栈顶的值

    def top(self):
        return self._top.value if self._top else None

    def clear(self):  # 在已构造的方法上再构造新方法
        while self._top:
            self.pop()


s = Stack()
s.init([1, 2, 3, 4, 5])
s.show()
