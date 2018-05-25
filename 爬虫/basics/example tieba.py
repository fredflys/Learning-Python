from urllib import request
from urllib import parse
from fake_useragent import UserAgent


def fake_ua():
    ua = UserAgent()
    headers = {
        "User-Agent": ua.random
    }
    return headers


def load_page(url):
    print("正在下载...")
    request_config = request.Request(url, headers=fake_ua())
    response = request.urlopen(request_config)
    return response.read()


def write_page(html, file_name):
    print('正在保存 ' + file_name)
    with open(file_name, "w") as f:
        f.write(html)


def tieba_spider(url, begin, end):
    for page in range(begin, end + 1):
        pn = (page - 1) * 50
        file_name = "第" + str(pn) + "页.html"
        page_url = url + "&pn=" + str(pn)
        html = load_page(page_url)
        write_page(html, file_name)


if __name__ == "__main__":
    tieba_name = input("请输入待爬取的贴吧名：")
    begin_page = int(input("爬取起始页："))
    end_page = int(input("爬取终止页："))

    base_url = "https://tieba.baidu.com/f?"
    encoded_name = parse.urlencode({"kw": tieba_name})
    full_url = base_url + encoded_name
    tieba_spider(full_url, begin_page, end_page)