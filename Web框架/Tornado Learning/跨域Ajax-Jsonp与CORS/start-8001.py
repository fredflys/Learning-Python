import tornado.ioloop
import tornado.web
import json


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')
        self.write

    def post(self):
        self.write('8001 Post')


settings = {
        "template_path": "views",  # 配置html文件路径
        "static_path": "statics",  # 配置静态文件路径
    }


# 路由映射
application = tornado.web.Application([
    (r"/index", IndexHandler),
], **settings)

# 启动
if __name__ == "__main__":
    application.listen(8001)
    tornado.ioloop.IOLoop.instance().start()

