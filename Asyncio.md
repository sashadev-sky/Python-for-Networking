# Asyncio

Asyncio is the Python asynchronous API

> "The central focus of Asyncio is on how best to perform multiple tasks at the same time—and not just any tasks, but specifically **tasks that involve waiting periods**. The key insight required with this style of programming is that while you wait for this task to complete, work on other tasks can be performed."

**Concurrent programming** using an **event-based programming model**.

* Note: **Threading** is also concurrent programming, but has a [different model](./Threads.md).

> **Think: Multithreading is about *workers*, Asynchronous is about *tasks*.**

## What Problem Is Asyncio Trying to Solve?

**For I/O-bound workloads, there are exactly (only!) two reasons to use async-based concurrency over thread-based concurrency:**

1. Asyncio offers a safer alternative to **preemptive multitasking** (i.e., using threads), thereby avoiding the bugs, race conditions, and other nondeterministic dangers that frequently occur in nontrivial threaded applications.

2. **Large-scale concurrency:** Asyncio offers a simple way to support many thousands of *simultaneous* socket connections, including being able to handle many long-lived connections for newer technologies like WebSockets, or MQTT for Internet of Things (IoT) applications.

That’s it.

### Threading

> "Threading—as a programming model—is best suited to certain kinds of **computational tasks that are best executed with multiple CPUs and shared memory for efficient communication between the threads**. In such tasks, the use of multicore processing with shared memory is a necessary evil because the problem domain requires it.
>
> **Network programming is not one of those domains**.

### Network programming

> "The key insight is that network programming involves a great deal of “waiting for things to happen,” and because of this, we don’t need the operating system to efficiently distribute our tasks over multiple CPUs. Furthermore, we don’t need the risks that preemptive multitasking brings, such as race conditions when working with shared memory."

## Misconceptions

---

1. *Asyncio will make my code blazing fast.*

---
Unfortunately, no. In fact, **threading solutions benchmark slightly faster than their comparable Asyncio solutions**.

If the extent of concurrency itself is considered a performance metric, Asyncio does make it a bit easier to create very large numbers of concurrent socket connections, though. Operating systems often have limits on how many threads can be created, and this number is significantly lower than the number of socket connections that can be made.  The OS limits can be changed, but it is certainly easier to do with Asyncio.

And **while we expect that having many thousands of threads should incur extra context-switching costs that coroutines avoid, it turns out to be difficult to benchmark this in practice.**

No, speed is not the benefit of Asyncio in Python; if that’s what you’re after, try Cython instead!

---

2. *Asyncio makes threading redundant.*

---
Definitely not! The true value of threading lies in being able to write multi-CPU programs, in which different computational tasks can share memory. The numerical library `numpy`, for instance, already makes use of this by speeding up certain matrix calculations through the use of multiple CPUs, even though all the memory is shared.

**For sheer performance, there is no competitor to this programming model for CPU-bound computation.**

---

3. *Asyncio removes the problems with the GIL.*

---

**Global Interpreter Lock** (**GIL**)

> Makes the Python interpreter code (not your code!) thread-safe by locking the processing of each opcode; it has the unfortunate side effect of effectively pinning the execution of the interpreter to a single CPU, and thus preventing multicore parallelism.

Again, no. It is true that Asyncio is not affected by the GIL, but this is only because the GIL affects multithreaded programs. The “problems” with the GIL that people refer to occur because it prevents true multicore parallelism when using threads. **Since Asyncio is single-threaded (almost by definition), it is unaffected by the GIL, but it cannot benefit from multiple CPU cores either**.

> 'This is similar to why JavaScript lacks a GIL "problem”: there is only one thread.'

---

4. *Asyncio prevents all race conditions.*

---
False. **The possibility of race conditions is always present with any concurrent programming, regardless of whether threading or event-based programming is used**.

It is true that Asyncio can virtually eliminate a certain *class* of race conditions common in multithreaded programs, such as intra-process shared memory access. However, it doesn’t eliminate the possibility of other kinds of race conditions, such as the interprocess races with shared resources common in distributed microservices architectures. You must still pay attention to how shared resources are being used.

**The main advantage of Asyncio over threaded code is that the points at which control of execution is transferred between coroutines are visible (because of the presence of `await` keywords)**, and thus it is much easier to reason about how shared resources are being accessed.
