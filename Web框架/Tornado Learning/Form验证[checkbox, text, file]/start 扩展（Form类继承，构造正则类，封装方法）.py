import tornado.ioloop
import tornado.web
import re
import myuimethod

class IPField:
    REGULAR = "^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9]?[0-9])(\.(25[0-5]|2[0-4][0-9]|[0-1]?[0-9]?[0-9])){3}$"

    def __init__(self, error_dict=None, required=True):
        # 封装自定义错误信息，格式为错误类型-错误信息
        self.error_dict = {}
        if error_dict:
            self.error_dict.update(error_dict)
        self.required = required
        # 用于返回给check_valid函数，让其判断输入是否全部合法
        self.is_valid = False
        # 封装了用户输入的值
        self.value = None
        # 封装了具体的错误信息
        self.error = None

    def validate(self, name, user_value):
        # 传入参数：域名、用户输入值
        # 是否要求必须输入
        if not self.required:
            self.is_valid = True
            self.value = user_value
        else:
            # 输入是否为空
            if not user_value.strip():
                # 是否自定义了域不可为空的错误信息
                if self.error_dict.get("required", None):
                    self.error = self.error_dict['required']
                else:
                    self.error = "%s is required." % name
            else:
                match_obj = re.match(IPField.REGULAR, user_value)
                # 是否匹配成功
                if match_obj:
                    self.is_valid = True
                    self.value = match_obj.group()
                else:
                    # 是否定义了非法输入的错误信息
                    if self.error_dict.get('valid', None):
                        self.error = self.error_dict['valid']
                    else:
                        self.error = "%s is invalid." % name


class CheckboxField:
    def __init__(self, error_dict=None, required=True):
        self.error_dict = {}
        if error_dict:
            self.error_dict.update(error_dict)
        self.required = required
        self.is_valid = False
        self.value = None
        self.error = None

    def validate(self, name, user_value):
        """
        :param name: 域名 game
        :param user_value: 用户勾选的内容 形如[1,2,3]
        :return:
        """
        if not self.required:
            self.is_valid = True
            self.value = user_value
        else:
            if not user_value:
                if self.error_dict.get('required', None):
                    self.error = self.error_dict['required']
                else:
                    self.error = '%s is required.' % name
            else:
                self.is_valid = True
                self.value = user_value


class FileField:
    REGULAR = r'(\w+.jpg)|(\w+.jpeg)|(\w+.gif)|(\*+.png)'

    def __init__(self, error_dict=None, required=True):
        self.name = None
        self.error = None
        # 封装了符合规范的文件名
        self.value = []
        # 上传文件一项是否符合规范，默认为True，验证中一旦有不合法的地方就将其改为False
        self.is_valid = True
        self.required = required
        # 存储最终成功上传的文件路径
        self.success_file_list = []
        # 将错误信息封装在字典中
        self.error_dict = {}
        # 如果自定义了错误信息，则更新默认字典
        if error_dict:
            self.error_dict.update(error_dict)

    def validate(self, name, file_name_list):
        self.name = name
        # 根据文件上传是否必须，区分为两大场景
        if not self.required:
            self.is_valid = True
            # 所有合法的文件列表，文件可能有1个没有上传，也有可能文件后缀或大小不符合要求
            self.success_file_list = file_name_list
        else:
            # 要求上传文件却没有上传
            if not file_name_list:
                self.is_valid = False
                if self.error_dict.get('required', None):
                    self.error = self.error_dict['required']
                else:
                    self.error = 'Files not selected and uploaded.'
            else:
                for file_name in file_name_list:
                    # 文件是否符合规范
                    if not re.match(FileField.REGULAR, file_name):
                        self.is_valid = False
                        if self.error_dict.get('error', None):
                            self.error = self.error_dict['error']
                        else:
                            self.error = '%s is invalid' % file_name
                    else:
                        self.value.append(file_name)

    def save(self, files_obj, path=''):
        import os
        for file_obj in files_obj:
            file_name = file_obj['filename']
            full_file_name = os.path.join(path, file_name)
            print(full_file_name)
            # 文件名不为空你且文件名在合法文件列表中
            if file_name and file_name in self.value:
                self.success_file_list.append(full_file_name)
                with open(full_file_name, 'wb') as f:
                    f.write(file_obj['body'])


class BaseForm:
    def check_valid(self, handler):
        flag = True
        error_message_dict = {}
        success_dict = {}
        # Form类继承自BaseForm类，self.__dict__内封装了派生类的所有字段
        # key是字段名，regOBj则是对应的正则对象
        for key, regObj in self.__dict__.items():
            # key: 输入域
            if type(regObj) == CheckboxField:
                user_value = handler.get_arguments(key)
            elif type(regObj) == FileField:
                # form表单内有文件上传时，一定要将enctype属性设置为multipart/form-data,否则服务端收不到文件数据
                # files_obj是一个列表，元素是字典，有键filename和body，封装了文件名和文件内容
                files_obj = handler.request.files.get(key)
                user_value = []
                # 如果没有上传任何文件，files_obj将是NoneType无法迭代，迭代前需判断
                if files_obj:
                    for file in files_obj:
                        user_value.append(file['filename'])
            else:
                user_value = handler.get_argument(key)
            # 将验证过程放入对应域的正则对象中
            # 这样可以将不同的验证规则封装到不同的类中
            regObj.validate(key, user_value)
            # 验证信息封装在regObj中
            if regObj.is_valid:
                success_dict[key] = regObj.value
                regObj.save(files_obj)
            else:
                flag = False
                error_message_dict[key] = regObj.error
        return flag, success_dict, error_message_dict


class IndexForm(BaseForm):
    def __init__(self):
        self.ip = IPField(required=True)
        self.game = CheckboxField(required=True)
        self.files = FileField(required=True)


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html', error_message_dict={})

    def post(self):
        _formVali = IndexForm()
        flag, success_dict, error_message_dict = _formVali.check_valid(self)
        if flag:
            print('success', success_dict)
        else:
            print('error', error_message_dict)
            self.render('index.html', error_message_dict=error_message_dict)


settings = {
        "template_path": "views",  # 配置html文件路径
        "static_path": "statics",  # 配置静态文件路径
        "ui_methods": myuimethod   # 配置模板方法文件
    }


# 路由映射
application = tornado.web.Application([
    (r"/index", IndexHandler),
], **settings)

# 启动
if __name__ == "__main__":
    application.listen(8001)
    tornado.ioloop.IOLoop.instance().start()
