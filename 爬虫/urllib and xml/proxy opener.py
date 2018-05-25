from urllib import request

# 设置开关，控制是否启用代理
proxy_switch = False
# 构建代理handler，参数是字典类型，包括代理类型和服务器IP及端口
proxy_handler = request.ProxyHandler({"http": "123.139.56.238:9999"})
# 构建一个没有代理的处理器对象
null_proxy_handler = request.ProxyHandler({})
opener = request.build_opener(proxy_handler)
if proxy_handler:
    opener = request.build_opener(proxy_handler)
else:
    opener = request.build_opener(null_proxy_handler)

# 构建了一个全局opener（非必要）
request.install_opener(opener)
request_obj = request.Request("http://www.baidu.com")
response = request.urlopen(request_obj)
print(response.read())


