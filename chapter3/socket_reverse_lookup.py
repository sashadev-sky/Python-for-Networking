#!/usr/bin/env python

import socket

result = socket.gethostbyaddr('8.8.8.8')
print('The host name is:', result[0])
print('Ip addresses:')
for item in result[2]:
	print(" "+item)

"""
This reverse lookup command obtains the hostname from the IP address.
For this task, we can use the gethostbyaddr() method.

If the IP address is incorrect, the call to the gethostbyaddr() method
will throw an exception with the message "Error for resolving ip address:
[Errno -2] Name or service not known".

$ p3 socket_reverse_lookup.py
The host name is: dns.google
Ip addresses:
 8.8.8.8
"""
