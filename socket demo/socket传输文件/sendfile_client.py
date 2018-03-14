import socket
import os
import sys


sk = socket.socket()
sk.connect(('127.0.0.1',9999,))

recv_bytes = sk.recv(1024)
recv_str = str(recv_bytes,encoding='utf-8')
print(recv_str)

# 发送当前文件大小，以便服务端判断何时接收完成
# 利用os模块获取文件大小
file_size = os.stat('file.PNG').st_size
print(file_size)
# bytes方法只能转换字符串类型，因此要将文件大小转为字符串
sk.sendall(bytes(str(file_size),encoding='utf-8'))

# 解决粘包问题（在发送文件前再进行一次通信）
validation_info = sk.recv(1024)
print(str(validation_info,encoding='utf-8'))
sum = 0
with open('file.PNG','rb') as f:
    for line in f:
        sk.sendall(line)
        # 进度显示效果
        sum += len(line)
        percent = sum/file_size
        sys.stdout.write('\r')
        sys.stdout.write('%s%%' % int(percent*100))
        sys.stdout.flush()
print('\n传输结束')
sk.close()
