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
        # 创建随机字符串
        # 创建自己的箱子
        # 在箱子中放入信息对
        # 在客户端中放入箱子的钥匙

        # 如果服务端还没有钥匙，先制作一个钥匙，并创建一个对应的箱子
        if not SESSIONS.get(self.user_key):
            self.user_key = Sessions.generate_random_str()
            SESSIONS[self.user_key] = {}
        # 起初/manager页面无论如何都无法进入，想了很久
        # 这个点费了我不少时间才找到：这边对SESSIONS中是否存在钥匙没有判断，使得每次set方法清空钥匙对应的箱子
        SESSIONS[self.user_key][k] = v
        self.handler.set_cookie(self.cookie_key, self.user_key)

    def __getitem__(self, item):
        # 获取客户端递来的钥匙
        # 看看房间里有对应钥匙吗
        # 用钥匙打开箱子，获得信息对，取出值
        # 没有钥匙返回None
        value = None
        _user_key = self.handler.get_cookie(self.cookie_key)
        if SESSIONS.get(_user_key):
            self.user_key = _user_key
            value = SESSIONS[self.user_key][item]
        return value


# IndexHandler和ManagerHandler都继承这个类
# tornado为我们留的钩子，使用继承RequestHandler的类并初始化时（执行__init__方法），会在最后执行 self.initialize(**kwargs)
# 我们可以自己定义initialize的函数内容，以实现不同的效果
# 这里我们是初始化了服务端的Sessions类，继承之后，两个类就不用自己再初始化了，更简洁一些
class BaseHandler(web.RequestHandler):
    def initialize(self):
        self.session = Sessions(self, 'steam')


# tornado内部通过反射调用get和post方法
# obj = IndexxHandler()
# func = getattr(obj, "get")
# func()
class IndexHandler(BaseHandler):
    def get(self):
        # 如果客户端有对应的钥匙则转到manager页面尝试匹配
        if SESSIONS.get(self.get_cookie('steam')):
            self.redirect('/manager')
        # 注意这里的多层嵌套
        # 第一次我将两个if写在了同级，但在执行了redirect函数后，还是会接着执行下面判断中的else块
        # 虽不至于中止程序，但会报错，所以这里写成了两层嵌套
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
        # session = Sessions(self, 'steam')

        # 从客户端拿来钥匙
        # 看看服务端的房间里有钥匙吗
        # 有则取出对应的信息对
        _site_user_key = self.get_cookie(self.session.cookie_key)
        if not SESSIONS.get(_site_user_key):
            self.write('登陆信息已失效，请先登陆*。*')
        else:
            display_str = "Name:%s\tAge:%s\tAccount:%s" % (self.session['name'], self.session['age'], self.session['accountInfo'])
            self.write(display_str)


settings = {
    "template_path": "views",
    "static_path": "statics",
}

application = web.Application([
    (r"/index", IndexHandler),
    (r"/manager", ManagerHandler),
], **settings)

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()