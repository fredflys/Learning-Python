import socketserver
from modules import threading_socket_server

class ArgvHandler:

    def __init__(self,args):
        #args是列表
        self.args = args
        self.argv_parse()
    #解析命令
    def argv_parse(self):
        if len(self.args) < 1:
            self.help_msg()
        else:
            #sys.argv[0]是代码本身路径
            first_argv = self.argv[1]
            #反射，将字符串格式的命令反射到类中，查看是否有用户输入的方法
            if hasattr(self,first_argv):
                func = getattr(self,first_argv)
                func()
            #如果没有，弹出帮助信息
            else:
                self.help_msg()


    def help_msg(self):
        mas = '''
            start
            stop
        '''
        print(msg)

    #start只涉及懂启动服务端
    def start(self):
        try:
            print('正在启动中...')
            #启动server，则自动重写socketserver的handle方法
            server = socketserver.ThreadingTCPServer((settings.BIND_HOST,settings.BIND_PORT),threading_socket_server.MyTCPHandler)
        except KeyboardInterrupt:
            pass
