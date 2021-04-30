#python 3
from concurrent.futures import ThreadPoolExecutor
import threading


def view_thread():
    print("Executing Thread")
    print("Accessing thread : {}".format(threading.get_ident()))
    print("Thread Executed {}".format(threading.current_thread()))


def main():
    executor = ThreadPoolExecutor(max_workers=3)
    thread1 = executor.submit(view_thread)
    thread1 = executor.submit(view_thread)
    thread3 = executor.submit(view_thread)


if __name__ == '__main__':
    main()

"""
$ p3 thread_pool_concurrency.py
Executing Thread
Accessing thread : 123145323118592
Thread Executed <Thread(ThreadPoolExecutor-0_0, started 123145323118592)>
Executing Thread
Accessing thread : 123145323118592
Thread Executed <Thread(ThreadPoolExecutor-0_0, started 123145323118592)>
Executing Thread
Accessing thread : 123145323118592
Thread Executed <Thread(ThreadPoolExecutor-0_0, started 123145323118592)>
"""