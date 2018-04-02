import socket
from selectors import DefaultSelector, EVENT_READ, EVENT_WRITE

selector = DefaultSelector()  # 该模块是对底层select/poll/epoll，会根据os自动选择最优的模块
stopped = False
urls_todo = {'/', '/1', '/2', '/3', '/4', '/5', '/6', '/7', '/8', '/9'}


class Crawler:
    def __init__(self, url):
        self.url = url
        self.sock = None
        self.response = b''

    def fetch(self):
        self.sock = socket.socket()
        self.sock.setblocking(False)
        try:
            self.sock.connect(('zh.moegirl.org', 80))
        except BlockingIOError:
            pass
        # EVENT_WRITE值为2
        selector.register(self.sock.fileno(), EVENT_WRITE, self.connected)

    def connected(self, key, mask):
        selector.unregister(key.fd)
        get = 'GET {0} HTTP/1.0\r\nHost: zh.moegirl.org\r\n\r\n'.format(self.url)
        self.sock.send(get.encode('utf-8'))
        # EVENT_READ值为1
        selector.register(key.fd, EVENT_READ, self.read_response)

    def read_response(self, key, mask):
        global stopped

        chunk = self.sock.recv(4096)
        if chunk:
            self.response += chunk
        else:
            selector.unregister(key.fd)
            urls_todo.remove(self.url)
            if not urls_todo:
                stopped = True


def event_loop():
    while not stopped:
        # 阻塞调用，直到有事件发生
        # 用于选择满足我们监听的event的文件对象
        # 返回值是(key,events)的元组
        # key是SelectorKey的实例，events就是event mask（EVENT_READ或EVENT_WRITE或二者组合
        events = selector.select()
        for event_key, event_mask in events:
            # 这里callback可能是connected方法或者read_response方法
            callback = event_key.data
            callback(event_key, event_mask)


if __name__ == '__main__':
    import time
    start = time.time()
    for url in urls_todo:
        crawler = Crawler(url)
        crawler.fetch()
    event_loop()
    end = time.time()
    print('unblocking_epoll: ', end-start)