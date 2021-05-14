from threading import Thread
from time import sleep

num_threads = 4


def thread_message(message):
	global num_threads
	num_threads -= 1
	print('Message from thread %s\n' % message)


while num_threads > 0:
	print("I am the %s thread" % num_threads)
	Thread(target=thread_message("I am the %s thread" % num_threads)).start()
	sleep(0.1)


"""
chapter2/threads$ p3 threads_init.py
I am the 4 thread
Message from thread I am the 4 thread

I am the 3 thread
Message from thread I am the 3 thread

I am the 2 thread
Message from thread I am the 2 thread

I am the 1 thread
Message from thread I am the 1 thread
"""
