from tornado import web
import tornado.ioloop


class IndexHandler(web.RequestHandler):
    def get(self):
        if self.get_argument('user', None) in ['yeff', 'mike']:
            self.set_secure_cookie('n', self.get_argument('user'))
            self.write('欢迎')
        else:
            self.write('请登陆')


class ManagerHandler(web.RequestHandler):
    def get(self):
        # 注意这里取得的cookie是bytes格式的，不是字符串格式
        if self.get_secure_cookie('n', None) in [b'yeff', b'mike']:
            self.write('欢迎登陆: ' + str(self.get_secure_cookie('n'),encoding="utf-8"))
        else:
            self.redirect('/index')


settings = {
    "template_path": "views",
    "static_path": "statics",
    "cookie_secret": "salt",
}

application = web.Application([
    (r"/index", IndexHandler),
    (r"/manager", ManagerHandler),
], **settings)

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()