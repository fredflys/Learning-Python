from urllib import request
from urllib import parse
from fake_useragent import UserAgent

ua = UserAgent()
headers = {
    "User-Agent": ua.random
}

url = "http://www.baidu.com/s"
keyword = input("请输入待查询的字符串：")
wd = {"wd": keyword}
encoded_wd = parse.urlencode(wd)
full_url = url + "?" + encoded_wd
request_config = request.Request(full_url, headers=headers)
response = request.urlopen(request_config)

print(response.read())