from tornado.ioloop import IOLoop
import tornado.web
from controllers import account
from controllers import home
from controllers import extend


settings = {
        "template_path": "views",  # 配置html文件路径
        "static_path": "statics",  # 配置静态文件路径
    }


# 路由映射
# 基于正则路由是为了解决基本路由僵化的一一对应问题，可以实现一个类处理多种url
application = tornado.web.Application([
    #
    (r"/index/?(?P<page>\d*)", home.IndexHandler),
    (r"/login", account.LoginHandler),
    # 模板继承与导入
    (r"/extend/index", extend.ExtendIndexHandler),
    (r"/extend/home", extend.ExtendHomeHandler),
], **settings)


# 启动服务端
if __name__ == "__main__":
    application.listen(8888)
    IOLoop.instance().start()

