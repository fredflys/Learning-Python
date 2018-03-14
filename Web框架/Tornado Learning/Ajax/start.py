import tornado.ioloop
import tornado.web
import json

UPLOADS = []


class LoginHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('login.html')

    def post(self):
        dic = {"status": True, "message": ""}
        usn = self.get_argument("username")
        pwd = self.get_argument("password")
        if usn == 'abc' and pwd == '123':
            pass
        else:
            dic["status"] = False
            dic["message"] = "用户名或密码错误"
        self.write(json.dumps(dic))


class JqueryLoginHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('jquerylogin.html')

    def post(self):
        dic = {"status": True, "message": "登陆成功"}
        usn = self.get_argument("username")
        pwd = self.get_argument("password")
        if usn == 'abc' and pwd == '123':
            pass
        else:
            dic["status"] = False
            dic["message"] = "用户名或密码错误"
        self.write(json.dumps(dic))


# 伪Ajax请求的实现
class SudoHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("sudo-ajax.html")


# form表单传输数据和上传文件
class FormHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('form.html', server_files='')

    def post(self):
        # 获取checkbox的value值
        checked = self.get_arguments('games')
        # request中封装了所有客户端传来的信息,get_argument方法内部也是调用request来实现
        # 通过参数获得上传文件的元信息
        # files_meta是一个列表，但只能通过迭代的方式访问，因为其内部是通过yield定义的
        files_meta = self.request.files['upload_files']
        for file in files_meta:
            # 每个file都是一个tornado.httputil.HTTPFile对象，其中封装了上传文件的各类信息
            # class HTTPFile(tornado.util.ObjectDict)
            # |  Represents a file uploaded via a form.
            # |  For backwards compatibility, its instance attributes are also accessible as dictionary keys.
            file_name = file['filename']
            # 新建一个文件句柄
            # 并在内存中新建一个文件名为上传文件名（并加上路径）的文件
            with open(".\\statics\\uploads\\" + file_name, 'wb') as f:
                # 用body键获取上传文件的内容
                # 写入文件内容，并关闭文件句柄
                f.write(file['body'])
            UPLOADS.append(file_name)
            print(UPLOADS)
        # self.write('文件已上传成功')
        self.render('form.html', server_files=UPLOADS)

settings = {
        "template_path": "views",  # 配置html文件路径
        "static_path": "statics",  # 配置静态文件路径
    }


# 路由映射
application = tornado.web.Application([
    (r"/login", LoginHandler),
    (r"/jquerylogin", JqueryLoginHandler),
    (r"/sudo", SudoHandler),
    (r'/form', FormHandler),
], **settings)

# 启动
if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()

