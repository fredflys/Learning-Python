import tornado.ioloop
import tornado.web
import time


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html', )


class ManagerHandler(tornado.web.RequestHandler):
    def get(self):
        cookie = self.get_cookie('auth')
        if cookie == '1':
            self.render('manager.html')
        else:
            self.redirect('/login')


class LoginHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('login.html', status_text='')

    def post(self):
        username = self.get_argument('username', None)
        password = self.get_argument('password', None)
        checked = self.get_argument('auto', None)
        if username == 'abc' and password == '123':
            if checked:
                self.set_cookie('usn', username, expires_days=7)
                self.set_cookie('auth', expires_days=7)
            else:
                expire_time = time.time() + 60 * 30
                # domain：针对哪个域名生效
                # path：为cookie划分权限，在那一些目录下生效，默认是'/'，全局生效
                self.set_cookie('usn', username, expires_days=expire_time)
                self.set_cookie('auth', '1', expires=expire_time, path='/')
            self.redirect('/manager')
        else:
            self.render('login.html', status_text='登陆失败')


class LogoutHandler(tornado.web.RequestHandler):
    def get(self):
        self.set_cookie('auth', '1', expires=time.time())
        self.set_cookie('usn', '', expires=time.time())
        self.redirect('/login')



settings = {
        "template_path": "views",  # 配置html文件路径
        "static_path": "statics",  # 配置静态文件路径
    }

# 路由映射
application = tornado.web.Application([
    (r"/index", MainHandler),
    (r"/login", LoginHandler),
    (r"/manager", ManagerHandler),
    (r"/logout", LogoutHandler)


], **settings)

# 启动
if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()


# session更灵活些
# set_secure_cookie有了加密，更安全