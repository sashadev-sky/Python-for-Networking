#!/usr/bin/python

from socket import (socket, gethostname, gethostbyname, gethostbyaddr,
                    getfqdn, getaddrinfo, gethostbyname_ex, SOCK_STREAM)

try:
    # Return the current host name.
    print("gethostname:", gethostname())
    # Return the IP address(a string of the form '255.255.255.255') for a host.
    print("gethostbyname:", gethostbyname('Locals-MBP.fios-router.home'))
    # Return the true host name, a list of aliases, and a list of IP addresses, for a host.
    print("gethostbyname_ex:", gethostbyname_ex('Locals-MBP.fios-router.home'))
    print("gethostbyaddr", gethostbyaddr('192.168.1.246'))
    print("gethostbyname:", gethostbyname('blahnotreal'))
    print("gethostbyname_ex:", gethostbyname_ex('blahnotreal'))
    print("gethostbyaddr", gethostbyaddr('blahnotreal'))
    print("gethostbyaddr", gethostbyaddr('92.242.140.21'))
    print("gethostbyname", gethostbyname('www.google.com'))
    print("gethostbyname_ex", gethostbyname_ex('www.google.com'))
    # gethostbyname_ex() does not support IPv6 name resolution,
    # and getaddrinfo() should be used instead for IPv4/v6 dual stack support.
    print("gethostbyaddr", gethostbyaddr('8.8.8.8'))
    print("getfqdn", getfqdn('www.google.com'))
    print("getaddrinfo", getaddrinfo(
        "www.google.com", None, 0, SOCK_STREAM))

except socket.error as error:
    print(str(error))
    print("Connection error")

"""
$ p3 socket_methods.py
gethostname: Locals-MBP.fios-router.home

### Locals-MBP.fios-router.home ###

gethostbyname: 192.168.1.246
gethostbyname_ex: ('locals-mbp.fios-router.home', [], ['192.168.1.246'])
gethostbyaddr ('locals-mbp.fios-router.home', ['246.1.168.192.in-addr.arpa'], ['192.168.1.246'])

### blahnotreal ###

gethostbyname: 92.242.140.21
gethostbyname_ex: ('blahnotreal', [], ['92.242.140.21'])
gethostbyaddr ('unallocated.barefruit.co.uk', ['21.140.242.92.in-addr.arpa'], ['92.242.140.21'])

### www.google.com ###

gethostbyname 172.217.165.132
gethostbyname_ex ('www.google.com', [], ['172.217.165.132'])
gethostbyaddr ('dns.google', ['8.8.8.8.in-addr.arpa'], ['8.8.8.8'])

getfqdn lga25s70-in-f4.1e100.net
getaddrinfo [(<AddressFamily.AF_INET: 2>, <SocketKind.SOCK_STREAM: 1>, 6, '', ('172.217.165.132', 0))]
"""
