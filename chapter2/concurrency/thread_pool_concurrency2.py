from concurrent.futures import ThreadPoolExecutor as Executor


def message(message):
 print(f'Processing {message}')

def main():
    print('Starting ThreadPoolExecutor')
    with Executor(max_workers=2) as exe:
        fut1 = exe.submit(message, ('message 1'))
        fut2 = exe.submit(message, ('message 2'))
    print('All tasks complete')


if __name__ == '__main__':
 main()

"""
$ p3 thread_pool_concurrency2.py
Starting ThreadPoolExecutor
Processing message 1
Processing message 2
All tasks complete
"""
