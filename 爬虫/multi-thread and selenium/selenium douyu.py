from selenium.webdriver import PhantomJS
from selenium.common.exceptions import NoSuchElementException
from collections import namedtuple
import time

all_live_list = []
info_tuple = namedtuple('Live', ['title', 'host', 'tag', 'viewers'])


def prepare_driver():
    driver = PhantomJS(r'C:\Python36\phantomjs.exe')
    driver.get('https://www.douyu.com/directory/all')
    print('已经到达斗鱼直播主页...')
    return driver


def parse_html(driver):
    global all_live_list
    count = 0
    print('正在解析网页...')
    while True:
        if count == 10:
            return True
        count += 1
        next_page_btn = driver.find_element_by_class_name('shark-pager-next')
        live_list = driver.find_elements_by_xpath('//div[@id="live-list-content"]/ul/li')
        for live in live_list:
            title = live.find_element_by_tag_name('h3').text
            host = live.find_element_by_class_name('fl').text
            viewers = live.find_element_by_class_name('fr').text
            tag = live.find_element_by_class_name('tag').text
            all_live_list.append(info_tuple(title, host, tag, viewers))
        try:
            driver.find_element_by_class_name('shark-pager-disable-next')
            driver.quit()
            return True
        except NoSuchElementException:
            print('已解析完成第%s页...开始解析下一页' % str(count))
            next_page_btn.click()
            time.sleep(0.5)


def write_info(live_list):
    f = open('live info.txt', 'a', encoding='utf-8')
    with f:
        # 中英文混排时，对齐并不准确，因为中文实际输出占用是一个全角字符，也就是两个半角字符，而英文是一个半角字符
        fmt = '{}{}{}{}\n'
        f.write(fmt.format(*info_tuple._fields))
        for live_tuple in live_list:
            f.write(fmt.format(*align_list(list(live_tuple))))
    print('已将数据输入到文件...')


def align_list(l):
    def chinese(data):
        count = 0
        for s in data:
            if ord(s) > 127:
                count += 1
        return count

    for i in range(len(l)):
        count = chinese(l[i])
        if i == 3:
            new_str = '{0:{wd}}'.format(l[i], wd=10 - count)
        else:
            new_str = '{0:{wd}}'.format(l[i], wd=40 - count)
        l[i] = '|%s|' % new_str
    return l


def sort_func(t):
    l = t[3].split('万')
    num = float(l[0])
    if len(l) > 1:
        return num * 10000
    else:
        return num


if __name__ == "__main__":
    dr = prepare_driver()
    if parse_html(dr):
        all_live_list.sort(key=sort_func)
        write_info(all_live_list)