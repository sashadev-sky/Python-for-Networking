# Threads

> "Threads are a feature provided by an operating system (OS), made available to software developers so that they may indicate to the OS which parts of their program may be run in parallel. The OS decides how to share CPU resources with each of the parts, much as the OS decides to share CPU resources with all the other different programs (processes) running at the same time."

**Standard multithreading model**: preemptive concurrency with shared memory

Asyncio is offered as an alternative to threading, so it’s hard to understand the value proposition without some comparison; and even when using Asyncio, you will still likely have to deal with threads and processes, so you need to know something about threading.

#### WARNING

> The context of this discussion is **exclusively concurrency in network programming applications**. Preemptive multithreading is also used in other domains, where the trade-offs are entirely different.

#### Benefits of Threading

1. *Ease of reading code*

2. *Parallelism with shared memory*: your code can exploit multiple CPUs while still having threads share memory. This is important in many workloads where it would be too costly to move large amounts of data between the separate memory spaces of different processes, for example.

3. *Know-how and existing code*: there is a large body of knowledge and best practices available for writing threaded applications. There is also a huge amount of existing “blocking” code that depends on multithreading for concurrent operation.

### Best practice for threading

Use the **`ThreadPoolExecutor`** class from the **`concurrent.futures`** module, passing all required data in through the **`submit()`** method.

```python
from concurrent.futures import ThreadPoolExecutor as Executor

def worker(data):
    # process the data
with Executor(max_workers=10) as exe:
    future = exe.submit(worker, data)
```

You can convert the pool of threads into a pool of subprocesses simply by using **`ProcessPoolExecutor`** instead.

In general, you’ll prefer your tasks to be somewhat short-lived, so that when your program needs to shut down, you can simply call `Executor.shutdown(wait=True)` and wait a second or two to allow the executor to complete.

**Most importantly**: if at all possible, you should **try to prevent your threaded code** (in the preceding example, the `worker()` function) **from accessing or writing to any global variables!**

## Drawbacks of Threading

1. *Threading is difficult*: threading bugs and race conditions in threaded programs are the hardest kinds of bugs to fix.

"**Unnecessarily enormous non-determinism**"
> Nontrivial multithreaded programs are incomprehensible to humans. It is true that the programming model can be improved... however, these techniques merely chip away at the **unnecessarily enormous non-determinism of the threading model. The model remains intrinsically intractable.**

And directly from the Mac Developer Library’s [Concurrency Programming Guide](https://developer.apple.com/library/archive/documentation/General/Conceptual/ConcurrencyProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40008091)
> "In the past, introducing concurrency to an application required the creation of one or more additional threads. Unfortunately, writing threaded code is challenging. Threads are a low-level tool that must be managed manually. **Given that the optimal number of threads for an application can change dynamically based on the current system load and the underlying hardware, implementing a correct threading solution becomes extremely difficult, if not impossible to achieve**. In addition, the synchronization mechanisms typically used with threads add complexity and risk to software designs without any guarantees of improved performance."

2. *Threads are resource-intensive*

3. *Threading can affect throughput*: at very high concurrency levels (say, >5,000 threads), there can also be an impact on throughput due to context-switching costs, assuming you can figure out how to configure your operating system to even allow you to create that many threads!

4. *Threading is inflexible*: the operating system will continually share CPU time with all threads regardless of whether a thread is ready to do work or not. For instance, a thread may be waiting for data on a socket, but the OS scheduler may still switch to and from that thread thousands of times before any actual work needs to be done. (In the async world, the `select()` system call is used to check whether a socket-awaiting coroutine needs a turn; if not, that coroutine isn’t even woken up, avoiding any switching costs completely.)

### "Tasks" - a more Asyncio approach:

> "Both OS X and iOS adopt a more asynchronous approach to the execution of concurrent tasks than is traditionally found in thread-based systems and applications. Rather than creating threads directly, applications **need only define specific tasks and then let the system perform them. By letting the system manage the threads, applications gain a level of scalability not possible with raw threads**. Application developers also gain a simpler and more efficient programming model."
>
> Mac Developer Library’s [Concurrency Programming Guide](https://developer.apple.com/library/archive/documentation/General/Conceptual/ConcurrencyProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40008091)

# Threading API

Python's built-in `threading` module

## Methods

* [**`current_thread()`**](#current_thread)

* [**`main_thread()`**](#main_thread)

### `current_thread`

```python
current_thread() -> Thread
"""Return the current Thread object, corresponding to the caller's
thread of control.

If the caller's thread of control was not created through the threading module, a dummy thread object with limited functionality is returned.
"""
```

*Source code*

```python
try:
    return _active[get_ident()]
except KeyError:
    return _DummyThread()
```

The default thread is the **`_MainThread`** (**`main_thread()`**). You can see this with the **`_active`** global, which returns a dictionary of active threads mapped to their identifiers.

```python
from threading import _active, current_thread, main_thread

print(_active)  # {4369714624: <_MainThread(MainThread, started 4369714624)>}
```

Called outside a thread activity, `current_thread()` returns `MainThread`:

```python
print((ct := current_thread()))  # <_MainThread(MainThread, started 4369714624)>
print(f'currrent thread is main thread? {ct == main_thread()}')  # True
```

From inside, it will be the **controlling thread** (the thread whose activity it is).

See **[thread_of_control.py](./chapter2/threads/thread_of_control.py)**

### `main_thread`

```python
main_thread() -> (_MainThread | Any)
"""Return the main thread object.

In normal conditions, the main thread is the thread from which the
Python interpreter was started.
"""
```


## Creating a thread

Using the **`threading.Thread()`** constructor

* [**`Thread()`**](#Thread)

* [**`start()`**](#start)

Or by subclassing

* [**`start()`**](#start)

* [**`run()`**](#run)

---

**The chain of events is always new `Thread` -> `start()` -> `run()` -> *`_target()`***

---

### `Thread`

```python
Thread(
    group=None,
    target: Optional[Callable] = None,
    name: Optional[str] = None,
    args: tuple=(),
    kwargs: Optional[dict] = None,
    *,
    daemon=None
) -> Thread
"""A class that represents a thread of control.

:param group: should be None; reserved for future extension when
              a ThreadGroup class is implemented.

:param target: is the callable object to be invoked by run()

:param name: thread name. By default, a unique name "Thread-N"
             where N is a small decimal number.

:param args: argument tuple for the target invocation.

:param kwargs: dictionary of keyword arguments for the target invocation
"""
```

* **Note**: this constructor should always be called with keyword arguments.

### `start`

```python
start() -> None
"""Start the thread's activity

Arranges for the object's run() method to be invoked in a separate
thread of control.

:raise: RuntimeError if called more than once on the same thread object
"""
```

When a thread is "started", a few things happen under the hood:

1. It gets assigned an identifier (**`self._ident`**), which can tell it apart from other active threads (`current_thread()`)

2. It recieves a **`_tstate_lock`** which is `locked`.

3. The internal flag is set to true for the started `Event`, awakening the thread

4. **`run()`** is invoked

    * The thread exits when:
      1. The function returns; the return value is ignored.
      2. Unhandled exception is raised; a stack trace will be printed unless the exception is `SystemExit`.

5. It is deactived (**`del _active[self.get_ident()]`**)

---

### Implementation: **`threading.Thread()`**

Ex. at the most basic level, initing a thread:

```python
from threading import Thread

def my_task(msg): print(msg)  # hey

t = Thread(target=my_task, args=('hey',))  # Create thread
t.start()  # Start `my_task`, the thread's activity, pass 'hey'
```

---

### `run`

```python
run() -> None
"""Method representing the thread's activity.

You may override this method in a subclass. The standard run()
method invokes the callable passed to the object's constructor
as the target argument, if any, with the args and kwargs arguments.
"""
```

*Source code*

```python
try:
    if self._target:
        self._target(*self._args, **self._kwargs)
finally:
    # Avoid a refcycle if the thread is running a function with
    # an argument that has a member that points to the thread.
    del self._target, self._args, self._kwargs
```

## Subclassing

`Thread` can be subclassed

* Create a new class inheriting from **`threading.Thread`**

* If override the constructor, make sure to invoke the base class constructor (**`threading.Thread.__init__(self)`**) FIRST before doing anything else to the thread. You can pass any additional arguments accepted by [`Thread()`](#Thread).

* Overriding **`run()`** in a subclass is an alternative to using `target` to specify the thread's activity.

---

### Implementation: subclassing

```python
from threading import Thread

class MyThread(Thread):
    def __init__(self, message):
        Thread.__init__(self, args=(message,))
        self.message = message

    def run(self): print(self.message)


def test():
    for num in range(0, 10):
        t = MyThread(f'thread {num}')
        t.start()

if __name__ == '__main__':
    test()
```

---

## Joining a thread

* **`join()`**

### `join`

```python
join(timeout: float=None) -> None
"""Wait until the thread terminates.

This blocks the calling thread until the thread whose join() method is
called terminates -- either normally or through an unhandled exception
or until the optional timeout occurs.

:param timeout: if using a timeout, you must call is_alive() after
                join() to decide whether a timeout happened -- if the
                thread is still alive, the join() call timed out.
:raise: RuntimeError if attempt to join the current thread
        (deadlock) or a thread that has not yet been started.
```

* **Note**: a thread can be `join()`ed many times.

Once the threads start, the current program (main thread) also keeps on executing. In order to prevent the main program from completing its execution until the thread execution is complete, we use the `join()` method.
