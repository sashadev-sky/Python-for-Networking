from concurrent.futures import ThreadPoolExecutor


def message(message):
 print(f'Processing {message}')

def main():
 print("Starting ThreadPoolExecutor")
 with ThreadPoolExecutor(max_workers=2) as executor:
   executor.submit(message, ('message 1'))
   executor.submit(message, ('message 2'))
 print("All tasks complete")


if __name__ == '__main__':
 main()

"""
$ p3 thread_pool_concurrency2.py
Starting ThreadPoolExecutor
Processing message 1
Processing message 2
All tasks complete
"""