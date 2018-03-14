from tornado import web
import tornado.ioloop


SESSIONS = {}


class Sessions(object):
    def __init__(self, handler, cookie_key):
        self.handler = handler
        self.user_key = None
        self.cookie_key = cookie_key

    @staticmethod
    def generate_random_str():
        import hashlib, time
        _en = hashlib.md5()
        _en.update(bytes(str(time.time()), encoding="utf-8"))
        return _en.hexdigest()

    def __setitem__(self, k, v):
        if not SESSIONS.get(self.user_key):
            self.user_key = Sessions.generate_random_str()
            SESSIONS[self.user_key] = {}
        SESSIONS[self.user_key][k] = v
        self.handler.set_cookie(self.cookie_key, self.user_key)

    def __getitem__(self, item):
        value = None
        _user_key = self.handler.get_cookie(self.cookie_key)
        if SESSIONS.get(_user_key):
            self.user_key = _user_key
            value = SESSIONS[self.user_key][item]
        return value


class BaseHandler(web.RequestHandler):
    def initialize(self):
        self.session = Sessions(self, 'steam')


class IndexHandler(BaseHandler):
    def get(self):
        if SESSIONS.get(self.get_cookie('steam')):
            self.redirect('/manager')
        else:
            # 判断用户登陆信息是否正确（这里作了简化，只判断了用户名）
            if self.get_argument('usn', None) in ['yeff', 'mike']:
                # session = Sessions(self, 'steam')
                self.session['isLogin'] = True
                self.session['name'] = 'Yifei Xu'
                self.session['age'] = '23'
                self.session['accountInfo'] = 'xyfst'
                self.write('登陆成功了哦@_@')
            else:
                self.write('请先登陆呦')


class ManagerHandler(BaseHandler):
    def get(self):
        _site_user_key = self.get_cookie(self.session.cookie_key)
        if not SESSIONS.get(_site_user_key):
            self.write('登陆信息已失效，请先登陆*。*')
        else:
            display_str = "Name:%s\tAge:%s\tAccount:%s" % (self.session['name'], self.session['age'], self.session['accountInfo'])
            self.write(display_str)


class LoginHandler(web.RequestHandler):
    def get(self):
        self.render('login.html', wrong_captcha='')


class CheckCodeHandler(BaseHandler):
    def get(self):
        # 生成图片并返回
        import io, check_code
        # 在内存中创建容器
        mstream = io.BytesIO()
        # 创建图片，并写入验证码
        img, code = check_code.create_validate_code()
        # 将图片写入都IO容器中
        img.save(mstream, "GIF")
        self.write(mstream.getvalue())
        # 为每个用户保存自己的验证码
        self.session['check_code'] = code


    def post(self):
        usn = self.get_argument('usn')
        pwd = self.get_argument('pwd')
        cap = self.get_argument('cap_code')
        check_code = self.session['check_code']
        wrong_captcha = '<a style="color:red;">验证码错误，请重新输入</a>'
        if cap.upper() == check_code.upper():
            self.write("Captcha is correct.")
        else:
            self.render("login.html", wrong_captcha=wrong_captcha)


class CsrfHandler(BaseHandler):
    def post(self):
        self.write('CSRF验证通过啦！')

class UploadHandler(BaseHandler):
    def post(self):
        files_info = self.request.files['Files']
        print(files_info)

settings = {
    "template_path": "views",
    "static_path": "statics",
    "cookie_secret": "salt",
    "xsrf_cookies": True
}

application = web.Application([
    (r"/index", IndexHandler),
    (r"/manager", ManagerHandler),
    (r"/login", LoginHandler),
    (r"/check_code", CheckCodeHandler),
    (r"/csrf", CsrfHandler),
    (r"/upload", UploadHandler),
], **settings)

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()