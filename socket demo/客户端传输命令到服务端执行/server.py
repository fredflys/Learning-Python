#客户端执行命令后的结果可能超过一次可传输的大小，客户端要循环进行接收
import socketserver
import subprocess

class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            connection = self.request
            connection.sendall(bytes('欢迎登陆',encoding='utf-8'))
            while True:
                try:
                    client_bytes = connection.recv(1024)
                except Exception as e:
                    print (e)
                client_str = str(client_bytes,encoding='utf-8')
                print(client_str)
                func,command = client_str.split('|',1)
                result_str = subprocess.getoutput(command)
                print(result_str)
                result_bytes = bytes(result_str,encoding='utf-8')
                info_str ="info|%d"%len(result_bytes)
                connection.sendall(bytes(info_str,encoding='utf-8'))
                connection.sendall(result_bytes)

if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(('127.0.0.1',9088),MyServer)
    server.serve_forever()

#ThreadingTCPServer -> ThreadingMixIn, TCPServer
    #TCPServer -> TCPServer.__init__
        #TCPServer.__init__ -> BaseServer.__init__
            #BaseServer.__init__-> self.server_address = ()
            #                   -> self.RequestHandlerClass = MyServer
        #                   -> self.socket
        #                   -> self.server_bind()
        #                   -> self.server_activate() [listen]
#serve_forever -> BaseServer
