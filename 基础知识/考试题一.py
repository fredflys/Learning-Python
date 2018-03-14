'''
计算100-300之间所有能被3和7整除的所有数之和
'''
def total():
    sum = 0
    for i in range(100,301):
        if i%3 == 0 and i%7 == 0:
            sum += i
    print(sum)


'''
定义一个函数，统计一个字符串中大写字母、小写字母、数字的个数，并返回结果
注意全局变量，不要把函数内要用到的参数定义在全局中
'''
def pick(s):
    upper = 0
    lower = 0
    num = 0
    for i in s:
        if i.isupper():
            upper += 1
        elif i.islower():
            lower += 1
        elif i.isnumeric():
            num += 1
    print('There are:\n%d characters in upper-case,\n%d characters in lower-case,\nand %d numbers in' % (upper,lower,num),s,'.')

'''
获取两个列表中的相同元素集合
'''
def overlap(list1,list2):
    set1 = set(list1)
    set2 = set(list2)
    return set1.intersection(set2)

'''
返回汉字的utf-8字节编码
'''
def get_bytes(s):
    return bytes(s,encoding='utf8')

'''
浅拷贝只拷贝最外层，深拷贝除最后一层外全部拷贝
'''

'''
使用requests和xml模块实现天气查询，输出方式对人类友好
http://ws.webxml.com.cn/WebServices/WeatherWS.asmx/getWeather?theuserid=&thecitycode=
'''
def getweatherinfo(city):
    import xml.etree.ElementTree as ET
    import requests

    page = requests.get('http://ws.webxml.com.cn/WebServices/WeatherWS.asmx/getWeather?theuserid=&thecitycode='+city)
    page.encoding = 'utf-8'
    tree = ET.XML(page.text)
    for node in tree:
        t = node.text
        if 'gif' and 'jpg' not in t:
            print(t)


