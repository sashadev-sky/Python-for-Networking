#!/usr/bin/env python3

from socket import socket

ip = '127.0.0.1'
portlist = [21, 22, 23, 80]
for port in portlist:
	sock = socket()
	result = sock.connect_ex((ip, port))
	print(port, ":", result)
	sock.close()

"""
Checks ports for ftp, ssh, telnet, and http services
in the localhost interface.

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
