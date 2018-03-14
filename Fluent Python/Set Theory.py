# 相异元素的集合
# 内部元素必须是hashable，set本身并不是hashable
# Example
needles = {1}
haystack = {1, 2, 4, 4, 4, 6, 1, }
# infix operation needs both element to be set
found = len(needles & haystack)
# in case they are not sets
found = len(set(needles) & set(haystack))
# or intersection method can be used, which does not require arguments to be set
haystack1 = []  # list
haystack2 = ()  # tuple
haystack3= {1: 'a'}  # dict
found = len(set(needles).intersection(haystack1, haystack2, haystack3))

# set comprehensions
from unicodedata import name
s = {
    chr(i) for i in range(32, 256) if 'SIGN' in name(chr(i), '')
}

# set operations
s = {1, 2, 3, 4, 5, 6}
z = {3, 4, 5, 7, 8, 9}
# 交集
s & z  # __and__x
s.intersection(z)
s &= z  # __iand__
s.intersection_update(z)
# 并集
s | z  # __or__
s.union(z)
s |= z  # __ior__
# 差集
s - z  # __sub__
s.difference(z)  # s有而z没有
s -= z  # __isub__
s.difference_update(z)
# 对称差集
# s有而z没有，或z有而s没有（除去交集后两者的并集） (s | z) - (s & z)
s ^ z  # __xor__
s.symmetric_difference(z)
s ^= z  # symmetric_difference_update

# set predicate
# 断言，返回True或False的operator与method
s.isdisjoint(z)  # s and z have no elements in common?
e in s  # __contains__ e is a member of s?
s <= z  # __le__ s is a subset of z?
s.issubset(itrable)
s < z  # __lt__ s is a proper subset of z? 真子集:A是B的子集，且B中至少有1个元素不属于A
s >= z  # s is a superset of the z set
s.issuperset(iterable)



