import logging

logging.basicConfig(filename='log.log',
                    format = '%(asctime)s - %(name)s - %(levelname)s - %(module)s': %(message)s',
                    datefmt = '%Y-%m-%d %H:%M:%S %p',
                    level = 10)

'''
CRITICAL = 50
FATAL = CRITICAL
ERROR = 40
WARNING = 30
WARN = WARNING
INFO = 20
DEBUG = 10
NOTSET = 0
'''
logging.error('error')
logging.log(40,'error')
####################################
#同时往多个日志文件中写数据
#创建文件
file_1_1 = logging.FileHandler('11_1.log','a')
#配置格式
fmt = logging.Formatter(fmt='%(asctime)s - %(name)s - %(levelname)s - %(module)s': %(message)s ')
#对文件应用格式
file_1_1.setFormatter(fmt)

#创建第二个文件
file_1_2 = logging.FileHandler('11_2.log','a')
fmt = logging.Formatter()
file_1_2.setFormatter(fmt) 

logger1 = logging.Logger('s1',level=logging.ERROR)
logger1.addHandler(file_1_1)
logger1.addHandler(file_1_2)
