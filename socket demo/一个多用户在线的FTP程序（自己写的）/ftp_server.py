'''
用户信息md5加密传输
允许多用户同时登陆
执行命令
上传文件：传输过程显示进度条，支持断点续传
'''
import socketserver
import pickle


def CreateAccount(connection,username,password):
    with open('user_accounts','rb') as f:
        users_dict = pickle.load(f)
    users_dict[username] = password
    with open('user_accounts','wb')  as f:
        pickle.dump(users_dict,f)
    # send-3:注册信息确认
    connection.sendall(bytes('注册成功',encoding='utf-8'))


def LogonCheck(connection,username,password):
    with open('user_accounts','rb') as f:
        users_dict = pickle.load(f)
        if users_dict.__contains__(username):
            if users_dict[username] == password:
                # send-2:发送验证反馈的信息
                connection.sendall(bytes('验证成功',encoding='utf-8'))
                return True
            else:
                # send-2:发送验证反馈的信息
                connection.sendall(bytes('密码错误',encoding='utf-8'))
                return False
        else:
            # send-2:发送验证反馈的信息
            connection.sendall(bytes('用户不存在',encoding='utf-8'))
            return False


def RecvUpload(connection,username):
    import os
    file_size = int(str(connection.recv(1024),encoding='utf-8'))
    file_name = str(connection.recv(1024),encoding='utf-8')

    # 如果用户文件夹已创建则不再创建
    try:
        os.mkdir(username)
    except FileExistsError:
        pass

    # 避免粘包，再进行一次通信，使得文件信息和文件内容分开传输
    connection.sendall(bytes('服务器已收到文件大小信息，开始传输...',encoding='utf-8'))

    has_recv = 0
    new_file = open(os.path.dirname(__file__) + '\\' + username + '\\' + file_name,'wb')
    while True:
        if has_recv == file_size:
            break
        data = connection.recv(1024)
        new_file.write(data)
        has_recv += len(data)
    new_file.close()
    connection.sendall(bytes('服务器传输完成',encoding='utf-8'))


class MyServer(socketserver.BaseRequestHandler):

    def handle(self):
        connection = self.request
        # send-1：发送欢迎信息
        connection.sendall(bytes('欢迎来到本服务器\n---------------------',encoding='utf-8'))

        # recv-1:接收客户端的命令【注册与登陆】
        account_option = connection.recv(1024)
        if account_option == bytes('1',encoding='utf-8'):
            # recv-2:接收注册用账户名
            username = str(connection.recv(1024),encoding='utf-8')
            # recv-3:接收注册用密码
            password = str(connection.recv(1024),encoding='utf-8')
            CreateAccount(connection,username,password)
        elif account_option == bytes('2',encoding='utf-8'):
            # 避免第二次登陆不成功时，会跳出该选项内的语句，断开连接并报错
            while True:
                # recv-2:接收登陆用户名
                username = str(connection.recv(1024),encoding='utf-8')
                # recv-3:接收登陆密码
                password = str(connection.recv(1024),encoding='utf-8')
                logon_result = LogonCheck(connection,username,password)
                # 只有在确实登陆成功后，再返回False，跳出while循环，否则一直重复该循环
                if logon_result:
                    RecvUpload(connection,username)
                    return False
        else:
            connection.close()


if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(('127.0.0.1',9999),MyServer)
    server.serve_forever()





