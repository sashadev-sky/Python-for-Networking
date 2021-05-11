#!/usr/bin/python

from socket import socket, create_server
import threading

SERVER_IP, SERVER_PORT   = '127.0.0.1', 9998

def handle_client(client_socket):
    request = client_socket.recv(1024).decode()
    print(f'[*] Received request: {request} from client {client_socket.getpeername()}')
    client_socket.send('ACK'.encode())

with create_server((SERVER_IP,SERVER_PORT)) as ss:
    print("[*] Server Listening on %s:%d" % (SERVER_IP,SERVER_PORT))
    client, addr = ss.accept()
    client.send("I am the server accepting connections...".encode())
    print("[*] Accepted connection from: %s:%d" % (addr[0], addr[1]))

    while True:
        handle_client(client)
