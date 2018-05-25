# a+b+c=1000 且 a^2 + b^2 = c^2, abc都为自然数，求所有组合
# 枚举
# 算法是独立存在的解决问题的方法和思想
# 输入 输出 有穷（步骤和时间） 确定
import time


# 时间复杂度 n^3 * 2 -> n^3  是步骤而非运算时间
# 渐近函数：忽略常数
# 剪枝留干
# 大O表示法
# 关注最坏时间复杂度
# 基本操作：O(1)
# 顺序结构：加法
# 循环结构：乘法
# 分支结构：取最大值
# 忽略次要项和常数项
def first_try():
    start = time.time()
    for a in range(0, 1001):
        for b in range(0, 1001):
            for c in range(0, 1001):
                if a + b + c == 1000 and a ** 2 + b ** 2 == c ** 2:
                    print('a,b,c: %d %d %d' % (a, b, c))
    end = time.time()
    print('time: %fs' % (end-start))


# T(n) = n * n * ( 1 + max(0,1))
#      = n ^ 2 * 2
#      = O(n ^ 2)
def second_try():
    start = time.time()
    for a in range(0, 1001):
        for b in range(0, 1001):
            c = 1000 - a - b
            if a ** 2 + b ** 2 == c ** 2:
                print('a,b,c: %d %d %d' % (a, b, c))
    end = time.time()
    print('time: %fs' % (end - start))


first_try()
second_try()

# 常见的时间复杂度
# 12           O(1)     常数阶
# 2n + 3       O(n)     线性阶
# 3n^2 + 2n    O(n^2)   平方阶
# 5log2n + 20  O(logn)  对数阶
# 3nlog2n + 10 O(nlogn) nlogn阶
# 5n^3+2n^2    O(n^3)   立方阶
# 2^n          O(2^n)   指数阶
