import threading
from thread_worker import ThreadWorker


def main():
    # This initializes ''thread'' as an instance of our Thread Worker
   thread = ThreadWorker()
   # This is the code needed to run our created thread
   thread.start()


if __name__ == "__main__":
	main()

"""
$ p3 main.py
0
1
2
3
4
5
6
7
8
9
"""