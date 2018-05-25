from urllib import request

# 构建一个HTTPHandler处理器对象，支持处理HTTP的请求
# debuglevel设为1则程序在执行时会打印收发包的信息
http_handler = request.HTTPHandler(debuglevel=1)
# 使用handler构建一个自定义opener
# opener的作用就是发送请求
opener = request.build_opener(http_handler)
request_obj = request.Request("http://www.baidu.com")
response = opener.open(request_obj)
print(response.read())