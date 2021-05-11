import threading
import time

num_threads = 4


def thread_message(message):
	global num_threads
	num_threads -= 1
	print('Message from thread %s\n' % message)


while num_threads > 0:
	print("I am the %s thread" % num_threads)
	threading.Thread(target=thread_message("I am the %s thread" % num_threads)).start()
	time.sleep(0.1)


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

start(self)

|            Start the thread’s activity.

|            It must be called at most once per thread object. It arranges for the

|            object’s run() method to be invoked in a separate thread of control.

|            This method will raise a RuntimeError if called more than once on the

|            same thread object.
"""
