from threading import Thread
import time

def my_counter():
    i = 0
    time.sleep(1)
    for _ in range(100000000000000000000):
        i = i + 1
        return True

def main():
    thread_array = {}
    start_time = time.time()

    for _ in range(2):
        t =  Thread(target=my_counter)
        t.start()
        thread_array[_] = t

    for _ in range(2):
        thread_array[_].join()
        end_time = time.time()
        print('Total time: {}'.format(end_time-start_time))

if __name__ == '__main__':
    main()

