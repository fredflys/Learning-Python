from threading import Thread
import time

def my_calc(i):
    i = i * i
    i = abs(i)
def my_counter():
    i = 0
    time.sleep(1)
    #对i累加1亿次
    for _ in range(100000000000000000000):
        i = my_calc(i)
        return True

def main():
    thread_array = {}
    start_time = time.time()
    for _ in range(2):
        t = Thread(target=my_counter)
        t.start()
        t.join()
        end_time = time.time()
        print('Total time: {}'.format(end_time-start_time))

if __name__ == '__main__':
    main()
