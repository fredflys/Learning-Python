import sys
from modules import client

if __name__ ==  '__main__':
    #命令定义为-s address -p port,共有5个参数
    client.Clinet(sys.argv)
