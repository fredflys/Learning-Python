from urllib import request
from urllib import parse
from fake_useragent import UserAgent

ua = UserAgent()

# 通过Request可以构造HTTP请求
headers = {
    "User-Agent": ua.random
}

# url地址
url = "http://www.baidu.com/"
# 待传入参数需要进行url编码
wd = {"wd": "python编程", "wo": "的"}
encoded_wd = parse.urlencode(wd)
print(encoded_wd)
request_config = request.Request(url, headers=headers)
response = request.urlopen(request_config)
response.getcode()
# 用以确定访问的url地址，检测重定向问题
response.geturl()
# 实现了字典协议的HTTPMessage对象，是服务器相应的HTTP报头
response.info()

