from threading import Thread, _active, _active_limbo_lock, _limbo, current_thread, main_thread
from time import sleep


def my_task(pt_thread: Thread):
    print('my_task',
          f'{_limbo=}',
          f'{_active=}',
          f'{pt_thread=}',
          f'ct={(ct := current_thread())}',
          f'currrent thread is main thread? {ct == main_thread()}',
          sep='\n\t')
    sleep(5)  # time.sleep blocks only the currrent thread, so the
    # main thread continues to execute and we come back to execute the next line
    # after 5 seconds
    not_main('my_task')

def not_main(caller):
    print('not_main',
          f'{caller=}',
          f'{_limbo=}',
          f'{_active=}',
          f'ct={(ct := current_thread())}',
          f'currrent thread is main thread? {ct == main_thread()}',
          sep='\n\t')

print('main',
      f'{_limbo=}',
      f'{_active=}',
      f'ct={(ct := current_thread())}',
      f'currrent thread is main thread? {ct == main_thread()}',
      sep='\n\t')

t = Thread(target=my_task, args=(ct,))  # Create thread
not_main('main')
t.start()  # Start `my_task`, the thread's activity
sleep(2)  # Prevent race condition
not_main('main')

"""
$ p3 thread_of_control.py
main
    _limbo={}
	_active={4369714624: <_MainThread(MainThread, started 4369714624)>}
	ct=<_MainThread(MainThread, started 4369714624)>
    currrent thread is main thread? True
not_main
	caller='main'
    _limbo={}
	_active={4369714624: <_MainThread(MainThread, started 4369714624)>}
	ct=<_MainThread(MainThread, started 4369714624)>
    currrent thread is main thread? True
my_task
    _limbo={}
	_active={4369714624: <_MainThread(MainThread, started 4369714624)>, 123145412456448: <Thread(Thread-1, started 123145412456448)>}
	pt_thread=<_MainThread(MainThread, started 4369714624)>
	ct=<Thread(Thread-1, started 123145412456448)>
    currrent thread is main thread? False
not_main
	caller='my_task'
    _limbo={}
	_active={4369714624: <_MainThread(MainThread, started 4369714624)>, 123145412456448: <Thread(Thread-1, started 123145412456448)>}
	ct=<Thread(Thread-1, started 123145412456448)>
    currrent thread is main thread? False
not_main
	caller='main'
    _limbo={}
	_active={4369714624: <_MainThread(MainThread, started 4369714624)>, 123145412456448: <Thread(Thread-1, started 123145412456448)>}
	ct=<_MainThread(MainThread, started 4369714624)>
    currrent thread is main thread? True

* Above, weirdy the last 'not_main' shows that 'Thread-1' is still active, even though we can see that
* Above that, 'Thread-1' already executed everything ('my_task', 'not_main' called by 'my_task') and
* should have exited. By adding a short sleep and running again, we see that this is just a race condition,
* will get the expected

not_main
	caller='main'
    _limbo={}
	_active={4514336192: <_MainThread(MainThread, started 4514336192)>}
	ct=<_MainThread(MainThread, started 4514336192)>
    currrent thread is main thread? True
"""
