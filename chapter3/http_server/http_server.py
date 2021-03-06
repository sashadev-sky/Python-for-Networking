#!/usr/bin/env python3

from socket import create_server, socket


"""
1. Classic Implementation

`ss = socket()
`ss.bind(('localhost', 8080))
`ss.listen()

The resulting socket obj created:
    - does not have 'timeout' enabled (-> None) ('timeout' attribute or 'gettimeout()' method)
    - 'socket.SO_REUSEADDR' is set to 4 (Remote Port)
    - 'socket.SO_REUSEPORT' is set to 512
    - 'ss.fileno()' -> 4
"""

"""
2. Alterantive Implementation: 'create_server'
"""

# with create_server(('localhost', 8080)) as serversocket:
    # while True:
    #     print('Waiting for connections')
    #     clientsocket, clientadd = serversocket.accept()
    #     clientsocket.settimeout(2.0)
    #     # handle new connection
    #     print('HTTP request received:')
    #     print(clientsocket.recv(1024))
    #     clientsocket.send(bytes(
    #         "HTTP/1.1 200 OK\r\n\r\n <html><body><h1>Hello World!</h1></body></html> \r\n", 'utf-8'))
    #     clientsocket.close()


"""
3. Alternative Implementation Refactored: Use a client context manager too
"""

with create_server(('localhost', 8080)) as serversocket:
    print(repr(serversocket))  # <socket.socket fd=3, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 8080)>
    while True:
        print('Waiting for connections')
        clientsocket, clientaddr = serversocket.accept()
        print(f'accept: {repr(serversocket)}')  # accept: <socket.socket fd=3, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 8080)>
        print(f'{repr(clientsocket)}')  # <socket.socket fd=6, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 8080), raddr=('127.0.0.1', 56416)>
        clientsocket.settimeout(2.0)
        # handle new connection
        with clientsocket:
            print('Connected by', clientaddr)  # Connected by ('127.0.0.1', 56416)
            data = clientsocket.recv(1024).decode()
            print(f'HTTP request received: {data}')  # b'GET / HTTP/1.1\r\nHost: localhost\r\n\r\n'
            res = "HTTP/1.1 200 OK\r\n\r\n <html><body><h1>Hello World!</h1></body></html> \r\n"
            clientsocket.send(res.encode())

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
