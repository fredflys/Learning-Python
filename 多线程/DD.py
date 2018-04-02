"""
协程 是为非抢占式多任务产生子程序的计算机程序组件，
协程允许不同入口点在不同位置暂停或开始执行程序
协程就是你可以暂停执行的函数, 就像生成器一样
"""


def eagar_range(up_to):
    index = 0
    sequence = []
    while index < up_to:
        sequence.append(index)
        index += 1


def lazy_range(up_to):
    index = 0
    while index < up_to:
        yield index
        index += 1

# a_lazy_range = lazy_range(100)
# next(a_lazy_range)

def jumping_range(up_to):
    index = 0
    while index < up_to:
        jump = yield index
        if jump is None
            jump = 1
        index += jump

jr = jumping_range(5)
next(jr)  # 0
jr.send(2)  # 2
next(jr)    # 3
jr.send(-1) # 2
for x in jr:
    print(x)  # 3, 4


def from_lazy_range(up_to):
    index = 0
    def gratuitous_refactor():
        while index < up_to:
            yield index
            index += 1
    yield from gratuitous_refactor()