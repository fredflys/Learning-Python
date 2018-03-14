#个人想到的：用布尔表达式一定要注意要比较双方的数据类型，否则会抛出错误
import socket
import os
import re


def progress_bar(num=1,sum=100):
    rate = float(num)/float(sum)
    temp = '\r%d%%' % (int(rate * 100),)
    sys.stdout.write(temp)
    sys.stdout.flush()


sk = socket.socket()
sk.connect((
    '127.0.0.1',8001
))
print(str(sk.recv(1024),encoding='utf-8'))

while True:
    # 输入格式为：post|文件路径 上传的目标路径
    inp = input('请输入文件名：').strip()
    # 获取文件大小和文件名.并传送给服务端
    func,file_path = inp.split('|',1)
    local_path,target_path = re.split('\s*', file_path,1)
    file_size = os.stat(local_path).st_size
    file_name = os.path.basename(local_path)
    post_info = 'post|%s|%s|%s' % (file_name,file_size,target_path)
    sk.sendall(bytes(post_info, encoding='utf-8'))

    # 开始传输文件内容
    # 服务端判断文件是否存在，接收结果
    if_exist_result = str(sk.recv(1024), encoding='utf-8')
    has_sent = 0
    if if_exist_result == '检测到有曾经上传的同名文件':
        inp = input('文件已存在，是否进行续传：Y/N\n>>>').strip()
        if inp == 'Y' or inp == 'n':
            # 等待服务端返回已上传的文件大小
            sk.sendall(bytes('resume', encoding='utf-8'))
            # 既是已经上传的文件大小，也是续传时指针应该移动到的目标位置
            has_sent = int(str(sk.recv(1024), encoding='utf-8'))
            print('已经上传了%s') % (str(has_sent/int(file_size)) + '%',)

            file_obj = open(local_path,'rb')
            file_obj.seek(has_sent)
            while has_sent < file_size:
                data = file_obj.read(1024)
                sk.sendall(data)
                has_sent += len(data)
                # 加上进度条效果
                progress_bar(has_sent,file_size)
            file_obj.close()
            print('上传成功')
