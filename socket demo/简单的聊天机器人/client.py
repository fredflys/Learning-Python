import socket

#建立socket对象
sk = socket.socket()
#连接服务端的socket对象
sk.connect(('127.0.0.1',9999,))
#接受服务端的信息,参数为可接收的最大字节数
recv_bytes = sk.recv(1024) #阻塞，等待着接受数据
recv_str = str(recv_bytes,encoding='utf-8')
print(recv_str)

while True:
    inp = input('请输入要发送的内容：')
    if inp == 'q':
        sk.sendall(bytes(inp,encoding='utf-8'))
        break
    else:
         sk.sendall(bytes(inp,encoding='utf-8'))
         recv_from_server = str(sk.recv(1024),encoding='utf-8')
         print(recv_from_server)
sk.close()

