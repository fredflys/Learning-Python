import tornado.ioloop
import tornado.web


class MainForm(object):
    # MainForm类的字段就是要匹配的输入域，值是匹配模式
    # 其中对checkbox和files两个域，暂时简单地用判断列表有无元素进行检测
    def __init__(self):
        # 匹配IP地址这里折腾了很久，一致尝试使用命名分组，却一直无法成功，
        # 不懂怎么回事，不想再看正则这一部分了，先放一放
        # 注意尖角号和美元符的作用：匹配字符串开头和结尾的位置
        # match从头匹配，没有则None，search则是匹配到
        self.ip = "^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9]?[0-9])(\.(25[0-5]|2[0-4][0-9]|[0-1]?[0-9]?[0-9])){3}$"
        self.email = "^\w+@\w+\.\w+"
        self.phone = "1[3|7|5|8]\d{8}"
        self.game = []
        self.files = []

    def check_valid(self, handler):
        import re
        # 获取了对象的所有字段，形式是一个字典，键值分别是字段和字段的值
        form_dict = self.__dict__
        flag = True
        # 用户输入的值也储存在一个字典中
        user_dict = {}
        # 这里我们迭代form_dict的所有元素
        for key, pattern in form_dict.items():
            if key == 'game':
                user_value = handler.get_arguments(key)
                is_valid = False if not user_value else True
            elif key == 'files':
                user_value = handler.request.files.get(key)
                is_valid = False if not user_value else True
            else:
                user_value = handler.get_argument(key)
                is_valid = re.match(pattern, user_value)
            if not is_valid:
                flag = False
            user_dict[key] = user_value
        return flag, user_dict


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')

    def post(self):
        # 用户提交数据后，会生成一个MainForm()对象
        _formVali = MainForm()
        flag, user_inputs = _formVali.check_valid(self)
        print(flag, user_inputs)


settings = {
        "template_path": "views",  # 配置html文件路径
        "static_path": "statics",  # 配置静态文件路径
    }

# 路由映射
application = tornado.web.Application([
    (r"/index", IndexHandler),
], **settings)

# 启动
if __name__ == "__main__":
    application.listen(8001)
    tornado.ioloop.IOLoop.instance().start()
