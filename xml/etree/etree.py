# cElementTree是用C语言写成的，效率更高，因此优先使用
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET
import sys

# 获取xml树状结构对象
tree = ET.ElementTree(file='movies.xml')
# 获取根节点对象
root = tree.getroot()
print(root.tag)  # 根节点的标签
print(root.attrib)  # 获取根节点的属性,值，以键值对的字典形式存储

# 逐级查找
for subnode in root:
    print(subnode)
    print(subnode.tag)
    print(subnode.attrib)  # 遍历根节点下每个子节点[非子孙节点]，一次获取一个子节点对象
print(root[0])  # 获取根节点下第一个子节点对象
print(root[0].getchildren())  # 获取第一个子节点对象所有的子节点
print(root[0].getchildren()[0].text)  # 获取第一个子节点对象其子节点中的第一个，并获取它的文本内容

# 打印所有子节点下的星级和评级信息
for subnode in root:
    print(subnode.getchildren()[-2].text, subnode.getchildren()[-3].text)


# 当xml层级很深的时候，虽然可以不断地向根部元素后加索引逐级获取
# 但这样做太过笨拙，可用iter方法迭代所有层级,会取到所有子孙层级的元素[深度优先]
# 可以统计一共有多少子孙节点
# iter是在整个树内查找，iterfind只能查找当前层级
count = 0
for ele in tree.iter():
    print(ele)
    count += 1
print(count)
# 筛选
for ele in tree.iter():
    if ele.text == '1989':
        print('Found it!')
# 用文本方式统计，可用count方法，因为将文件读为了字符串
with open('d:\\movies.xml') as f:
    content = f.read()
    print(content.count('movie'))
# 查找元素时，如果知道层级关系，但不清楚位置，可用iterfind方法查找
for ele in tree.iterfind('movie/year'):
    print(ele)
# 查找元素时，如果不知道层级关系，可用iter方法，加上tag参数，遍历所有层级来查找
for ele in tree.iter(tag='year'):
    print(ele)
# 基于属性来查找，但iterfind只能基于当前层级，不能往下深入
# movie/type是指定了具体的层级，也可以用*代表模糊查找
for ele in tree.iterfind('movie/type[@title="Ishtar"]'):
    print(ele)


# 01:24:20
