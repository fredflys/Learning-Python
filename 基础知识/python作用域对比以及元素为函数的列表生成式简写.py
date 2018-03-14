li = []
for i in range(10):
    def f1():
        return i
    li.append(f1)
    # 和下面的lambda写法是等价的
    # li.append(lambda: i)

# 此时li内是10个函数，添加的只是函数，而不是函数的返回值
print(li)
# 返回值是9，而不是0
# 因为f1一直都没有执行过，而这时i经过循环已经等于了9
# 注意python中循环中的i并不会随着循环结束而消失掉
print(li[0]())

# 另一种生成列表的简写方式
li2 = [x+10 for x in range(10) if x > 5]
print(li2)

li3 = [lambda: x for x in range(10)]
print(li3[0]())
