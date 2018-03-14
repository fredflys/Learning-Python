# 主要应用了文件指针和文件大小
# 个人想到：如果文件名一样而文件不同，可能会导致上传后的文件无法读取。可添加MD5校验。虽然我是没实现啦。
import socket
import os

# 获取程序所在的绝对路径
BASE_DIR = os.path.abspath(__file__)

sk = socket.socket()
sk.bind(('127.0.0.1',8001))
sk.listen(5)

while True:
    connection,address = sk.accept()
    connection.sendall(bytes('欢迎登陆文件服务器',encoding='utf-8'))
    Flag = True
    while Flag:
        #接收文件信息
        post_info = str(connection.recv(),encoding='utf-8')
        func,file_name,file_size,target_path = post_info.split('|',3)
        file_size = int(file_size)
        path = os.path.join(home,file_name)

        #开始接收客户端传输的文件
        has_received = 0
            #文件是否已经上传过，有则可选择进行断点传输，否则直接传输
        if os.path.exists(path):
            connection.sendall(bytes('检测到有曾经上传的同名文件',encoding='utf-8'))
            #用户选择是否断点续传，接收用户的选择
            if_resume = str(connection.recv(1024),encoding='utf-8')
            if if_resume == 'resume':
                recvd_file_size = os.stat(path).st_size
                connection.sendall(bytes(recvd_file_size,encoding='utf-8'))\
                file_obj = open(path,'ab')
                has_received += recvd_file_size
                while has_received < file_size:
                    try:
                        data = connection.recv(1024)
                        #强制关闭时，会报错或客户端发送值为空
                        #发送值为空的情况
                        if not data:
                            raise Exception
                    except Exception:
                        flag = False
                        break
            else:
                f = open(path,'wb')
        else:
            connection.sendall(bytes('文件未存在，直接开始上传...',encoding='utf-8'))
            f = open(path,'wb')

