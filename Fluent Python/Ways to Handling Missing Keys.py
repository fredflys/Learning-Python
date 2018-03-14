import re
import collections

txt = r'C:\Users\a634238\zen.txt'
WORD_RE = re.compile('\w+')
index = {}

with open(txt, encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)
            # k不在字典中时，get(k, d)返回的是d,而非设置的默认值的引用，
            # 因此连用append()方法是无法更新字典的键值
            occurrences = index.get(word, [])
            occurrences.append(location)
            index[word] = occurrences

index = {}
with open(txt, encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)
            # k不在字典中时，setdefault(k, d)方法返回默认插入后的值，
            # 因此可以直接进行更新，并且不用二次赋值
            index.setdefault(word, []).append(location)


# 构造一个defaultdict，默认工厂是list，
# 当试图获取不存在的key（只对__getitem__()有作用）时，就调用工厂函数，
# 并返回对返返回值得引用
index = collections.defaultdict(list)
with open(txt, encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)
            index[word].append(location)