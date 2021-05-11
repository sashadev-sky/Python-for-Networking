# Network Programming

## Concepts

### TCP vs. HTTP

>TCP is to HTTP as gasoline is to cars.

Ex. while i'm on stackoverflow in my browser and run `$ netstat`:

```bash
Proto Recv-Q Send-Q  Local Address          Foreign Address        (state)
tcp4       0      0  locals-mbp.fios-.60919 stackoverflow.co.https ESTABLISHED
```

### TCP/IP Ports

On a TCP/IP network every device must have an IP address.

Just as the IP address identifies the computer, the network **port** identifies the **application or service** running on the computer.

> The use of **ports allow computers/devices to run multiple services/applications**.

### TCP Sockets

**Sockets** are the main components that allow us to exploit the capabilities of the operating system to interact with the network.

A **network socket** is one endpoint of a two-way communication link between two programs (**process**) running on the network. A socket is **bound to a port number** so that the **TCP layer** can identify the application that data is destined to be sent to.

> #### `IP Address + Port number = Socket` (socket address)

#### Client-server Architecture

A central server provides services to a set of machines that connect to it.

**One socket on a host binds to an IP and a unique port number for each connection.**

![socket on a webserver](./socket_on_a_webserver.jpg)

#### Concurrency

> A **socket** is *identified* by a **`local address + remote address`** (**socket pair** tuple).
>
A server may create several **concurrently established TCP sockets** with the same **local port number** and **local IP address**, each mapped to its own server-child process, serving its own client process. They are treated as different sockets by the operating system since the **remote socket address** (the **client IP address** and **client port number**) is different.

While the original socket continues to listen for incoming connections (status: LISTEN), a new socket with same local address is created to communicate with each accepted connection (status: ESTABLISHED).

### "Client" socket vs. "server" socket

* **“client” socket** - an endpoint of a conversation. (ESTABLISHED)

* **“server” socket** - more like a switchboard operator. (LISTEN)
  * Formally called a **passive** socket

* The **client application** (your browser, for example) **uses “client” sockets exclusively**.
  * It will be implemented as a Python **`socket` client** that **`connect`** s to a remote host, **`send`** s it a request or command and **`recv`** s the response data.

* The **web server** it’s talking to **uses both “server” sockets and “client” sockets**.

  * It will be implemented as a Python **`socket` server** that starts a web server process at a local address to `listen` for incoming connections and create unique, dedicated sockets to handle them in 1. A new child process or 2. A new processing thread.

* **local address**: for both "server" and "client" sockets refers to **whatever is listening** for connections on your machine (**loopback interface** web server (`127.0.0.1:xxxx`, `0.0.0.0:xxxx`) for a socket server or **internal ip** (`192.168.x.xxx:xxxxx`) for a socket client.

* **remote address**: "server" sockets don't have a remote address because they don't establish the connection, "client" sockets do and their remote address is the **connected client's address** (ex. a browser: `172.217.6.196:80` or `127.0.0.1:xxxxx`).

## Sockets in Python

Python's `socket` module provides an interface to the Berkeley sockets API.

It exposes all of the necessary methods to quickly write TCP and UDP clients and servers for writing low-level network applications. There are higher-level Python APIs such as `Twisted` that might be better suited.

### Type

Based on the **communication type**, sockets are classified as follows:

Type | Constant | Notes
--- | --- | ---
**TCP** | `SOCK_STREAM` | You’ll get better behavior and performance from a STREAM socket than anything else.
**UDP** | `SOCK_DGRAM` |

### Family

Sockets can also be categorized by **family**. We will focus on the following two:

Type | Constant | Notes
--- | --- | ---
**IPv4** | `AF_INET` | Account for at least 99% of the sockets in use. <br><br> A pair (host, port) is used, with **host** as: <ul><li>A hostname in Internet domain notation like 'daring.cwi.nl'</li><li>An IPv4 address like '100.50.200.5'
**IPv6** | `AF_INET6` |

## Socket Methods

* [**`getaddrinfo()`**](#getaddrinfo)

* [**`getfqdn()`**](#getfqdn)

* [**`gethostname()`**](#gethostname)

* [**`gethostbyname()`**](#gethostbyname)

* [**`gethostbyname_ex()`**](#gethostbyname_ex)

* [**`gethostbyaddr()`**](#gethostbyaddr)

[socket_methods.py](./chapter3/socket_methods.py)

### `getaddrinfo`

```python
getaddrinfo(host, port, family=0, type=0, proto=0, flags=0) -> list[tuple[family, type, proto, canonname, sockaddr]]
"""Translate the host/port argument into a sequence of 5-tuples that contain all the necessary arguments for creating a socket connected to that service.

:param host: a domain name, a string representation of an IPv4/v6 address or None.
:param port: a string service name such as 'http', a numeric port number or None.
"""
```

### `getfqdn`

```python
getfqdn([name]) -> str
"""Return a fully qualified domain name for name. If name is omitted or empty, it is interpreted as the local host."""
```

* **Note**: To find the fully qualified name, the hostname returned by `gethostbyaddr()` is checked, followed by aliases for the host, if available. The first name which includes a period is selected. In case no fully qualified domain name is available, the hostname as returned by `gethostname()` is returned.

### `gethostname`

```python
gethostname() -> str
"""Return the current hostname of the machinne where the Python interpreter is currently executing."""
```

* **Note**: `gethostname()` doesn’t always return the **fully qualified domain name**; use **[`getfqdn()`](#getfqdn)** for that.

The **hostname** is just the computer name. Alternative ways to retrieve this value:

```python
# Bash
$ hostname  # MacingtonProlll.fios-router.home

# Python
import platform
platform.node()  # MacingtonProlll.fios-router.home
```

#### **Direct DNS Resolution**

> When binding a socket to listen to a host name, it will in turn be resolved to an IP address.

### `gethostbyname`

```python
gethostbyname(hostname: str) -> str
"""Return the IPv4 address(a string of the form '255.255.255.255') for a host."""
```

You can get this value by running **`ping <hostname>`** in your console:

```bash
$ ping macingtonprolll.fios-router.home  # PING macingtonprolll.fios-router.home (192.168.1.155): 56 data bytes
$ ping www.google.com  # PING www.google.com (172.217.3.100): 56 data bytes
```

#### *Why is `ping` and `gethostbyname` resolving to an IP 92.242.140.21 for any random hostname that I type?*

```bash
$ ping madeupnameblag  # PING madeupnameblag (92.242.140.21): 56 data bytes
```

* Because your ISP is **hijacking** your DNS queries. They are trying to be "helpful" by redirecting requests for nonexistent domains to a white label service that provides search results and advertising, from which everyone but you gets a cut of the revenue.
  * For example, searchassist.verizon.com for me because my ISP is Verizon FiOS, and they run Verizon DNS servers for my router.

* Your DNS instead should be returning error & failing the request. Your ISP should have a preferences page where you can supposedly turn it off. Another solution is to [consider using a 3rd party DNS service](https://www.howtogeek.com/167239/7-reasons-to-use-a-third-party-dns-service/).

**Note**: I fixed this problem by configuring my router to use a 3rd party DNS service. I selected **Cloudflare's 1.1.1.1** on the basis of speed and privacy. Now I get the desired result for an unknown host:

```Bash
# Bash
$ ping madeupnameblag  # ping: cannot resolve madeupnameblag: Unknown host

# Python
gethostbyname('madeupnameblag')  # socket.gaierror: [Errno 8] nodename nor servname provided, or not known
```

### `gethostbyname_ex`

```python
gethostbyname_ex(hostname: str) -> (name, alias: list, address: list)
"""Extended interface for gethostbyname"""
```

* **Note**: `gethostbyname()` and `gethostbyname_ex()` do not support IPv6 name resolution, and **`getaddrinfo()`** should be used instead for IPv4/v6 dual stack support.

### `gethostbyaddr`

```python
gethostbyaddr(hostname: str) -> (name, alias: list, address: list)
"""Return the true host name, a list of aliases, and a list of IP addresses, for a host."""
```

* **Note**: "True host name" refers to the primary name by which the host at that IP address would like to be known. It is not necessarily the fully qualified hostname.

* **Note**: Supports both IPv4 and IPv6.

#### Reverse resolution

> Allows us to associate a domain name with a specific IP address.

## Creating a Socket

A server *must* perform the sequence

1. [**`socket()`**](#socket)
2. [**`bind()`**](#bind)
3. [**`listen()`**](#listen)
4. [**`accept()`**](#accept) (possibly repeating the `accept()` to service more than one client)

* **Note**: 1-3 may be replaced by [**`create_server()`**](#create_server)

[http_server.py](./chapter3/http_server/http_server.py)

While a client only needs the sequence

1. [**`socket()`**](#socket)
2. [**`connect()`**](#connect) or [**`connect_ex()`**](#connect_ex)

* **Note**: 1-2 may be replaced by [**`create_connection()`**](#create_connection)

[socket_data.py]((./chapter3/socket_data.py))

**Note**: both implementations can make use of **`settimeout`**. See [Timeout Notes](#Timeout-Notes).

#### socket server

Status | Local Address (`laddr`) | Remote Address (`raddr`) |
--- | --- | --- |
Before `bind` | zero (`0.0.0.0:0`), no connection. | N/A
After `bind` | ex. `0.0.0.0:8080` (everyone on IPv4 interface) <br> ex2. `127.0.0.1:8080` (localhost) <br> ex3. `192.168.1.246:8080` (public ip) <ul><li><b>ip</b>: your web server's ip</li><li><b>port</b>: your web server's port</li></ul>A TCP server (such as a web server process) <b><i>listens</b></i> on a local port. Here, the local address only controls who can connect to this port - see [`bind()`](#bind). | N/A
After `listen` | No change | N/A
After `accept` | No change <br><br> `accept` returns a new socket to handle the connection while this one just keeps on listening. | N/A

#### socket client

Status | Local Address (`laddr`) | Remote Address (`raddr`) |
--- | --- | --- |
Before `connnect` | zero (`0.0.0.0:0`), no connection. | N/A
After `connect` | ex. `192.168.1.246:50679`<ul><li><b>ip</b>: internal ip of your machine</li><li><b>port</b>: dynamically assigned</li></ul> | ex.`142.250.64.68:80` <ul><li><b>ip</b>: ip of the client's web server</li><li><b>port</b>: port the client's web server is listening on (`80` for http is normal)</li></ul>

### Implementation

### socket()

**socket server** and **socket client** method (used the same for both)

Create a new socket object.

```python
socket(family=AF_INET, type=SOCK_STREAM, proto: int=0) -> socket
socket(family=-1, type=-1, proto=-1, fileno: int=None) -> socket
"""Open a socket of the given type.

:param family: socket domains defined on AddressFamily
:param type: socket types defined on SocketKind. Stream (SOCK_STREAM) or datagram (SOCK_DGRAM) socket.
:param proto: protocol
:param fileno: when passed, family, type and proto are auto-detected, unless they are explicitly set.
:return: one endpoint of a network connection
"""
```

The default socket is a TCP socket using IPV4:

```python
# Equivalent to socket(family=AF_INET, type=SOCK_STREAM, proto=0)
ss = socket()  # <socket.socket fd=3, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('0.0.0.0', 0)>
```

### connect()

**socket client** method

```python
connect(addr: tuple[str, int]) -> None
"""Connects the client to the server IP address.

:param addr: A pair (host, port).
"""
```

Roughly speaking, when you visit the webpage www.python.org, your browser does something like the following (**client socket**):

```python
# Create an INET, STREAMing socket
s = socket()  # <... laddr=('0.0.0.0', 0)>

# Now connect to the web server on port 80 (normal http port)
s.connect(("www.python.org", 80))
# <... laddr=('192.168.1.246', 50679), raddr=('142.250.64.68', 80)>
```

As discussed under [gethostbyname()](#gethostbyname), `connect` will **not fail even if the host is not a real existing host** because of your ISPs DNS resolution. It will even allow you to `send` and `recv` data.

* You can test this out by passing a random host to `target_host` in [socket_data.py](./chapter3/http_server/testing_http_server.py).

However, if the ***port* is not accepting connections, it will hang after `connect` until a timeout** (a random host will probably fail if you change your port from 80 to something non-standard).

### connect_ex()

**socket client** method

```python
connect_ex(addr: tuple[str, int]) -> int
"""
Same functionality as the connect() method and also offers the possibility
of returning an error in the event of not being able to connect with that
address.

:return: 0 if connects, otherwise the value of the errno variable.
"""
```

Useful for:

1) Implementing **port scanning** with sockets: [socket_ports_open.py](./chapter3/socket_ports_open.py)

2) Asynchronous

  * If you try to use `connect` with `setblocking(False)`, you will raise an exception `BlockingIOError: [Errno 36] Operation now in progress`
  * But if you use `connect_ex`, you will just return 36

### create_connection()

**socket client** method

```python
create_connection: (addr: Tuple[str | None, int], timeout: float | None, source_address: Tuple[bytearray | bytes | str, int] | None) -> socket
"""Connect to *addr* and return the socket object."""
```

### bind()

**socket server** method

```python
bind(addr: tuple[str, int]) -> None
"""Bind the socket to a local address.

The socket must be open before establishing the connection with the address.

:param addr: (host, port)
"""
```

**Note**: non-privileged ports are > 1023. Using a privileged port without root privileges will result in `PermissionError: [Errno 13]`

**For host, passing**:

1) 'localhost' means only localhost (this machine) can connect to this port

```python
ss.bind(('localhost', 8080))
# <... laddr=('127.0.0.1', 8080)>
```

2) '' makes the port available to connect for everyone

```python
ss.bind(('', 8080))
# <... laddr=('0.0.0.0', 8080)>
```

3) A specific IP address, as resolved from the result of **`gethostname()`**, will only accept connections to the associated interface. (A connection made must be made to the resolved IP)

```python
ss.bind((gethostname(), 8080))
# <... laddr=('192.168.1.246', 8080)
```

**For port, passing**:

1) 0 selects an arbitrary unused port

```python
ss.bind(('localhost', 0))
# <.... laddr=('127.0.0.1', 61510)>
```

2) Any other existing port value selects that port

### listen()

**socket server** method

Marks the socket referred to by `sockfd` as a passive socket.

```python
listen(backlog: int=SOMAXCONN) -> None
"""Listen for connections on a socket.

:param backlog: queue limit for incoming connection.
"""
```

The default value for `backlog` for `listen` is currently 128 (platform dependent):

```python
print(SOMAXCONN)  # 128
```

### create_server()

**socket server** method

Convenience function for creating a **TCP socket** (SOCK_STREAM) which combines `socket`, `setsockopt`, `bind` and `listen`

```python
create_server(addr, family=AF_INET, backlog=None, reuse_port=False, dualstack_ipv6=False) -> socket
"""Creates a TCP socket bound to address (a 2-tuple (host, port)).

:param addr: what we pass to 'bind'
:param family: 'AF_INET' or 'AF_INET6'
:param backlog: the queue sized passed to 'listen'
:param reuse_port: dictates whether to use the
    'SO_REUSEPORT' socket option. True is same as
    'ss.setsockopt(SOL_SOCKET, SO_REUSEPORT, 1)'.
:param dualstack_ipv6: If true and the platform
    supports it, create an 'AF_INET6' socket able to
    accept both IPv4 or IPv6 connections. When false
    it will explicitly disable this option on
    platforms that enable it by default (e.g. Linux).
"""
```

Usage:

```python
with create_server(('localhost', 8080)) as ss:
```

OR

```python
ss = create_server(('localhost', 8080))
```

### accept()

**socket server** method

```python
accept() -> tuple[clientsocket, clientaddr]
"""Accept connection, returning new socket fd and client address.

Blocks and waits for an incoming connection.

Enables us to accept client connections and returns a tuple with
two values that represent client_socket and client_address. You
need to call the socket.bind() and socket.listen() methods
before using this method.
"""
```

For example: I've started a `python3 -m http.server` on localhost port 7001:

```bash
Proto Local Address   Foreign Address  (state)       COMMAND
tcp4  127.0.0.1:7001                   LISTEN        32143/python3
```

When the server process `accept`s the connection we get a socket representing that connection (**a unique file descriptor**).

I connect to that web server via my web browser, and we see two additional sockets:

```bash
Proto Local Address   Foreign Address  (state)      COMMAND
tcp4  127.0.0.1:7001   0.0.0.0:*        LISTEN       32143/python3
tcp4  127.0.0.1:50204  127.0.0.1:7001   ESTABLISHED  1658/firefox
tcp4  127.0.0.1:7001   127.0.0.1:50204  ESTABLISHED  32143/python3
```

(data obtained via `$ netstat`, and edited for clarity. Also check out `$ lsof -i`)

The Firefox browser created a socket to `connect()` to the server. Firefox uses port 50204 in this case, so its socket is identified as local `127.0.0.1:50204 remote 127.0.0.1:7001`. **When the server `accept()`ed the connection, this connection got its own socket, which is basically the reverse of the client's socket**: `local 127.0.0.1:7001 remote 127.0.0.1:50204`. The local port is the same port the server is listening to.

## Using a Socket

These are the general socket methods we can use in both socket clients and servers:

**TCP communication**:

* [**`send()`**](#send)
* [**`recv()`**](#recv)

**UDP communication**:

* **`sendto(data, addr)`**: Sends data to a given address.
* **`recvfrom(bufsize)`**: This method receives data and the sender's address.

### send()

```python
send(data: bytes) -> bytes
"""Sends bytes of data to the specified target."""
```

Use **`encode`** to convert to bytes: `str.encode(encoding: str='UTF-8') -> bytes`

### recv()

```python
recv(bufsize: int) -> bytes
"""Receive data from the socket.

It is a blocking call - blocking if no data is waiting to be read.

:param bufsize: the maximum amount of data it can receive.
:return: bytes object representing the data received.
"""
```

* Ex. `s.recv(1024)` will read at most 1024 bytes.

* Note: for best match with hardware and network realities, the value of `bufsize` should be relatively small (commonly, power of 2), for example, 4096.

Use **`decode`** to convert the `recv`'d data from bytes when you know the encoding: `bytes.decode(encoding: str='UTF-8') -> str`

## Basic socket client with the `socket` module

> **Normally, the *connecting* socket starts the conversation, by sending in a request**, or perhaps a signon. But that’s a design decision - it’s not a rule of sockets.

1) When the **`connect`** completes
2) The socket can be used to **`send`** in a request for the text of the page.
3) The same socket will read the reply (**`recv`**)
4) And then be destroyed (**`close`**).
    * That’s right, destroyed. Client sockets are normally only used for one exchange (or a small set of sequential exchanges).
       * (Like the multiple commands we send from a command struct to the `watchout_client`)

[`socket_data.py`](./chapter3/http_server/testing_http_server.py)

## HTTP server in Python with the `socket` module

After marking our socket as a "server" socket with `listen`, we enter the mainloop of the server.
Here, we are establishing the logic of our server every time it receives a request from a client:

1) **`Accept`** the connection
2) Spawns a new socket to communicate directly with the newly connected client. (First instance of two-way communications between them). Allows other clients to connect.
    * The loop, often a simple **`while True`**, keeps the "server" socket listening. Without it, it would disconnect after the first client request.

```python
while True:
    # accept connections from outside
    (clientsocket, clientaddr) = ss.accept()
    # now do something with the clientsocket
    # in this case, we'll pretend this is a threaded server
    ct = client_thread(clientsocket)
    ct.run()
  ```

There’s actually 3 general ways in which this loop could work:

1) Dispatching a thread to handle clientsocket
2) Create a new process to handle clientsocket
3) Restructure this app to use non-blocking sockets, and multiplex between our “server” socket and any active "client" sockets using select.

#### The important thing to understand now is this: this is all a “server” socket does.

* It doesn’t send any data.
* It doesn’t receive any data.
* It just produces “client” sockets.
  * **Each clientsocket is created in response to some other “client” socket doing a `connect()` to the host and port we’re bound to**.
  * As soon as we’ve created that clientsocket, we go back to listening for more connections.
  * The two “clients” are free to chat it up - they are using some dynamically allocated port which will be recycled when the conversation ends.

## Timeout Notes

### Timeout Methods

* [**`getdefaulttimeout()`**](#getdefaulttimout)

* [**`gettimeout()`**](#gettimout)

* [**`setdefaulttimeout()`**](#setdefaulttimout)

* [**`settimeout()`**](#settimout)

### Timeouts and the `connect` method
>
>The `connect()` operation is subject to the `timeout` setting, and in general it is recommended to call **`settimeout()` before calling `connect()` or pass a `timeout` parameter to `create_connection()`**. However, the system network stack *may* also return a connection timeout error of its own regardless of any Python socket timeout setting.

```python
s = socket()
s.settimeout(2.0)
s.connect((target_host, target_port))
```

or using **`create_connection`**:

```python
s = create_connection((target_host, target_port), timeout=2.0)
```

**Without a timeout**: timeout eventually occurs with exception **`TimeoutError: [Errno 60] Operation timed out.`**

**With a timeout**: timeout occurs after the set number of seconds with exception **`socket.timeout: timed out`**.

### We can map errors to their standard `errno` system symbols:

```python
import errno

sock = socket()
sock.settimeout(5)
result = sock.connect_ex((ip, port))
if result == 0:
    print(f"Port {port}: \t Open")
else:
    print (f"Port {port}: \t Closed")
    print("Reason:", errno.errorcode[result])
sock.close()
```

**without a timeout**: result = 60, Reason: **`ETIMEDOUT`** (Device not a stream).

**With a timeout**: result = 35, Reason: **`EAGAIN`**, meaning a receive timeout had been set, and the timeout expired before data were received. (Resource deadlock avoided).

### Timeouts and the `accept` method

> If **`getdefaulttimeout()`** is not None, sockets returned by the `accept()` method inherit that timeout. Otherwise, the behaviour depends on settings of the listening socket:
>
> * If the listening socket is in blocking mode or in timeout mode, the socket returned by `accept()` is in blocking mode;
>
> * If the listening socket is in non-blocking mode, whether the socket returned by `accept()` is in blocking or non-blocking mode is operating system-dependent. If you want to ensure cross-platform behaviour, it is recommended you manually override this setting.

### `getdefaulttimeout()`

```python
getdefaulttimeout() -> float | None
"""Return the default timeout in seconds (float) for new socket objects.

:return: None indicates that new socket objects have no timeout.
```

**Note**: When the socket module is first imported, the default is None, meaning newly created socket objects have no timeout.

### `setdefaulttimeout()`

```python
setdefaulttimeout(timeout: float=None)
"""Set the default timeout in seconds (float) for new socket objects.
```

Used directly on the `socket` module:

```python
setdefaulttimeout(2.0)
ss = socket()
```

### `gettimeout()`

```python
gettimeout() -> float | None
"""Returns the timeout for socket operations associated with the socket object.

:return: None indicates that timeouts on socket operations are disabled.
"""
```

Also can access with the socket object's `timeout` attribute.

### `settimeout()`

```python
settimeout(timeout: float | None) -> None
"""Set a timeout for socket operations associated with the socket object.

:param timeout: can be a float, giving in seconds, or None.
    Setting a timeout of None disables the timeout feature and is
    equivalent to setblocking(1). Setting a timeout of zero is
    the same as setblocking(0).
"""
```
