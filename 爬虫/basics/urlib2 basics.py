from urllib import request

# 向指定的url地址发送请求，并返回服务器相应的类文件对象
# 不支持构造HTTP请求，默认的user-agent是 Python-urllib/
response = request.urlopen("http://www.baidu.com/")
# 类文件对象顾名思义，支持python文件对象的方法
html = response.read()
# print(str(html, encoding='utf-8'))


