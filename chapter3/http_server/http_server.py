from socket import (AF_INET, SO_REUSEPORT, SOCK_STREAM, SOL_SOCKET,
                    create_server, socket)


"""
`socket(family=AF_INET, type=SOCK_STREAM, proto=0)`
"""

# serversocket = socket()

"""
To set a socket option do it right before `bind`:
    `serversocket.setsockopt(SOL_SOCKET, SO_REUSEPORT, 1)`
"""

# serversocket.bind(('localhost', 8080))
# serversocket.listen(5)

"""
The resulting socket obj created:
    - does not have 'timeout' enabled (-> None) ('timeout' attribute or 'gettimeout()' method)
    - 'socket.SO_REUSEADDR' is set to 4 (Remote Port)
    - 'socket.SO_REUSEPORT' is set to 512
    - 'serversocket.fileno()' -> 4
    - 'serversocket.family' -> <AddressFamily.AF_INET: 2>
    - 'serversocket.type' -> <SocketKind.SOCK_STREAM: 1>
    - 'serversocket.proto' -> 0
"""

"""
* Alterantive way: 'create_server'

Convenience function which creates a TCP socket bound to address (a 2-tuple (host, port)) and return the socket object.

    * combines 'socket', 'setsockopt', 'bind' and 'listen'

`create_server(addr, family=AF_INET, backlog=None, reuse_port=False, dualstack_ipv6=False) -> socket
    `@addr
        what we pass to `bind`
    `@backlog
        what we pass to `listen`
    `@reuse_port
        dictates whether to use the SO_REUSEPORT socket option. True is same as `serversocket.setsockopt(SOL_SOCKET, SO_REUSEPORT, 1)`
    `@dualstack_ipv6
        If true and the platform supports it, create an AF_INET6 socketable to accept both IPv4 or IPv6 connections.
        When false it will explicitly disable this option on platforms that enable it by default (e.g. Linux).

`serversocket = create_server(('localhost', 8080), backlog=5)`
or
`with create_server(('localhost', 8080), backlog=5) as serversocket:`
"""

"""
* if we removed 'while True', socketserver would disconnect after the request (opening browser window at addr)
"""

# with create_server(('localhost', 8080), backlog=5) as serversocket:
#     while True:
#         print('Waiting for connections')
#         clientsocket, address = serversocket.accept()
#         # handle new connection
#         print('HTTP request received:')
#         print(clientsocket.recv(1024))
#         clientsocket.send(bytes(
#             "HTTP/1.1 200 OK\r\n\r\n <html><body><h1>Hello World!</h1></body></html> \r\n", 'utf-8'))
#         clientsocket.close()

"""
Refactored a 3rd time - use a client context manager too
"""

with create_server(('localhost', 8080), backlog=5) as serversocket:
    # <socket.socket fd=3, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 8080)>
    print(repr(serversocket))
    while True:
        print('Waiting for connections')
        clientsocket, addr = serversocket.accept()
        # handle new connection
        with clientsocket:
            print('Connected by', addr)
            print('HTTP request received:')
            print(clientsocket.recv(1024))
            clientsocket.send(bytes(
                "HTTP/1.1 200 OK\r\n\r\n <html><body><h1>Hello World!</h1></body></html> \r\n", 'utf-8'))


"""
$ p3 http_server.py

* Open browser and go to localhost:8080. In terminal will see:

Waiting for connections
Connected by ('127.0.0.1', 62993)
HTTP request received:
b'GET / HTTP/1.1\r\nHost: localhost:8080\r\nConnection: keep-alive\r\nsec-ch-ua: "Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"\r\nsec-ch-ua-mobile: ?0\r\nUpgrade-Insecure-Requests: 1\r\nUser-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\nSec-Fetch-Site: none\r\nSec-Fetch-Mode: navigate\r\nSec-Fetch-User: ?1\r\nSec-Fetch-Dest: document\r\nAccept-Encoding: gzip, deflate, br\r\nAccept-Language: en-US,en;q=0.9\r\nCookie: io=af57fbe00f1b44208dff7aa758fa5038; _ga=GA1.1.1015030773.1615958191\r\n\r\n'

* Refreshing the page or reopening it in a new tab resends everything with a new client connection each time. Closing the browser
* does not close the server.
"""

"""
!The important thing to understand is this: this is all a “server” socket does.
* It doesn’t send any data.
* It doesn’t receive any data.
* It just produces “client” sockets.
    * Each clientsocket is created in response to some other “client” socket doing a connect() to the host and port we’re bound to.
    * As soon as we’ve created that clientsocket, we go back to listening for more connections.
    * The 2 “clients” are free to chat it up - they r using some dynamically allocated port which will be recycled when the conversation ends.
"""
