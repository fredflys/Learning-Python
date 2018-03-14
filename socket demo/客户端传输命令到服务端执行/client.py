import socket

sk = socket.socket()
sk.connect(('127.0.0.1',9088))

while True:
    print(str(sk.recv(1024),encoding='utf-8'))
    inp = input("请输入要执行的命令种类和命令(格式为 种类|名称：").strip()
    if inp.startswith('cmd'):
         sk.sendall(bytes(inp,encoding='utf-8'))
         basic_info_str = str(sk.recv(1024),encoding='utf-8')
         print(basic_info_str)
         result_length = int(basic_info_str.split('|')[-1])

         print(result_length)
         has_received = 0
         content_bytes = bytes()
         while has_received < result_length:
             fetched_bytes = sk.recv(1024)
             has_received += len(fetched_bytes)
             #类型相同才可以做加法，所以上面初始化时要用bytes()，而非0
             content_bytes += fetched_bytes
         cmd_result = str(content_bytes,encoding='utf-8')
         print(cmd_result)
