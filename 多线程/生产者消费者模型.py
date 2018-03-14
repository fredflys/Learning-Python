import queue
import threading

message = queue.Queue(10)


def producer(i):
    while True:
        message.put(i)


def consumer(i):
    while True:
        msg = message.get()


for i in range(12):
    t = threading.Thread(target=producer,args=(i,))
    t.start()

for i in range(10):
    t = threading.Thread(target=consumer,args=(i,))
    t.start()
