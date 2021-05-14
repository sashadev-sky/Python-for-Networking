from threading import Thread


class ThreadingJoin(Thread):

    def __init__(self, message):
        Thread.__init__(self)
        self.message = message

    def run(self): print(self.message)


threads = []


def test():
    for num in range(0, 10):
        t = ThreadingJoin(f'I am the {num} thread')
        t.start()
        threads.append(t)
    # Wait for all threads to complete by entering them
    for thread in threads:
        thread.join()


if __name__ == '__main__':
    import timeit
    print(timeit.timeit("test()", setup="from __main__ import test", number=5))


"""
$ p3 threading_join.py
I am the 0 thread
I am the 1 thread
I am the 2 thread
I am the 3 thread
I am the 4 thread
I am the 5 thread
I am the 6 thread
I am the 8 thread
I am the 7 thread
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
I am the 5 thread
I am the 4 thread
I am the 7 thread
I am the 8 thread
I am the 6 thread
I am the 9 thread
I am the 0 thread
I am the 1 thread
I am the 2 thread
I am the 4 thread
I am the 5 thread
I am the 3 thread
I am the 8 thread
I am the 7 thread
I am the 6 thread
I am the 9 thread
0.006161209999999993

The main thread in the previous code does not finish its execution
before the child process, which could result in some platforms
terminating the child process before the execution is finished.
The join method may take as a parameter a floating-point number
that indicates the maximum number of seconds to wait.
"""
