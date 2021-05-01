#!/usr/bin/python3
from socket import socket

webhost, webport = 'localhost', 8080
print("Contacting %s on port %d ..." % (webhost, webport))
webclient = socket()
webclient.connect((webhost, webport))
webclient.send("GET / HTTP/1.1\r\nHost: localhost\r\n\r\n".encode())
reply = webclient.recv(4096)
print(f'len: {len(reply)}' )
print("Response from %s:" % webhost)
print(reply.decode())

"""
$ p3 testing_http_server.py
Contacting localhost on port 8080 ...
Response from localhost:
HTTP/1.1 200 OK

 <html><body><h1>Hello World!</h1></body></html>
"""
