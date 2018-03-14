from models import chouti_orm
from backend.core.request_handler import BaseRequestHandler
from backend import commons
from backend.utils import message,check_code
import datetime
import json
import io


class CheckCodeHandler(BaseRequestHandler):
    def get(self, *args, **kwargs):
        stream = io.BytesIO()
        img, code = check_code.create_validate_code()
        img.save(stream, "png")
        self.session["CheckCode"] = code  #利用session保存验证码
        self.write(stream.getvalue())


class SendCodeHandler(BaseRequestHandler):
    def post(self, *args, **kwargs):
        ret = {'status': True, "data": "", "error": ""}
        email = self.get_argument('email', None)
        print(email)
        if email:
            code = commons.random_code()  # 获取随机验证码
            print(code)
            message.email([email, ], code)  # 发送验证码到邮箱
            conn = chouti_orm.session()  # 获取数据库session对象
            print('1')
            obj = chouti_orm.SendCode(email=email, code=code, stime=datetime.datetime.now())  # 写入数据库
            print('2')
            conn.add(obj)
            conn.commit()
        else:
            ret['status'] = False
            ret['error'] = "邮箱格式错误"

        self.write(json.dumps(ret))


class RegisterHandler(BaseRequestHandler):
    def post(self, *args, **kwargs):
        rep = BaseResponse()   #总的返回前端的类，包含是否注册成功的状态、错误信息
        form = account.RegisterForm()  #实例化RegisterForm
        if form.valid(self):  #调用baseform核心验证处理函数valid，返回是否验证成功
            current_date = datetime.datetime.now()
            limit_day = current_date - datetime.timedelta(minutes=1)
            conn = ORM.session()  #获取数据库session对象<br>　　　　　　　　#查看验证码是否过期
            is_valid_code = conn.query(ORM.SendMsg).filter(ORM.SendMsg.email == form._value_dict['email'],
                                                           ORM.SendMsg.code == form._value_dict['email_code'],
                                                           ORM.SendMsg.ctime > limit_day).count()
            if not is_valid_code:
                rep.message['email_code'] = '邮箱验证码不正确或过期'
                self.write(json.dumps(rep.__dict__))
                return
            has_exists_email = conn.query(ORM.UserInfo).filter(ORM.UserInfo.email == form._value_dict['email']).count()#邮箱是否存在
            if has_exists_email:
                rep.message['email'] = '邮箱已经存在'
                self.write(json.dumps(rep.__dict__))
                return
            has_exists_username = conn.query(ORM.UserInfo).filter(
                ORM.UserInfo.username == form._value_dict['username']).count() #用户名是否存在
            if has_exists_username:
                rep.message['email'] = '用户名已经存在'
                self.write(json.dumps(rep.__dict__))
                return<br>　　　　　　　　#按数据库表的列订制form._value_dict