#!/usr/bin/env python

from socket import socket, SOCK_DGRAM

SERVER_IP, SERVER_PORT = '127.0.0.1', 6789

address = (SERVER_IP ,SERVER_PORT)

socket_client = socket(type=SOCK_DGRAM)

while True:
	message = input('Enter your message > ')
	if message== 'quit':
		break
	socket_client.sendto(message.encode(),address)
	response_server, addr = socket_client.recvfrom(4096)
	print("Response from the server => %s" % response_server.decode())

socket_client.close()
