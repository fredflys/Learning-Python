import socket
import time


def nonblocking_way():
    sock = socket.socket()
    # 该socket上的阻塞调用都改为非阻塞
    sock.setblocking(False)
    try:
        # 连接时不再阻塞，connect()执行后立刻执行下面的语句
        # 在进行非阻塞连接时，系统底层还是会抛出异常
        sock.connect(('zh.moegirl.org', 80))
    except BlockingIOError:
        pass
    request = 'GET / HTTP/1.0\r\nHost:zh.moegirl.org\r\n\r\n'
    data = request.encode('utf-8')
    while True:
        try:
            # 连接时是非阻塞，因此send时并不知道连接是否已经就绪，就需要不断尝试
            # 非阻塞节省下的时间，只是在不断尝试读写socket，不停判断非阻塞调用的状态是否就绪
            # 还得处理来自底层的异常，也不能同时处理多个socket
            sock.send(data)
            break
        except OSError:
            pass

    response = b''
    while True:
        try:
            # 接收数据时不再阻塞
            chunk = sock.recv(4096)
            while chunk:
                response += chunk
                chunk = sock.recv(4096)
            break
        except OSError:
            pass
    return response


def sync_way():
    res = []
    for i in range(10):
        res.append(nonblocking_way())
    return len(res)


if __name__ == '__main__':
    start = time.time()
    sync_way()
    end = time.time()
    print('sync_way: ', end - start)