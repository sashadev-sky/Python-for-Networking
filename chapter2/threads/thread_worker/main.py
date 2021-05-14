from thread_worker import ThreadWorker


def main():
   t = ThreadWorker()  # initializes 'thread' as an instance of our ThreadWorker
   t.start()   # run our created thread


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
