from tornado import web
import tornado.ioloop
import time
import hashlib

sessions = {}

# 可以注意到在用了session后，每次重启客户端后，用户拿着cookie也是没有办法登陆的
# 因为客户端这边的sessions中的内容被清空了，好比用户手里虽然还有钥匙（cookie键值对）
# 但服务端的箱子已经没有了
# 当然sessions可以放在数据库/文件/缓存中，而不是存储在内存中
# cookie是否使用完全看服务端的需求：只要将对应user的islogin信息换成False即可
# 通过在服务端和cookie间多添加一层抽象，既便于存储大量信息，也提升了安全性


class IndexHandler(web.RequestHandler):
    def get(self):
        if self.get_argument('usn', None) in ['yeff', 'mike']:
            _en = hashlib.md5()
            _en.update(bytes(str(time.time()), encoding="utf-8"))
            user_key = _en.hexdigest()
            sessions[user_key] = {}
            sessions[user_key]['name'] = 'Yifei Xu'
            sessions[user_key]['age'] = '23'
            sessions[user_key]['accountInfo'] = 'xyfst'
            sessions[user_key]['isLogin'] = True
            self.set_cookie(name='steam', value=user_key)
            self.write('登陆成功了哦@_@')
        else:
            self.write('请登陆-_-')


class ManagerHandler(web.RequestHandler):
    def get(self):
        user_key = self.get_cookie(name='steam')
        user_info = sessions.get(user_key)
        if not user_info:
            self.redirect("/index")
        else:
            if user_info.get('isLogin'):
                display_str = "Name:%s\tAge:%s\tAccount:%s" % (user_info.get('name'), user_info.get('age'), user_info.get('accountInfo'))
                self.write(display_str)
            else:
                self.write("登陆信息已失效，得重新登陆啦*_*")


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