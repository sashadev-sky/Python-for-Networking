#!/usr/bin/env python

from socket import socket, SOCK_DGRAM
import sys

SERVER_IP, SERVER_PORT = '127.0.0.1', 6789

socket_server = socket(type=SOCK_DGRAM)
socket_server.bind((SERVER_IP,SERVER_PORT))

print(f'[*] Server UDP Listening on {SERVER_IP}:{SERVER_PORT}')

while True:
	data, address = socket_server.recvfrom(4096)
	socket_server.sendto('I am the server accepting connections...'.encode(), address)
	data = data.decode().strip()
	print(f'Message {data} received from {address}')

	try:
		response = f'Hi {sys.platform}'
	except Exception as e:
		response = f'{sys.exc_info()[0]}'

	print("Response", response)
	socket_server.sendto(response.encode(), address)
