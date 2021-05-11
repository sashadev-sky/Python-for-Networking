#!/usr/bin/python

from socket import socket, create_connection

host, port = '127.0.0.1', 9998

try:
    with create_connection((host, port)) as cs:
        print(f'Connected to host {host} in port: {port}')
        msg = cs.recv(1024)
        print(f'Message received from the server: {msg}')
        while True:
            message = input('Enter your message > ')
            cs.send(message.encode())
            if message == 'quit':
                break
except Exception as exception:
	print('[-] Reason: %s' % (str(exception)))
