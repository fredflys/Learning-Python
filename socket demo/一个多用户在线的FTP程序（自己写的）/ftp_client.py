import socket
import hashlib
import os
import sys

def Encryp(in_str):
    md5_obj = hashlib.md5()
    md5_obj.update(bytes(in_str,encoding='utf-8'))
    encrypted_result = md5_obj.hexdigest()
    return encrypted_result

def UploadFile(connection,file):
    file_size = os.stat(file).st_size
    print('文件大小为：' + str(file_size))
    sk.sendall(bytes(str(file_size),encoding='utf-8'))
    sk.sendall(bytes(file,encoding='utf-8'))
    validation_info = str(sk.recv(1024),encoding='utf-8')
    print(validation_info)

    sum = 0
    with open(file,'rb') as f:
        for line in f:
            sk.sendall(line)
            #进度显示效果
            sum += len(line)
            percent = sum/file_size
            sys.stdout.write('\r')
            sys.stdout.write('%s%%' % int(percent*100))
            sys.stdout.flush()
    print('\n客户端传输结束')
    print(str(sk.recv(1024),encoding='utf-8'))

sk = socket.socket()
sk.connect(('127.0.0.1',9999))

#recv-1:接收欢迎信息
print(str(sk.recv(1024),encoding='utf-8'))

def logon_registry():
    while True:
        choice = input('请选择您的操作：\n1.注册账户\n2.登陆账户\nq:退出\n>>>')
        if choice not in ['1','2','q']:
            print('命令未找到，请重新输入。')
        else:
            return choice


choice = logon_registry()
#send-1:发送选择的命令
sk.sendall(bytes(choice,encoding='utf-8'))


while True:
    if choice == '1':
        username = input('请输入您要注册的用户名:')
        password = input('请输入您的密码:')
        #send-2:发送注册用账户名
        sk.sendall(bytes(Encryp(username),encoding='utf-8'))
        #send-3:发送注册用密码
        sk.sendall(bytes(Encryp(password),encoding='utf-8'))
        print(str(sk.recv(1024),encoding='utf-8'))
        choice = logon_registry()

    elif choice == '2':
        username = input('请输入您的用户名:')
        password = input('请输入您的密码:')
        #send-2:发送登陆用账户名
        sk.sendall(bytes(Encryp(username),encoding='utf-8'))
        #send-3:发送登陆用密码
        sk.sendall(bytes(Encryp(password),encoding='utf-8'))
        #recv-2:接收验证反馈的信息
        logon_info = str(sk.recv(1024),encoding='utf-8')
        print(logon_info)
        if logon_info == '验证成功':
            while True:
                file = input('请输入要上传的文件名:\n')
                if os.path.exists(file):
                    UploadFile(sk,file)
                    break
                else:
                    print('文件未找到，请重新输入文件名。')
                    continue
        else:
            #验证失败，则继续登陆界面的循环
            choice = '2'



    elif choice == 'q':
        sk.close()
        break


