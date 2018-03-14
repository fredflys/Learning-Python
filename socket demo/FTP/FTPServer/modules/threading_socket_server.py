#重写类的方法都在这个文件中，也就是需求实现都在这个文件中
import socketserver
import json
from conf import settings
from modules import user
import hashlib
import subprocess

class MyTCPHandler(socketserver.BaseRequestHandler):
    response_code_list = {
        '200':'验证通过',
        '201':'用户或密码不正确',
        '300':'准备好向客户端发送文件',
        '301':'客户端已准备好接受文件',
        '302':'文件不存在',
        '2002':'可以开始上传文件',
        '2003':'文件已存在',
        '2004':'继续上传',
    }

    #重写handle方法
    def handle(self):
        while True:
            data = self.request.recv(1024).decode()
            print('已经收到数据:',data)
            if not data:
                print('用户已断开连接')
                break
            self.instruction_distributor(data)

    def instruction_distributor(self,instructions):
        print('in1',instructions)
        instructions = instructions.split('|')
        print('in2',instructions)

        function_str = instructions[0]
        if hasattr(self,function_str):
            func = getattr(self,function_str)
            func(instructions[1])
        else:
            print('无效的用户指令')

    def calculate_storage(self):
        self.login_user.used_storage = 0

    def ls(self,user_data):
        directory_path = '%s\%s%s' % (settings.USER_HOME, self.login_user.username,'\\'.join(self           ))

    def user_auth(self,data):
        auth_info = json.loads(data)
        #用户是否存在
        if auth_info['username'] in settings.USER_ACCOUNT:
            #密码是否正确
            if settings.USER_ACCOUNT[auth_info['username']['password'] == auth_info['password']:
                #实例化一个用户对象
                self.login_user = user.User(auth_info['username'],settings.USER_ACCOUNT[auth_info['username']])
                #验证成功，返回提示信息
                response_code = '200'
        else:
            response_code = '201'
        #将返回信息发出
        self.request.sendall('response|{0}',format(response_code).encode())
