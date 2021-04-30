import threading


def my_task():
    print(f'Hello World: {threading.current_thread()}')

# We create our first thread and pass in our myTask function
my_first_thread = threading.Thread(target=my_task)
# We start out thread
my_first_thread.start()

"""
$ python3 threading_init.py
Hello World: <Thread(Thread-1, started 123145376243712)>
"""