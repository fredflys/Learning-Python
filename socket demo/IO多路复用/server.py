#实际应用中并不会去写socket
#但有助于深入理解socket的源码
import socket

sk1 = socket.socket()
sk1.bind((
    '127.0.0.1',8001
))
sk1.listen()

sk2 = socket.socket()
sk2.bind((
    '127.0.0.1',8002
))
sk2.listen()


sk3 = socket.socket()
sk3.bind((
    '127.0.0.1',8003
))
sk3.listen()
# #如此创建两个端口无法实现
#一个while循环监听一个端口，堵住了后面的接口持续监听
# while True:
#     conn,address =sk1.accept()
#     while True:
#         content_bytes = conn.recv(1024)
#         content_str = str(content_bytes,encoding='utf-8')
#         conn.sendall(bytes(content_str + '已收到',encoding='utf-8')
#     conn.close()


#用于读取消息
inputs = [sk1,sk2,sk3,]
#存放谁给我发送过消息（存放发送者）
outputs = []
#存放谁给我发送了什么消息（存放发送内容）
message_dict = {}
import select
while True:
    #inputs,自动监听sk1,sk2,sk3,一旦某个对象发生变化，就会感知到
    #如有人连接sk1，r_list = sk1
    #1表示最多等待1秒，如果超时，就会执行下一句
    #第二个参数是传入的对象原封不动地传入其中
    #第三个参数是当对象发生错误时，就将其放入期中

    #select内部自动监听socket对象，一旦socket有变化，就会感知到
    #伪造出同时处理多人连接的能力，但实际仍是一个一个处理
    #其实是好比同时有多部电话，客户端拨过来时都接起，但仍只有一个人在操作
    #有客户说话，就立刻赶过去回答
    r_list,w_list,e_list = select.select(inputs,outputs,[],1)
    print('正在监听的socket对象:%d' % len(inputs))
    print(r_list)
    for sk_or_conn in r_list:
        #如果有人第一次连接，sk1发生变化
        #每一个连接对象
        #有新用户连接:
        if sk_or_conn == sk1:
            conn,address = sk_or_conn.accept()
            inputs.append(conn)
            #为第一次连接的用户先在字典中创建一个键位，存储一个空列表，有消息后都存储在列表中
            message_dict[conn] = []
        else:
            #有老用户发消息了
            try:
                data_in_bytes = sk_or_conn.recv(1024)
            except Exception as e:
                inputs.remove(sk_or_conn)
            else:
                #用户正常发送消息
                data_in_str = str(data_in_bytes,encoding='utf-8')
                #用户发来的消息存放在已经创建的列表中
                message_dict[sk_or_conn].append(data_in_str)
                # sk_or_conn.sendall(bytes(data_in_str+'好',encoding='utf-8'))
                outputs.append(sk_or_conn)

    #w_list仅仅保存了谁给我发的消息
    #用于读写分离
    #w_list只用于发送信息
    for conn in w_list:
        #取出消息列表中的数据
        recv_str = message_dict[conn][0]
        #取到数据后，再从列表中删除，下一次再取时，避免重复读取
        #如不删除，只会一直取到第一次存储的数据
        #可用queue进行优化（先进先出）
        del message_dict[conn][0]
        conn.sendall(bytes(recv_str + '  已经收到',encoding='utf-8'))
        outputs.remove(conn)


    for sk in e_list:
        inputs.remove(sk)

