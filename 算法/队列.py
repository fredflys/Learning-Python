class Queue:
    def __init__(self):
        self.__list = []

    def is_empty(self):
        return True if not len(self.__list) else False

    def enqueue(self, item):
        self.__list.append(item)

    def dequeue(self):
        self.__list.pop(0)

    def size(self):
        return len(self.__list)

