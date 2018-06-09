from urllib import request
from fake_useragent import UserAgent as UA
from lxml import etree
from collections import namedtuple
import re


# 产生代理连接池
# 因为是免费代理，还需要预先判断代理是否可以使用
# 尚未进行处理
# 原本是为了应对豆瓣的封锁机制定义好的，后来使用了cookie进行模拟登陆
# 也就没有再完善
def get_time(s):
    pattern = re.compile('\d+')
    number = int(re.findall(pattern, s)[0])
    time = 0
    if '小时' in s:
        time = number * 60
    elif '天' in s:
        time = number * 24 * 60
    elif '月' in s:
        time = number * 30 * 24 * 60
    elif '年' in s:
        time = number * 365 * 24 * 60
    return time if time else number


def get_proxy_list():
    request_obj = request.Request(url='http://www.xicidaili.com/', headers={'User-Agent': UA().random})
    response = request.urlopen(request_obj)
    html = str(response.read(), encoding='utf-8')

    xml = etree.HTML(html)
    ip_list = xml.xpath('//tr[@class="odd" or @class]/td[2]/text()')
    port_list = xml.xpath('//tr[@class="odd" or @class]/td[3]/text()')
    type_list = xml.xpath('//tr[@class="odd" or @class]/td[6]/text()')
    endure_list = xml.xpath('//tr[@class="odd" or @class]/td[7]/text()')
    last_check_list = xml.xpath('//tr[@class="odd" or @class]/td[8]/text()')

    proxy_list = []
    proxy = namedtuple('proxy', ['ip', 'port', 'type', 'endure', 'last_check'])
    for i in range(len(ip_list)):
        proxy_list.append(
            proxy(ip_list[i], port_list[i], type_list[i], get_time(endure_list[i]), get_time(last_check_list[i]))
        )
    return proxy_list

