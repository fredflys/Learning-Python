import pymysql

# 创建连接
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='db1')

# 创建游标，并定义游标返回值为字典类型，这样就可以报错列名
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

# 获取受影响的行数
effected_rows = cursor.execute("select * from tb1;")
cursor.execute("insert into tb1(nid,name,mail) values(%s,%s,%s);", (4, 'linda', '3@qq.com'))
# 必须要commit才能使改动生效
conn.commit()
# 新增数据后获取主键ID
print(cursor.lastrowid)


# 游标中此时存储有select语句返回的结果，通过fetchall方法可取出
r1 = cursor.fetchall()

# 获取一条数据，其内部是生成器，移动指针并获取数据，没有数据时，返回None
r2 = cursor.fetchone()

# 获取n条数据，原理同fetchone一次获取若干条
r3 = cursor.fetchmany(3)

# 移动游标指针，可选相对和绝对模式
cursor.scroll(-1, mode='relative')


# 执行存储过程,自动忽略out参数
cursor.callproc('proc_1', (1, 2, 3))
# 存储过程的查询结果，即过程中select语句的返回结果
result = cursor.fetchall()
# 专门获取存储过程的返回值, @_后写上存储过程的名字， @_procname_后再跟上参数的序号，从0开始
cursor.execute("select @_proc_1_0, @_proc_1_1, @_proc_1_2;")
# 存储过程的返回值
ret_vals = cursor.fetchone()
print(result)
print(ret_vals)