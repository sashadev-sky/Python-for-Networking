# Network Programming - Sockets

## Concepts

### Streams

* **Readable streams**: an abstraction for a *source* from which data is consumed
  * HTTP responses, on the client -> client reads HTTP responses from server
  * HTTP  requests,  on the server -> server reads HTTP requests from a client
  * `process.stdin`

* **Writable streams**: an abstraction for a destination to which data is written
  * HTTP responses, on the server -> server writes responses
  * HTTP requests, on the client  -> client writes requests
  * `process.stdout`

### HTTP/1.1 vs. HTTP/2

## Building an HTTP client

**HTTP clients test the response of a website or web service.**

Python offers a series of modules designed to create an HTTP client.

#### Main library modules

  1. **`http.client`**
  2. **`urllib.request`**: the recommended Python *std lib* package for **HTTP tasks**.
      * Simpler interface
      * The capacity to manage all tasks related to HTTP requests

#### Installables

1. **`requests`**: the recommended Python ecosystem package for **HTTP tasks**.
A wrapper of `urllib.request`, along with other Python modules to provide the REST structure with simple methods (so we have the `get`, `post`, `put`, `update`, `delete`, `head`, and `options` methods).
     * Unless you have a requirement to use `urllib`, recommend using `requests` for your projects in Python.
     * Does not yet support HTTP/2

1. **`httpx`**: recommended Python std lib package for **HTTP and asynchronous tasks** in Python 3.7.

    * Compatible with `requests` and with the version of the **HTTP/2 protocol, which offers a series of improvements at the performance level, such as the compression of the headers that are sent in the requests**.
    * Supports both versions HTTP/1.1 and HTTP/2.
    * For HTTP/2, just need to install the `http2` extension additionally: `$ pip3 install httpx[http2]`. The main difference between these two versions is that the HTTP/2 version is a protocol based on binary data instead of textual data.
    * HTTP/2 does not change the core semantics of the request or response, but does change the way data is transmitted from and to the server.
    * For **asynchronous programming support**, we can use with module that allows us to make many requests in parallel without blocking the rest of the operations.
      * **`asyncio`**: recommended module for this task.
      * **`trio`**
1. **`aiohttp`**: for managing asynchronous requests. **`asyncio`**-only.

## asyncio

---
Asynchronous IO Support.

**Write explicitly asynchronous, concurrent Python code.**

 `asyncio` offers a safer alternative to **preemptive multitasking** (**threading**) - it will be much easier for you to avoid race condition bugs with Asyncio.

 Also offers large-scale concurrency - provides a simple way to support thousands of simultaneous socket connections.

### Preface

---

### **Event loop**

The event loop is the core of every asyncio application. Event loops run asynchronous tasks and callbacks concurrently, perform network IO operations, and run subprocesses.

> Fundamentally, waits for some events to happen and executes handlers associated with those events. In the case of AsyncIO, these **handlers are coroutines**.

* They inherit from the `BaseEventLoop` abstract class, which contains several methods used to execute asynchronous code.

Application developers should typically use the high-level asyncio functions, such as **`asyncio.run()`**, and should rarely need to reference the loop object or call its methods.

### Coroutine

**Coroutines** are a more generalized form of **subroutines**

> **Subroutines** are entered at one point and exited at another point. **Coroutines** can be entered, exited, and resumed at many different points. They can be implemented with the **`async def`** statement.

```python
async def func_name() -> Coroutine:
```

### Low-level

---

* **[`get_event_loop()`](#get_event_loop)**

* **[`get_running_loop()`](#get_running_loop)**

### `get_event_loop`

```python
get_event_loop() -> AbstractEventLoop
```

Get the current event loop.

If there is no current event loop set in the current OS thread, the OS thread is main, and `set_event_loop()` has not yet been called, `asyncio` will create a new event loop and set it as the current one.

> Because this function has rather complex behavior (especially when custom event loop policies are in use), **`get_running_loop` is preferred for use with coroutines and callbacks**.

### `get_running_loop`

```python
get_running_loop() -> AbstractEventLoop
```

Return the running event loop in the current OS thread.

If there is no running event loop a `RuntimeError` is raised.

* **Note**: This function can only be called from a coroutine or a callback.

#### Running and Stopping the Loop

* **[`run_until_complete()`](#run_until_complete)**

* **[`run_forever()`](#run_forever)**

### `run_until_complete`

```python
run_until_complete(future: Awaitable)
```

Run until the future has completed.

If the argument is a **coroutine** object it is implicitly scheduled to run as a **`asyncio.Task`**:

1. task is created and the coroutine is associated with it.

### `run_forever`

```python
run_forever() -> None
```

Run the event loop until `stop()` is called.

If `stop()` is called while `run_forever()` is running, the loop will run the current batch of callbacks and then exit. Note that new callbacks scheduled by callbacks will not run in this case; instead, they will run the next time `run_forever()` or `run_until_complete()` is called.

### High-level

---

### `run`

```python
run(coro: Awaitable, *, debug: bool=False)
```

Runs the passed coroutine, taking care of managing the asyncio event loop, finalizing asynchronous generators, and closing the threadpool.

* Always creates a new event loop and closes it at the end.

> Should be used as a **main entry point for `asyncio` programs**, and should ideally only be called once.

### Running an `asyncio` Program

```python
import time, asyncio

async def wait(delay: int) -> Coroutine:
    print(f'wait for {delay} seconds at {time.strftime("%X")}')
    await asyncio.sleep(delay)
    print(f'waited for {delay} seconds at {time.strftime("%X")}')
```

Low-level

```python
loop = asyncio.get_event_loop()
loop.run_until_complete(wait(2))
```

High-level (Preferred)

```python
asyncio.run(wait(2))
```

```python
# wait for 2 seconds at 22:49:56
# waited for 2 seconds at 22:49:58
```
