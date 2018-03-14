import tornado.ioloop
import tornado.web
import json


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        code = self.get_argument('code')
        func = self.get_argument('callback')
        code = '0' if code not in ['1', '2', '3'] else code
        data = {
            '0': '根据提供的参数没有找到数据哦',
            '1': 'Divinity: Original Sin',
            '2': 'Watch Dogs',
            '3': 'Dishonored    ',
        }
        # 字符串拼接，我拼接得也很笨拙
        send_str = func + "({" + "'" + "num" + "'" + ":" + "'" + code + "'" + "," + "'" + "message" + "'" + ":" + "'" + data[code] + "'" + "});"
        print(send_str)
        self.write(send_str)

    def post(self):
        self.write('alert("8002 Post");')


class CorsHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('123')

    def post(self):
        # 响应头的值如有多个，在单引号内用逗号隔开
        # 如果要允许所有网站自由共享，则将单引号内的值改为*
        self.set_header('Access-Control-Allow-Origin', 'http://127.0.0.1:8001, ,')
        self.write('CORS请求成功啦，服务端摸了模你的头')

    def options(self):
        self.set_header('Access-Control-Allow-Origin', 'http://127.0.0.1:8001')
        self.set_header('Access-Control-Allow-Methods', 'PUT')
        self.set_header('Access-Control-Allow-Headers', 'k')
        # 用来设置预检的失效时间
        self.set_header('Access-Control-Max-Age', 10)
        # 是否允许客户端携带cookie来，当允许cookie时，allow-origin属性的值就不能是*，必须是具体的url
        self.set_header('Access-Control-Allow-Credentials', 'true')
        print('服务器端给了客户端一张通行证,并允许put方法和自定义请求头通过')

    def put(self):
        # 这时客户端才会发送put请求的内容
        # 可以这样理解复杂请求：
        # 每次发送请求时，客户端都先派个叫OPTIONS的小人，去服务端叫叫门，
        # 服务端知道后，返回个客户端一张临时卡片，上面写着允许XX网站的XX请求通过
        # 然后客户端就发送put请求过来了
        # 服务端根据put请求返回数据时，临时卡片早没用了，又得在返回的东西最前头
        # 加个响应头，说我已经允许X网站和我共享资源了，客户端你就接收吧
        self.set_header('Access-Control-Allow-Origin', 'http://127.0.0.1:8001')
        self.set_header('Access-Control-Allow-Credentials', 'true')

        # 可以自定义发回数据的响应头，但要设置expose-headers属性
        self.set_header('title', 'whatever')
        self.set_header('Access-Control-Expose-Headers', 'title')
        self.write('你好，我是服务端，总算把你们网站CORS PUT请求的内容给你啦，真是麻烦死啦')

settings = {
        "template_path": "views",  # 配置html文件路径
        "static_path": "statics",  # 配置静态文件路径
    }


# 路由映射
application = tornado.web.Application([
    (r"/index", IndexHandler),
    (r"/cors", CorsHandler),
], **settings)

# 启动
if __name__ == "__main__":
    application.listen(8002)
    tornado.ioloop.IOLoop.instance().start()

