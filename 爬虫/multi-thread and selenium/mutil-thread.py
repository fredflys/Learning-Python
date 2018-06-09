"""
CPU计算
一个CPU一次只能执行一个任务
一个CPU一次只能执行一个进程，其它进程处于非运行状态

本质上来说，进程和线程的区别只是CPU的时间切片长度不同
进程包含的执行单元是线程 ，一对多

进程的内存空间在其线程间是共享的，但在使用时是被独占的（共享单车）
一个线程使用共享对象时，其上会被加锁，防止其它线程使用（互斥锁）

"""
import requests
from fake_useragent import UserAgent
from lxml import etree
import json

from queue import Queue
import threading

CRAWL_EXIT = False
PARSE_EXIT = False


class ThreadingCrawl(threading.Thread):
    def __init__(self, thread_name, page_queue, data_queue):
        super(ThreadingCrawl, self).__init__()
        self.thread_name = thread_name
        self.page_queue = page_queue
        self.data_queue = data_queue

    def run(self):
        print('%s 已经开始采集网页...' % self.thread_name)
        while not CRAWL_EXIT:
            try:
                page_num = self.page_queue.get(False)
                self.data_queue.put(get_html(page_num))
            except:
                pass
        print('%s 已经采集完毕' % self.thread_name)


class ThreadingParse(threading.Thread):
    def __init__(self, thread_name, data_queue, file, lock):
        super(ThreadingParse, self).__init__()
        self.thread_name = thread_name
        self.data_queue = data_queue
        self.file = file
        self.lock = lock

    def run(self):
        print('%s 已经开始解析网页并存储段子' % self.thread_name)
        while not PARSE_EXIT:
            try:
                html = self.data_queue.get(False)
                self.parse_html(html)
            except:
                pass
        print('%s 已经解析完成网页并存储了段子' % self.thread_name)

    def parse_html(self, html):
        tree = etree.HTML(html)
        node_list = tree.xpath('//div[contains(@id, "qiushi_tag")]')
        for node in node_list:
            title = node.xpath('.//h2')[0].text.strip()
            content = node.xpath('.//div[@class="content"]/span')[0].text.strip()
            unum = node.xpath('.//span[@class="stats-vote"]/i')[0].text.strip()
            cnum = node.xpath('.//a[@class="qiushi_comments"]/i[@class="number"]')[0].text.strip()
            image = node.xpath('.//img[@class="illustration"]/@src')
            item = {"title": title,
                                "content": content,
                                "unum": unum,
                                "cnum": cnum,
                                "image": image}
            with self.lock:
                self.file.write(json.dumps(item) + '\n')


def fake_ua():
    ua = UserAgent()
    headers = {"User-Agent": ua.random}
    return headers


def get_html(page_num):
    session = requests.Session()
    url = 'https://www.qiushibaike.com/8hr/page/%s/' % page_num
    html = session.get(url, headers=fake_ua()).text
    return html


def main():
    page_queue = Queue(20)
    data_queue = Queue()
    lock = threading.Lock()
    file = open('qiushi.json', 'a', encoding='utf-8')

    # 往队列放入10个页码
    for i in range(1, 20):
        page_queue.put(i)
    crawl_name_list = ["萧峰", "段誉", "虚竹"]
    parse_name_list = ["阿朱", "木婉清", "梦姑"]
    crawl_thread_list = []
    parse_thread_list = []
    for crawl_thread_name in crawl_name_list:
        thread = ThreadingCrawl(crawl_thread_name, page_queue, data_queue)
        thread.start()
        crawl_thread_list.append(thread)

    for parse_thread_name in parse_name_list:
        thread = ThreadingParse(parse_thread_name, data_queue, file, lock)
        thread.start()
        parse_thread_list.append(thread)

    while not page_queue.empty():
        pass
    global CRAWL_EXIT
    CRAWL_EXIT = True
    print('页码队列已被消耗')
    for crawl_thread in crawl_thread_list:
        crawl_thread.join()

    while not data_queue.empty():
        pass
    global PARSE_EXIT
    PARSE_EXIT = True
    print('数据队列已被消耗')
    for parse_thread in parse_thread_list:
        parse_thread.join()

    with lock:
        file.close()


if __name__ == "__main__":
    main()