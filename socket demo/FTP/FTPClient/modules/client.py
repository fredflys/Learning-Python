import os,sys
import socket
import socketserver
import json
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class Client:
    def __init__(self,sys_argv):
        self.USER_HOME = '%s/var/users' % BASE_DIR
        self.args = sys_argv
        self.argv_parse()
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

    #解析命令，命令定义为-s address -p port,共有5个参数
    def argv_parse(self):
        if len(self.args) < 5:
            self.help_mag()
            sys.exit()
        else:
            #如果没缺少-p或-s的任意一个，就提示帮助信息
            mandatory_fields = ['-p','-s']
            for i in mandatory_fields:
                if i not in self.args:
                    self.help_msg()
                    sys.exit('')
            try:
                #根据-s的索引，取到IP地址
                self.ftp_host = self.args[self.args.index('-s') + 1]
                #根据-p的索引，取到端口号
                self.ftp_port = int(self.args[self.args.index('-p') + 1])
                #如果有5个参数，但没有按照预定格式输入，同样跳出帮助信息
            except (IndexError,ValueError):
                self.help_msg()
                sys.exit()

        self.handle()
    def handle(self):
        self.connect(self.ftp_host,self.ftp_port)
        if self.auth():
            self.interactive()
    def current_dir(self,cwd):
        return '/'.join(cwd) + '/'

#验证成功后，用户的上传下载等操作在这个方法中实现
    def interactive(self):
        self.logout_flag = False
        while self.logout_flag is not True:
            user_input = nput('[%s]:%s' % (self.login_user,self.current_dir(self.cwd))).strip()
            if len(user_input) == 0: continue
            #返回标志位
            status,user_input_instructions = self.parse_instruction(user_input)
            if status is True:
                func = getattr(self,'instruction_'+user_input_instructions[0])
                func(user_input_instructions)
            else:
                print('Invalid instruction.')








    def connect(self,host,port):
        try:
            self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            self.sock.connect((host,port))
        except socket.error as e:
            sys.exit("连接服务端失败：%s" % e)

    def get_response_code(self,response):
        #服务发来的相应信息是response|code的格式，因此用split方法取出code部分
        response_code = response.split('|')
        code = response_code[1]
        return code

    def parse_instruction(self,user_input):
        user_input_to_list =user_input.split()
        func_str = user_input_to_list[0]
        if hasattr(self,'instrction_' + func_str):
            return True,user_input_to_list
        else:
            return False,user_input_to_list

    def instruction_ls(self,instructions):
        self.sock.send(("ls|%s" % json.dumps({})).encode())
        server_response = self.sock.recv(1024)
        print(str(server_response,'utf-8'))

    def auth(self):\
        #给用户三次尝试的机会
        retry_count = 0
        while retry_count < 3:
            username = input('请输入用户名:')
            if len(username) == 0:continue
            password = input('请输入密码:')
            if len(password) == 0:continue
            md5 = hahslib.md5()
            md5.update(password.encode())
            auth_str = 'user_auth|%' % (json.dumps({'username':username,'password':md5.hexdigest()}))
            self.sock.send(auth_str.encode())
            server_response  = self.sock.recv(1024)
            response_code = self.get_response_code(server_response)
            if response_code == '200':
                self.login_user = username
                #
                self.cwd = ['']
                try:
                    os.makedirs('%s%s' % (self,USER_HOME,self.login_user))
                #如果已经创建则跳过这一步
                except OSError:
                    print('hhh')

                return True
            else:
                retry_count+=1
        else:
            sys.exit('登陆次数已经超过最大限制')

