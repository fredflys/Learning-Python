from concurrent.futures import ThreadPoolExecutor, wait, as_completed
import time

d = dict()
l = []
futs = []

def func(x, y, t):
    time.sleep(t)
    return x + y


def run():
    fut = pool.submit(func, 2, 3)
    fut.add_done_callback(result_handler)


def result_handler(fut):
    try:
        result = fut.result()
        print('Got: ', result)
    except Exception as e:
        print('Failed: %s: %s' % (type(e).__name__, e))


# pool = ThreadPoolExecutor(max_workers=8)
# fut = pool.submit(func, 2, 3)
# fut2 = pool.submit(func, 4, 5)
# fut3 = pool.submit(func, 6, 7)
# # fut.result()  # 执行后就可以取得值，但会阻塞主线程
# fut.add_done_callback(result_handler)  # 加上
# fut2.add_done_callback(result_handler)
# fut3.add_done_callback(result_handler)


with ThreadPoolExecutor(max_workers=8) as exec:
    start = time.time()
    for i in range(10):
        fut = exec.submit(func, i, i, i)
        # 每次得到一个future对象，就像列表中添加，因此是有序的，最后拿到的结果也是有序的
        futs.append(fut)
        fut.add_done_callback(result_handler)

print('---main thread---')
lst = [fut.done() for fut in futs]
print(lst)
