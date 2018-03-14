import socket


sk = socket.socket()
sk.connect((
    '127.0.0.1',8001
    ))
#print(str(sk.recv(1024),encoding='utf-8'))
while True:
    inp = input('>>>')
    sk.sendall(bytes(inp,encoding='utf-8'))
    print(str(sk.recv(1024),encoding='utf-8'))
