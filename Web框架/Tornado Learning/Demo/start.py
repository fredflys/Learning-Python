import tornado.ioloop
import tornado.web
import uimethods as mt
import uimodules as md

# 1.导入模块
# 2.声明类，继承自RequestHandler
# 3.声明tornado web应用，在url和类之间建立路由映射，添加配置
# 4.配置html和静态文件
# 5.使web应用监听特定端口
# 6.声明IO循环实例，并启动

INPUT_LIST = [
]


# 继承类
class MainHandler(tornado.web.RequestHandler):
    # get与post不同之处在于，get可通过url来传输参数，post只能以提交的方式
    def get(self):
        # 后台与html进行交互
        # html则通过模板语言与后台交互
        age = self.get_argument('age', None)
        if age:
            INPUT_LIST.append(age)
        self.write("Hello,Get Yourself Up")
        # 1.打开html文件，读取内容（包含特殊语法）
        # 2.将渲染内容和html集合（通过模板的特殊语法）
        # 3.渲染完成后得到新的字符串，替换html的模板结果返回给用户
        # 4.结果返回给用户

        # 通过render方法，实现了后台和html之间的交互
        self.render("home bak.html", temp=INPUT_LIST, method_arg="Get: I am method argument.")

    def post(self, *args, **kwargs):
        # 获取用户提交的数据
        name = self.get_argument('comment')
        INPUT_LIST.append(name)
        self.render("home bak.html", temp=INPUT_LIST, method_arg="Post: I am method argument.", handler=self, request=self.request)


settings = {
        "template_path": "views",  # 配置html文件路径
        "static_path": "statics",  # 配置静态文件路径
        "ui_methods": mt,
        "ui_modules": md,
    }

# 路由映射
application = tornado.web.Application([
    (r"/index", MainHandler)

], **settings)

# 启动
if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()

