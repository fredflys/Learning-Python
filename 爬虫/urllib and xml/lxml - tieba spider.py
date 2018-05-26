from urllib import request
from lxml import etree
from urllib import parse
import json
import re


def load_main_page(tieba_name, page_num):
    """
    :param tieba_name: 贴吧名
    :param page_num: 待处理的该贴吧页数
    :return: 返回当前页的html，以便接下来解析
    """
    base_url = 'https://tieba.baidu.com/f?'
    pn = (page_num - 1) * 50
    paras = {"kw": tieba_name, "ie": "utf-8", "pn": str(pn)}
    full_url = base_url + parse.urlencode(paras)
    response = request.urlopen(full_url)
    html = str(response.read(), encoding='utf-8')
    return html


def parse_main_html(html):
    """
    :param html: 某贴吧某页的html
    :return: 当前页内的主题帖标题与其链接后缀
    """
    xml_tree = etree.HTML(html)
    # 每个帖子的地址后半部分，形如/p/5716244071
    # 可使用chrome的xpath helper插件帮助定位
    post_lable_list = xml_tree.xpath("//li[contains(@class, 'j_thread_list')]/div[1]/div[2]/div[1]/div[1]/a/@href")
    title_list = xml_tree.xpath("//li[contains(@class, 'j_thread_list')]/div[1]/div[2]/div[1]/div[1]/a/@title")
    return title_list, post_lable_list


def get_post_html(post_label):
    """
    :param post_label: 主题帖的后缀
    :return: 返回要处理的主题帖地址的列表
    """
    # 对每一个主题帖创建一个列表，如有多页，则列表中会有多个元素
    post_html_list = []
    base_url = 'https://tieba.baidu.com'
    post_link = base_url + post_label
    post_html_list.append(post_link)
    response = request.urlopen(post_link)
    html = str(response.read(), encoding='utf-8')
    tree = etree.HTML(html)
    # 如果帖子有多页，则处理每一页上的帖子
    pager_list = tree.xpath('//li[contains(@class, "l_pager")]/a/@href')
    if pager_list:
        for page_label in pager_list:
            sub_post_link = base_url + page_label
            post_html_list.append(sub_post_link)
    return post_html_list


def parse_post_html(post_html):
    """
    :param post_html: 主题帖特定页的地址
    :return:  打印当前页内每一层的帖子作者与帖子内容（纯文本）
    """
    response = request.urlopen(post_html)
    html = str(response.read(), encoding='utf-8')
    tree = etree.HTML(html)
    # 定位到每一个帖子
    thread_list = tree.xpath('//div[contains(@class, "l_post")]/@data-field')
    for thread in thread_list:
        thread_poster = json.loads(thread)['author']['user_name']
        raw_content = json.loads(thread)['content']['content']
        # 清洗掉帖子内容中的html标签
        text_content = re.sub('<.*?>', '', raw_content)
        print('----', thread_poster, " 说: ", text_content)


def run_spider(tieba_name, page):
    """
    对所有功能函数进行上层封装
    """
    main_html = load_main_page(tieba_name, page)
    post_title_list, post_lable_list = parse_main_html(main_html)
    for i in range(len(post_lable_list)):
        print('主题：', post_title_list[i])
        post_html_list = get_post_html(post_lable_list[i])
        for page in post_html_list:
            parse_post_html(page)


if __name__ == "__main__":
    run_spider('steam', 1)