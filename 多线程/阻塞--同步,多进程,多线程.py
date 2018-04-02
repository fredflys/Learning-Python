import socket
import time


def blocking_way():
    sock = socket.socket()
    # blocking
    # 连接速度不是取决于程序，而与网络环境和服务端处理能力有关，因此是阻塞的
    sock.connect((r'zh.moegirl.org', 80))
    # 请求方法 URL 协议版本\r\n  --请求行
    # 头部字段名:值\r\n
    # \r\n
    # 请求数据
    request = 'GET / HTTP/1.0\r\nHost:zh.moegirl.org\r\n\r\n'
    sock.send(request.encode('utf-8'))
    response = b''
    chunk = sock.recv(4096)
    while chunk:
        response += chunk
        # blocking
        # 同上
        chunk = sock.recv(4096)
    return response


def sync_way():
    res = []
    for i in range(10):
        res.append(blocking_way())
    return len(res)


def process_way():
    from concurrent import futures
    workers = 10
    with futures.ProcessPoolExecutor(workers) as executor:
        futs = {executor.submit(blocking_way) for i in range(10)}
    return len([fut.result() for fut in futs])


def thread_way():
    from concurrent import futures
    workers = 10
    with futures.ThreadPoolExecutor(workers) as executor:
        futs = {executor.submit(blocking_way) for i in range(10)}
    return len([fut.result() for fut in futs])


if __name__ == '__main__':
    start = time.time()
    sync_way()
    end = time.time()
    print('sync_way: ', end - start)

    start = time.time()
    process_way()
    end = time.time()
    print('process_way: ', end - start)

    start = time.time()
    thread_way()
    end = time.time()
    print('thread_way: ', end - start)