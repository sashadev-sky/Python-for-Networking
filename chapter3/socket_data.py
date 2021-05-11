#!/usr/bin/python

from socket import socket, create_connection

"""
1. Create a socket object then connect it to the remote host

a) Classic Implementation
`s = socket()
`s.settimeout(2.0)
`target_host, target_port = "www.google.com", 80
`s.connect((target_host, target_port))

b) Alternaative Implementation: `create_connection`

2. When the connect completes, the socket can be used to send in a request for the text of the page.
3. Receive some data back from the server
4. The socket will then be destroyed
"""

target_host, target_port = "www.google.com", 80
with create_connection((target_host, target_port), timeout=2.0) as cs:
    print(f'connection ok: {repr(cs)}')

    request = "GET / HTTP/1.1\r\nHost:%s\r\n\r\n" % target_host
    cs.send(request.encode())

    data = cs.recv(4096)
    print("Data", data.decode())
    print("Length", len(data))

"""
$ p3 socket_data.py
creating socket ...
connection ok: <socket.socket ...>
Data HTTP/1.1 200 OK ...
Length 2836
closing the socket
"""
