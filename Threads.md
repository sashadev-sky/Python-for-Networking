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