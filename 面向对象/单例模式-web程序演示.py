# -*- coding:utf-8 -*-
#用python2.7执行
from wsgiref.simple_server import make_server

#数据库连接池中的类
class ConnectionPool():

    __instance = None

    def __init__(self):
        self.ip = '192,168,1,4'
        self.port = 8809
        self.pwd = '123456'
        self.username = 'xxx'
        #创建10个连接
        self.con_list = [1,2,3,4,5,6,7,8,9,10]

    #保证无论是多人还是单人访问都只创建一个实例
    @staticmethod
    def get_instance():
        if ConnectionPool.__instance:
            return ConnectionPool.__instance
        else:
            ConnectionPool.__instance = ConnectionPool()
            return ConnectionPool.__instance

    def get_connection(self):
        pass
        import random
        ran_con = random.randrange(1,11)
        return ran_con


def RunServer(environ,start_response):
    start_response(status='200 OK',headers =[('Content-Type', 'text/html')])
    url =  environ['PATH_INFO']
    if url.endswith('index'):
        ret = index()
        return ret
    elif url.endswith('new'):
        ret = new()
        return ret
    else:
        return '404'
    print('url')

def index():
    p = ConnectionPool()
    print(p)
    #普通模式：两次返回的对象地址不同，说明已经创建了多个实例
    return 'index'

def new():
    #单例模式创建一个对象
    p = ConnectionPool.get_instance()
    #每次返回的实例地址一样，说明只创建了一个实例，不同用户访问只使用一个实例。
    #当大量用户访问时，不会占用多份内存数据
    #所有用户都通过一个对象去访问
    con =  p.get_connection()
    print(p)
    return 'Line:' + str(con)

if __name__ ==  '__main__':
    httpd = make_server('', 8008, RunServer)
    print('Serving HTTP on port 8008...')
    #内部有wihle循环，监听用户访问请求
    httpd.serve_forever()
