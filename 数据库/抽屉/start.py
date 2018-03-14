import tornado.ioloop
import tornado.web
import pymysql as pymysql


INPUT_LIST = [
]

USER_INFO = {
    'is_login': None,
}

# 动态地生成新闻
NEWS_LIST = [
    {"title": "第一条新闻", "content": "北京大火"},
    {"title": "第二条新闻", "content": "强制拆迁"},

]


class HomeHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render("home bak.html", userinfo=USER_INFO, newslist=NEWS_LIST)


class LoginHandler(tornado.web.RequestHandler):
    def post(self, *args, **kwargs):
        username = self.get_argument('usn', None)
        password = self.get_argument('pwd', None)
        if username == 'yeff' and password == '123':
            USER_INFO['is_login'] = True
            USER_INFO['username'] = username
        # self.render('home bak.html', userinfo= USER_INFO)
        self.redirect('/home')

    def get(self):
        pass


class PublishHandler(tornado.web.RequestHandler):
    def post(self, *args, **kwargs):
        if USER_INFO['is_login']:
            title = self.get_argument('title', None)
            content = self.get_argument('content', None)
            _news_dict = {'title': title, 'content': content}
            NEWS_LIST.append(_news_dict)
        # 直接跳转到/home，也就避免了渲染时再次传入参数
        self.redirect('/home')


class DBUtil(object):
    def __init__(self, host=None, port=None, user=None, passwd=None, db=None):
        self.conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db)
        self.cursor = pymysql.cursor(pymysql.cursors.DictCursor)



settings = {
        "template_path": "views",  # 配置html文件路径
        "static_path": "statics",  # 配置静态文件路径
    }

# 路由映射
application = tornado.web.Application([

    (r"/home", HomeHandler),
    (r"/login", LoginHandler),
    (r"/publish", PublishHandler),
], **settings)

# 启动
if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()

