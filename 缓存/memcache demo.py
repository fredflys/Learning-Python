# 内存存取数据快于硬盘，
# 持久化：数据写入硬盘
# 在数据库存取相对较慢耗时很久
# 将硬盘（数据库等）中最常用的数据，放入内存中预先开辟好的一部分区域
# 从而实现高速存取，就是缓存
# memcached -d -m 128 -p 2000 -u root -c 1024 -l 192.168.17.122 -P /tmp/memcached.pid -s /tmp/memcached.sock
#  -d 设置为守护进程
#  -m 设置内存大小(M)
#  -p 设置监听端口
#  -u 设置启动用户
#  -l 是监听的服务器IP地址
#  -c 选项是最大运行的并发连接数，默认是1024，按照你服务器的负载量来设定
# -P 是设置保存Memcache的pid文件
#   -s 设置套接口

'''
1、执行的命令
telnet 127.0.0.1 11211
2、报错提示
Trying 127.0.0.1...
telnet: connect to address 127.0.0.1: Connection refused
telnet: Unable to connect to remote host
3、/usr/bin/memcached -h
memcached 1.4.13（正常显示了对应的版本）
是什么原因导致不能连接到memcached服务呢，telnet的原因吗？
iptables没打开11211端口
已经找找到问题：
1、没有开启memcached服务
正解：/usr/bin/memcached -d -m 2048 -p 11211
2、注意port保持一致
telnet 127.0.0.1 11211
'''

import memcache
# 与服务器建立连接，到线上时debug参数一定要去掉
# 为什么是参数是一个列表？ 支持集群
# 如何判断设置的键值对放在哪台机器上？
# 将key进行位运算转换为数字，除以服务器个数，看余数
# 那不同机器的权重如何设置？让权重高的机器多出现几次（将要设置的服务器地址用元组包裹，第二个参数就是重复出现几次）
# 高可用：有一台机器静默地从工作机器上备份数据，如无哦工作机器挂掉，则备份机器自动顶上来，代替工作

mc = memcache.Client([('192.168.17.122:2000', 3),
                      '192.168.17.122:2001',
                      '192.168.17.122:2002',
                      ], debug=True)
# 设置键值对，并设置超时时间（可不设置）
# 存在则覆盖，不存在则新插入
mc.set('foo', 'bar', 5)
# 匹配设置，传入字典
mc.set_multi({})
mc.get('foo')
mc.get_multi([])
mc.delete()
mc.delete_multi([])

# 添加，如果已存在，则会抛出异常
mc.add('a', 'b')
# 替换，如果原没有，则会抛出异常
mc.replace('a', 'c')

# 在值后面添加或前面添加
mc.append('k1', 'after')
mc.prepend('k1', 'before')

# 自增，默认自增1
mc.incr('k1', 5)
mc.decr('k1', 6)

# gets, cas 防止脏数据
# 内部维护了一个计数器
