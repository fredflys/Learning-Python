# yield的作用正如同其在英文中的两个意思：produce and give way
# 产生值并让步（暂停生成器的执行过程）
# yield x 正如字面的理解，x被产出（只是形象的说法，
# 与被return语句里返回意味不同，只是执行到x就停止了，停到了yield），
# yield被赋予了send方法的参数值
# 理解yield的关键是将它当作控制运行过程的装置


from inspect import getgeneratorstate as ggs


def averager():
    total = 0.0
    count = 0
    average = None
    print('Before While...')
    while True:
        print('average(before term assignment): ', average, '\n')
        term = yield average
        print('term: ', term)
        print('average(after term assignment): ', average)
        total += term
        count += 1
        average = total/count


coro_avg = averager()
print(ggs(coro_avg))
# priming the coroutine
# 执行到average处停止,也就是还未执行yield，因此此时term还未定义
next(coro_avg)


# 从yield处恢复，参数10通过yield传入，term被赋值为10， 而average仍为None,之后同理
avg1 = coro_avg.send(10)
avg2 = coro_avg.send(30)
avg3 = coro_avg.send(80)
print(avg1, avg2, avg3)