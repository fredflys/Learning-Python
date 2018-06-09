from bs4 import BeautifulSoup as bs
import requests
from fake_useragent import UserAgent
from lxml import etree
import json
"""
Unix時間戳 下·下·
"""


def fake_ua():
    ua = UserAgent()
    headers = {"User-Agent": ua.random}
    return headers


def save_duanzi_original(page_num):
    session = requests.Session()
    url = 'https://www.qiushibaike.com/8hr/page/%s/' % page_num
    html = session.get(url, headers=fake_ua()).text
    tree = etree.HTML(html)
    node_list = tree.xpath('//div[contains(@id, "qiushi_tag")]')

    title_node_list = tree.xpath('//div[contains(@id, "qiushi_tag")]//h2')
    content_node_list = tree.xpath('//div[contains(@id, "qiushi_tag")]//div[@class="content"]/span')
    up_node_list = tree.xpath('//span[@class="stats-vote"]/i')
    cnum_node_list = tree.xpath('//a[@class="qiushi_comments"]/i[@class="number"]')

    title_list = [i.text.strip() for i in title_node_list]
    content_list = [i.text.strip() for i in content_node_list]
    up_list = [i.text.strip() for i in up_node_list]
    cnum_list = [i.text.strip() for i in cnum_node_list]
    info_list = []
    for i in range(len(title_list)):
        d = {"title": title_list[i],
             "content": content_list[i],
             "up": up_list[i],
             "cnum": cnum_list[i]
             }
        info_list.append(d)

    with open("qiushi_%s.json" % page_num, "a") as f:
        f.write(json.dumps(info_list, ensure_ascii=False))

# root //div[contains(@id, "qiushi_tag")]
# title //div[contains(@id, "qiushi_tag")]//h2
# content //div[contains(@id, "qiushi_tag")]//div[@class="content"]/span
# up //span[@class="stats-vote"]/i
# comments //a[@class="qiushi_comments"]/i[@class="number"]
# pictures //img[@class="illustration"]


def save_duanzi(page_num):
    session = requests.Session()
    url = 'https://www.qiushibaike.com/8hr/page/%s/' % page_num
    html = session.get(url, headers=fake_ua()).text
    tree = etree.HTML(html)
    node_list = tree.xpath('//div[contains(@id, "qiushi_tag")]')
    duanzi_list = []
    for node in node_list:
        title = node.xpath('.//h2')[0].text.strip()
        content = node.xpath('.//div[@class="content"]/span')[0].text.strip()
        unum = node.xpath('.//span[@class="stats-vote"]/i')[0].text.strip()
        cnum = node.xpath('.//a[@class="qiushi_comments"]/i[@class="number"]')[0].text.strip()
        image = node.xpath('.//img[@class="illustration"]/@src')
        duanzi_info_dict = {"title": title,
                            "content": content,
                            "unum": unum,
                            "cnum": cnum,
                            "image": image}
        duanzi_list.append(duanzi_info_dict)
    with open("qiushi_%s.json" % page_num, "a") as f:
        f.write(json.dumps(duanzi_list, ensure_ascii=False))


if __name__ == "__main__":
    save_duanzi(1)