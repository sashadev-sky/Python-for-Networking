#!/usr/bin/env python
import subprocess
import sys
import argparse

parser = argparse.ArgumentParser(description='Ping Scan Network')

# Main arguments
parser.add_argument("-network", dest="network",
                    help="NetWork segment[For example 192.168.56]", required=True)
parser.add_argument("-machines", dest="machines",
                    help="Machines number", type=int, required=True)

parsed_args = parser.parse_args()

for ip in range(1, parsed_args.machines+1):
    ipAddress = parsed_args.network + '.' + str(ip)
    print("Scanning %s " % (ipAddress))
    if not sys.platform.startswith('win'):
        output = subprocess.Popen(
            ['/sbin/ping', '-c 1', ipAddress], stdout=subprocess.PIPE).communicate()[0]
    else:
        output = subprocess.Popen(
            ['ping', ipAddress], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
    output = output.decode('utf-8')
    print("Output", output)
    if "Lost = 0" in output or "bytes from " in output:
        print("The Ip Address %s has responded with a ECHO_REPLY!" % ipAddress)


"""
Pass as parameters the network we are analyzing
and the numbers of machines we want to check inside this network:

$ python3 ping_scan_network.py - network 192.168.56 - machines 5

ex: scan five machines on the network at 192.168.56

Scanning 192.168.56.1
Output PING 192.168.56.1 (192.168.56.1): 56 data bytes

--- 192.168.56.1 ping statistics ---
1 packets transmitted, 0 packets received, 100.0% packet loss

Scanning 192.168.56.2
Output PING 192.168.56.2 (192.168.56.2): 56 data bytes

--- 192.168.56.2 ping statistics ---
1 packets transmitted, 0 packets received, 100.0% packet loss

Scanning 192.168.56.3
Output PING 192.168.56.3 (192.168.56.3): 56 data bytes

--- 192.168.56.3 ping statistics ---
1 packets transmitted, 0 packets received, 100.0% packet loss

Scanning 192.168.56.4
Output PING 192.168.56.4 (192.168.56.4): 56 data bytes

--- 192.168.56.4 ping statistics ---
1 packets transmitted, 0 packets received, 100.0% packet loss

Scanning 192.168.56.5
Output PING 192.168.56.5 (192.168.56.5): 56 data bytes

--- 192.168.56.5 ping statistics ---
1 packets transmitted, 0 packets received, 100.0% packet loss
"""
