#python 3
from concurrent.futures import ThreadPoolExecutor as Executor
import threading


def view_thread_worker():
    print('Executing Thread')
    print(f'Accessing thread: {threading.get_ident()}')
    print(f'Thread Executed {threading.current_thread()}')


def main():
    with Executor(max_workers=3) as exe:
        print(exe)
        fut1 = exe.submit(view_thread_worker)
        fut2 = exe.submit(view_thread_worker)
        fut3 = exe.submit(view_thread_worker)


if __name__ == '__main__':
    main()

"""
Output order not guaranteed.

$ p3 thread_pool_concurrency.py
Executing Thread
Accessing thread: 123145323118592
Thread Executed <Thread(ThreadPoolExecutor-0_0, started 123145323118592)>
Executing Thread
Accessing thread: 123145323118592
Thread Executed <Thread(ThreadPoolExecutor-0_0, started 123145323118592)>
Executing Thread
Accessing thread: 123145323118592
Thread Executed <Thread(ThreadPoolExecutor-0_0, started 123145323118592)>
"""
