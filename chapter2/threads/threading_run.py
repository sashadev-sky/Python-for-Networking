import threading


class MyThread(threading.Thread):

    def __init__(self, message):
        threading.Thread.__init__(self)
        self.message = message

    def run(self):
        print(self.message)


def test():
    for num in range(0, 10):
        thread = MyThread("I am the "+str(num)+" thread")
        thread.name = num
        thread.start()


if __name__ == '__main__':
    import timeit
    print(timeit.timeit("test()", setup="from __main__ import test", number=5))

"""
$ p3 threading_run.py
I am the 0 thread
I am the 1 thread
I am the 2 thread
I am the 3 thread
I am the 4 thread
I am the 5 thread
I am the 6 thread
I am the 7 thread
I am the 8 thread
I am the 9 thread
I am the 0 thread
I am the 1 thread
I am the 2 thread
I am the 3 thread
I am the 4 thread
I am the 5 thread
I am the 6 thread
I am the 7 thread
I am the 8 thread
I am the 9 thread
I am the 1 thread
I am the 0 thread
I am the 2 thread
I am the 4 thread
I am the 5 thread
I am the 3 thread
I am the 8 thread
I am the 9 thread
I am the 0 thread
I am the 6 thread
I am the 3 thread
I am the 4 thread
I am the 1 thread
I am the 7 thread
I am the 8 thread
I am the 7 thread
I am the 1 thread
I am the 2 thread
I am the 6 thread
I am the 5 thread
I am the 6 thread
I am the 9 thread
I am the 9 thread
0.0059691460000000016
I am the 3 thread
I am the 2 thread
I am the 8 thread
I am the 5 thread
I am the 4 thread
I am the 0 thread
I am the 7 thread
"""