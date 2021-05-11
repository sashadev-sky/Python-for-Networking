#!/usr/bin/python

from socket import (gethostname, gethostbyname, gethostbyaddr,
                    getfqdn, getaddrinfo, gethostbyname_ex, SOCK_STREAM)

hostnames = [gethostname(), 'www.google.com']

for host in hostnames:
    # Get the primary, fully qualified domain name and IP address
    name = getfqdn(host)
    addr = gethostbyname(name)
    print('\nhostname:', host, '\nfqdn:', name, '\naddr:', addr, '\n')

    # Might have other names and addresses, and if you want to find out about them, you can do the following:
    the_name, aliases, addresses = gethostbyaddr(addr)
    print('Primary name for %s (%s): %s' % (host, addr, the_name))
    for alias in aliases: print('AKA', alias)
    for address in addresses: print('address:', address)

    print('\ngetaddrinfo', f'{host}:', getaddrinfo(host, None, type=SOCK_STREAM))

"""
$ p3 socket_methods.py

hostname: MacingtonProlll.fios-router.home
fqdn: macingtonprolll.fios-router.home
addr: 192.168.1.155

Primary name for MacingtonProlll.fios-router.home (192.168.1.155): macingtonprolll.fios-router.home
AKA 155.1.168.192.in-addr.arpa
address: 192.168.1.155

getaddrinfo MacingtonProlll.fios-router.home: [(<AddressFamily.AF_INET: 2>, <SocketKind.SOCK_STREAM: 1>, 6, '', ('192.168.1.155', 0))]

hostname: www.google.com
fqdn: lga34s18-in-f4.1e100.net
addr: 172.217.3.100

Primary name for www.google.com (172.217.3.100): lga34s18-in-f4.1e100.net
AKA 100.3.217.172.in-addr.arpa
address: 172.217.3.100

getaddrinfo www.google.com: [(<AddressFamily.AF_INET: 2>, <SocketKind.SOCK_STREAM: 1>, 6, '', ('172.217.3.100', 0))]
"""
