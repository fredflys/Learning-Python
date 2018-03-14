class ConnectionPool():

    __instance = None

    def __init__(self):
        self.ip = '192,168,1,4'
        self.port = 8809
        self.pwd = '123456'
        self.username = 'xxx'
        # 创建10个连接
        self.con_list = [1,2,3,4,5,6,7,8,9,10]

    # 保证无论是多人还是单人访问都只创建一个实例
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

for i in range(10):
    pool = ConnectionPool.get_instance()
    print('去连接池',pool,'中获取一个连接')
    con = pool.get_connection()
    print('获取到的连接是：',con)
