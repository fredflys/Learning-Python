from urllib import request

"""
request.HTTPPasswordMgrWithDefaultRealm  密码管理对象，用来保存和HTTP请求相关的授权信息
request.ProxyBasicAuthHandler  授权代理处理器
request.HTTPBasicAuthHandler   验证web客户端的授权处理器

"""

usn = 'test'
pwd = '123456'
web_server = '122.114.31.177:808'
# 构建一个密码管理对象
password_mgr = request.HTTPPasswordMgrWithDefaultRealm()
# 添加授权用户信息
password_mgr.add_password(None, web_server, usn, pwd)
# 以密码管理对象为参数，创建auth handler
# 注意这里处理的是web服务器的验证信息，不是代理服务器的验证信息
httpauth_handler = request.HTTPBasicAuthHandler(password_mgr)
# 这个才是处理代理服务器验证信息的handler，可以同时作为创建opener的参数
proxyauth_handler = request.ProxyBasicAuthHandler(password_mgr)

opener = request.build_opener(httpauth_handler, proxyauth_handler)
request_obj = request.Request('http://' + web_server)
response = opener.open(request_obj)
print(response.read())