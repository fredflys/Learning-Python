#先进先出,指定最大个数，可等可不等（get，get_nowait)
#FIFO
import queue

q = queue.Queue(maxsize=10)
#如果插入数达到上限，会造成阻塞
for i in range(11):
    q.put(i)

while not q.empty():
    print(q.get())
