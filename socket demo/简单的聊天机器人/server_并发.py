import socketserver

class MyServer(socketserver.BaseRequestHandler):

    def handle(self):
        connection = self.request
        connection.sendall(bytes('欢迎光临', encoding='utf-8'))
        while True:
            recv_bytes = connection.recv(1024)
            recv_str = str(recv_bytes,encoding='utf-8')
            if recv_str == 'q':
                break
            connection.sendall(bytes(recv_str+' 已收到', encoding='utf-8'))
        print(address,connection)

if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(('127.0.0.1',9999),MyServer)
    server.serve_forever()  # 内部是while循环,自动执行类中的handle方法
