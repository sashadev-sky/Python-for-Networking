#!/usr/bin/python

from socket import socket, create_connection

"""
1. Create a socket object
"""

print('creating socket ...')
# s = socket()
# print(f'socket created: {repr(s)}')
# s.settimeout(2.0)

# print("connection with remote host")
target_host, target_port = "www.google.com", 80

"""
2. Then connect the client to the remote host
"""

# s.connect((target_host, target_port))

# 2nd way
s = create_connection((target_host, target_port), timeout=2.0)
print(f'connection ok: {repr(s)}')

"""
3. When the connect completes, the socket can be used to send in a request for the text of the page.
"""

request = "GET / HTTP/1.1\r\nHost:%s\r\n\r\n" % target_host
s.send(request.encode())

"""
4. Receive some data back from the server
"""

data = s.recv(4096)
print("Data", data.decode())
print("Length", len(data))

"""
5. The socket will then be destroyed
"""

print('closing the socket')
s.close()

"""
$ p3 socket_data.py
creating socket ...
connection ok: <socket.socket ...>
Data HTTP/1.1 200 OK ...
Length 2836
closing the socket
"""
