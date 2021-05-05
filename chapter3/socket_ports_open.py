#!/usr/bin/env python3

from socket import socket, gethostbyname
import sys
from datetime import datetime
import errno
from threading import *
import optparse


def socket_scan(host, port):
	try:
		socket_connect = socket()
		socket_connect.settimeout(5)
		socket_connect.connect((host, port))
		print('[+] %d/tcp open' % port)
	except Exception as exception:
		print('[-] %d/tcp closed' % port)
		print('[-] Reason:%s' % str(exception))
	finally:
		socket_connect.close()

def port_scanning(host: str, ports: list, is_range: bool):
	time_init = datetime.now()
	try:
		ip = gethostbyname(host)
		print('[+] Scan Results for: ' + ip)
	except:
		print("[-] Cannot resolve '%s': Unknown host" % host)
		return

	if is_range:
		ports = range(int(ports[0]), int(ports[1]))
	for port in ports:
		t = Thread(target=socket_scan, args=(ip, int(port)))
		t.start()

	time_finish = datetime.now()
	total = time_finish - time_init
	print('Port Scanning Completed in: ', total)


def main():
	parser = optparse.OptionParser('socket_portScan ' + '-H <Host> -P <Port>')
	parser.add_option('-H', dest='host', type='string', help='specify host')
	parser.add_option('-P', dest='port', type='string',
	                  help='specify port[s] separated by comma')
	parser.add_option('-R', default=False, dest='is_range', type='string',
	                  help='specify specified ports as a range')

	(options, _) = parser.parse_args()

	host, ports = options.host, str(options.port).split(',')

	if (host == None) | (ports[0] == None):
		print(parser.usage)
		exit(0)

	port_scanning(host, ports, options.is_range)


# host = input("Enter a host to scan: ")

# opt = input("(1) Scan a range or (2) Scan a list: ")
# if opt == '1':
# 	print("Please enter the range of ports you would like to scan on the machine")
# 	start_port = input("Enter a start port: ")
# 	end_port = input("Enter a end port: ")
# 	ports = [start_port, end_port]
# 	is_range = True
# elif opt == '2':
# 	ports = [21, 22, 80, 8080, 443]
# 	is_range = False
# else:
# 	print('Please select a valid option')
# 	sys.exit()

# port_scanning(host, ports, is_range)

if __name__ == '__main__':
	main()

"""
$ check_ports_socket('localhost', [21, 22, 80, 8080, 443], is_range=False)

Checks ports for ftp, ssh, telnet, and http services, + 2 extra ports
in the localhost interface.

error code 61: ECONNREFUSED Connect	The requested connection was refused. Ensure server application is available and at specified port.

$ p3 socket_ports_open.py
Enter a host to scan: localhost
(1) Scan a range or (2) Scan a list: 2
Please wait, scanning remote host 127.0.0.1
Checking port 21 ...
Port 21: 	 Closed
Reason: ECONNREFUSED
Checking port 22 ...
Port 22: 	 Closed
Reason: ECONNREFUSED
Checking port 80 ...
Port 80: 	 Closed
Reason: ECONNREFUSED
Checking port 8080 ...
Port 8080: 	 Closed
Reason: ECONNREFUSED
Checking port 443 ...
Port 443: 	 Closed
Reason: ECONNREFUSED
Port Scanning Completed in:  0:00:00.002329

To get 80 to return 0:

$ sudo python3 -m http.server 80 -b 127.0.0.1
$ p3 socket_ports_open.py
Enter a host to scan: localhost
(1) Scan a range or (2) Scan a list: 2
Please wait, scanning remote host 127.0.0.1
Checking port 21 ...
Port 21: 	 Closed
Reason: ECONNREFUSED
Checking port 22 ...
Port 22: 	 Closed
Reason: ECONNREFUSED
Checking port 80 ...
Port 80: 	 Open
Checking port 8080 ...
Port 8080: 	 Closed
Reason: ECONNREFUSED
Checking port 443 ...
Port 443: 	 Closed
Reason: ECONNREFUSED
Port Scanning Completed in:  0:00:00.001447


Ex. with a remote host

Enter a remote host to scan: 172.217.168.164
(1) Scan a range or (2) Scan a list: 1
Please enter the range of ports you would like to scan on the machine
Enter a start port: 80
Enter a end port: 83
Please wait, scanning remote host 172.217.168.164
Checking port 80 ...
Port 80: 	 Open
Checking port 81 ...
Port 81: 	 Closed
Reason: EAGAIN
Checking port 82 ...
Port 82: 	 Closed
Reason: EAGAIN
Port Scanning Completed in:  0:00:10.115433
"""
