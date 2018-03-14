import socket

# 创建socket对象
sk = socket.socket()
# 把socket对象绑定到地址和端口上
sk.bind(('127.0.0.1',9999,))
# 开始监听请求
sk.listen(5)

while True:
    connection,address = sk.accept()
    connection.sendall(bytes('欢迎',encoding='utf-8'))

    # 解决粘包问题
    connection.sendall(bytes('已收到文件大小信息，开始传输...',encoding='utf-8'))

    # 接收到的文件大小
    file_size = str(connection.recv(1024),encoding='utf-8')
    print(file_size)
    # 文件大小转为int
    total_size = int(file_size)
    # 将已经接收的文件大小设为0，用于下面循环中的判断
    has_recv = 0
    # 打开文件句柄，准备写入文件
    f = open('new.png','wb')
    # 接收文件大小，然后开始接收文件
    while True:
        # 如果接收到的文件尺寸等于文件总尺寸，则不再接收
        if total_size == has_recv:
            break
        data = connection.recv(1024)
        f.write(data)
        # 每次接收文件后，都对已接收文件大小进行累加
        has_recv += len(data)
    f.close()
