import socketserver

class MyServer(socketserver.BaseRequestHandler):

if __name__ == '__main__':
    # socket demo + select + 多线程
    # 创建ip，端口和类名
    # 带有括号，因此找ThreadingTCPServer的构造方法__init__
    # 继承自ThreadingMixIn, TCPServer
    # ThreadingMixIn中有process_request_threa，dprocess_request两个方法,但没有__init__
    # 在TCPServer中找到，看其形参->server_address,RequestHandlerClass,MyServer => RequestHandlerClass
    # obj = RequestHandlerClass()
    # obj.handle()
    # 接着看语句，首先执行了父类的构造方法 BaseServer  __init__
    # obj = self.RequestHandlerClass()
    # ThreadingTCPServer.__init__ => TCPServer.__init__ => BaseServer.__init__
    server = socketserver.ThreadingTCPServer(('127.0.0.1',8009),MyServer)
    server.serve_forever()

