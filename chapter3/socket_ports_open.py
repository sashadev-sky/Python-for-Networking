#!/usr/bin/env python3

from socket import AF_INET, SOCK_STREAM, socket

ip = '127.0.0.1'
portlist = [21, 22, 23, 80]
for port in portlist:
	# sock = socket(AF_INET, SOCK_STREAM)
	sock = socket()
	result = sock.connect_ex((ip, port))
	print(port, ":", result)
	sock.close()

"""
script shows ports that are open in the localhost machine
with the loopback IP address interface of 127.0.0.1.

checks ports for ftp, ssh, telnet, and http services
in the localhost interface.

'connect_ex' returns 0 if connects, otherwise returns an error code

error code 61: ECONNREFUSED Connect	The requested connection was refused. Ensure server application is available and at specified port.

$ p3 socket_ports_open.py
21: 61
22: 61
23: 61
80: 61

To get 80 to return 0:

$ sudo python3 -m http.server 80 -b 127.0.0.1
$ p3 socket_ports_open.py
21: 61
22: 61
23: 61
80: 0
"""
