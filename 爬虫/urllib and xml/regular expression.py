import re
from urllib import request
from urllib import parse
from http import cookiejar
from fake_useragent import UserAgent

ua = UserAgent()
headers = {
    "User-Agent": ua.random
}


class Joke_Spider:
    def __init__(self):
        pass

    def load_page(self, page_num):
        url = 'http://www.neihan8.com/article/list_5_' + str(page_num) + '.html'
        request_obj = request.Request(url=url, headers=headers)
        html_response = request.urlopen(request_obj)
        str_html = str(html_response.read(), encoding='gbk')

        title_pattern = re.compile('<h4>\s+<a href=.*?>(.*?)</a>', re.S)
        title_list = title_pattern.findall(str_html)

        content_pattern = re.compile('<div\sclass="f18 mb20">(.*?)</div>', re.S)
        content_list = content_pattern.findall(str_html)

        return title_list, content_list


def parse_content(alist):
    _l = []
    for i in alist:
        _l.append(re.sub('[<p>,</p>,&rdquo, helli, b]', '', i).strip())
    return _l


def parse_title(alist):
    _l = []
    for i in alist:
        _l.append(re.sub('[<b>,</b>]', '', i).strip())
    return _l


if __name__ == "__main__":
    js = Joke_Spider()
    title_list, content_list = js.load_page(2)
    new_content_list = parse_content(content_list)
    new_title_list = parse_title(title_list)
    for i in range(len(new_content_list)):
        print('题目:%s' % new_title_list[i])
        print(new_content_list[i], '\n')
