"""
cookielib
-CookieJar
管理HTTP Cookie的值、存储HTTP请求生成的cookie、向HTTP请求添加cookie，都在内存中
不与本地文件交互
-FileCookieJar
从CookieJar派生而来，检索cookie信息，并将其存储在文件中
-MozillaCookieJar
从FileCookieJar派生而来，创建与Mozila cookie.txt兼容的FileCookieJar实例
-LWPCookieJar
从FileCookieJar派生而来，创建与libwww-perl标准的Set-Cookie3文件格式兼容的FileCookieJar实例
"""

from urllib import request
from urllib import parse
from http import cookiejar
from fake_useragent import UserAgent

# 准备request对象
login_info = {"email": "xyf220@126.com", "password": "x9zv4vemj7"}
encoded_info = parse.urlencode(login_info)
ua = UserAgent()
headers = {
    "User-Agent": ua.random
}
url = 'http://www.renren.com/PLogin.do'
request_obj = request.Request(url=url, headers=headers, data=bytes(encoded_info,encoding='utf-8'))


# 构建cookie和处理器对象，用来处理cookie
cookie = cookiejar.CookieJar()
cookie_handler = request.HTTPCookieProcessor(cookie)

# 第一次是POST请求，因为有data参数
opener = request.build_opener(cookie_handler)
response = opener.open(request_obj)
print(str(response.read(), encoding='utf-8'))

# 访问需要登陆才能浏览的主页，这时opner已经带有登陆后的cookie
response_profile = opener.open("http://www.renren.com/410043129/profile")
print(str(response_profile.read(), encoding='utf-8'))