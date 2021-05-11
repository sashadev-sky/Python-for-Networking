#!/usr/bin/env python3

import optparse
from socket import gethostbyname, socket, create_connection
import time
from threading import *

def socket_scan(host, port):
	try:
		with create_connection((host, port), timeout=5):
			print('[+] %d/tcp open' % port)
	except Exception as exception:
		print('[-] %d/tcp closed\n[-] Reason: %s' % (port, exception))

def port_scanning(host: str, ports: list, is_range: bool):
	try:
		ip = gethostbyname(host)
		print('[+] Scan Results for: ' + ip)
	except Exception as exception:
		print('[-] Reason: %s' % (str(exception)))
		return

	if is_range:
		ports = range(int(ports[0]), int(ports[-1]) + 1)

	threads = []
	for port in ports:
		t = Thread(target=socket_scan, args=(ip, int(port)))
		t.start()
		threads.append(t)

	while threads:
		# Wait for all threads to complete by entering them - make them stay in order
		threads.pop().join()

def main():
	parser = optparse.OptionParser('socket_ports_open.py ' + '-H [hostname] -p [port[s]]')
	parser.add_option('-H', "--host", dest='host', type='string', help='specify host')
	parser.add_option('-p', "--port", dest='port', type='string',
	                  help='specify port[s] separated by comma')
	parser.add_option('-r', action="store_true", dest='is_range',
	                  help='specify port numbers as a range: lo,hi [inclusive]')

	(options, _) = parser.parse_args()
	host, ports, is_range = options.host, str(options.port).split(','), options.is_range

	if (host == None) | (ports[0] == None):
		print(parser.usage)
		exit(0)

	port_scanning(host, ports, is_range)

if __name__ == '__main__':
	started = time.time()
	main()
	elapsed = time.time() - started
	print()
	print("time elapsed: {:.2f}s".format(elapsed))

"""
Using `threading` module in simplest one-thread-per-item fashion.

$ sudo python3 -m http.server 80 -b 127.0.0.1
$ p3 socket_ports_open.py -H localhost -p 80,83 -r
[+] Scan Results for: 127.0.0.1
[+] 80/tcp open
[-] 81/tcp closed
[-] Reason: [Errno 61] Connection refused
[-] 82/tcp closed
[-] Reason: [Errno 61] Connection refused
[-] 83/tcp closed
[-] Reason: [Errno 61] Connection refused

time elapsed: 0.01s

With a remote host:
$ p3 socket_ports_open.py -H 172.217.168.164 -p 80,83
[+] Scan Results for: 172.217.168.164
[+] 80/tcp open
[-] 83/tcp closed
[-] Reason: timed out

time elapsed: 5.01s

With an unknown host:
$ p3 socket_ports_open.py -H blah -p 80,83
[-] Reason: [Errno 8] nodename nor servname provided, or not known

time elapsed: 0.01s
"""
