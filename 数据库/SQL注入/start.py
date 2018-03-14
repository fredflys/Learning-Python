import tornado.ioloop
import tornado.web
import pymysql


class LoginHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('index.html')

    def post(self, *args, **kwargs):
        usn = self.get_argument('username', None)
        pwd = self.get_argument('password', None)
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='db1')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        info_sql = "select username, password from users where username='%s' and password= '%s';" % (usn, pwd)
        # 如果用户输入 yeff'-- a
        # 在字符串拼接时，会多出一个引号，sql语句如下
        # select username, password from users where username = 'yeff' -- a' and password= '';
        # 相当于给用户输入加入了引号，截断了密码验证的sql，并加上了注释标记，将后半部分其屏蔽掉了
        # 使得只用用户名验证就可以通过检测
        # 还可以输入 abc' or 1=1 -- a
        # 这样人为添加永远为真的条件，用户名验证也跳过了
        print(info_sql)
        # 解决方法用execute()的方法传入参数
        cursor.execute('select username, password from users where username=%s and password= %s;', (usn, pwd))
        # 如果没有数据fetchone()方法会返回None
        result = cursor.fetchone()
        if result:
            self.write('登陆成功')
        else:
            self.write('登陆失败')


settings = {
    'template_path': 'tpl',
    'static_path': 'statics',

}

application = tornado.web.Application([
    (r'/index', LoginHandler)

], **settings)

if __name__ == '__main__':
    application.listen(8001)
    tornado.ioloop.IOLoop.instance().start()