import multiprocessing
from multiprocessing import Process


def f(name):
    print('hello', name)


if __name__ == '__main__':
    # 指定调用对象，以及实参
    p = Process(target=f, args='y')
    p.start()
    p.join()


