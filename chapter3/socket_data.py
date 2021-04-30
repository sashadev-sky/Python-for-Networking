#!/usr/bin/python


# 1. Create a socket object with the AF_INET and SOCK_STREAM parameters:

from socket import AF_INET, SOCK_STREAM, socket

print('creating socket ...')
# s = socket(AF_INET, SOCK_STREAM)
s = socket()
print(f'socket created: {repr(s)}')
print("connection with remote host")

target_host = "www.google.com"
target_port = 80

"""
If we were to plug in a port that is not accepting connections
for example just pick a random port number that is not a classic like 80,
the script will hang and we will never hit 'connection ok'.
"""

s.connect((target_host, target_port))
print(f'connection ok: {repr(s)}')

# 2. Then connect the client to the remote host and send it some data:

request = "GET / HTTP/1.1\r\nHost:%s\r\n\r\n" % target_host

# The encode() method encodes the string, using the specified encoding.
# If no encoding is specified, UTF-8 will be used.

s.send(request.encode())

# 3. The last step is to receive some data back and print out the response:

# Using the recv() method from the socket object to receive
# the response from the server in the data variable.

data = s.recv(4096)

print(f"Size: {len(data)}")

print("Data", str(bytes(data)))
print("Length", len(data))

print('closing the socket')
s.close()

"""
$ p3 socket_data.py
creating socket ...
socket created: <socket.socket fd=3, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('0.0.0.0', 0)>
connection with remote host
connection ok
Data b'HTTP/1.1 200 OK\r\nDate: Thu, 29 Apr 2021 22:32:37 GMT\r\nExpires: -1\r\nCache-Control: private, max-age=0\r\nContent-Type: text/html; charset=ISO-8859-1\r\nP3P: CP="This is not a P3P policy! See g.co/p3phelp for more info."\r\nServer: gws\r\nX-XSS-Protection: 0\r\nX-Frame-Options: SAMEORIGIN\r\nSet-Cookie: 1P_JAR=2021-04-29-22; expires=Sat, 29-May-2021 22:32:37 GMT; path=/; domain=.google.com; Secure\r\nSet-Cookie: NID=214=DwNWq3l4SAUiH-H4BOaudw2ejGFAeYrH22wk3qD3avHrthblzYyzfMMveuyHnlCra4YmDzrPyeazqSqgukUihvH8SShUy9g2Zn03YNmTjZrcDgnfiQTCA0jT3grvBX1txlsPrpMY1-rcjllMUpv23zVxe-CcwqpJ9cny_cpuRw4; expires=Fri, 29-Oct-2021 22:32:37 GMT; path=/; domain=.google.com; HttpOnly\r\nAccept-Ranges: none\r\nVary: Accept-Encoding\r\nTransfer-Encoding: chunked\r\n\r\n50d3\r\n<!doctype html><html itemscope="" itemtype="http://schema.org/WebPage" lang="en"><head><meta content="Search the world\'s information, including webpages, images, videos and more. Google has many special features to help you find exactly what you\'re looking for." name="description"><meta content="noodp" name="robots"><meta content="text/html; charset=UTF-8" http-equiv="Content-Type"><meta content="/images/branding/googleg/1x/googleg_standard_color_128dp.png" itemprop="image"><title>Google</title><script nonce="TTNTZ8SCuIckrYRJDixqNg==">(function(){window.google={kEI:\'BTSLYJTiA5Pj5NoPxsyCeA\',kEXPI:\'0,1302536,56873,954,5105,206,4804,2316,383,246,5,1354,4936,314,16231,10,1106275,1233,1196491,558,43,1,328941,51224,16114,19398,9286,17572,4858,1362,9290,3023,2821,1924,12841,4020,978,13228,2054,1793,4192,6430,1142,13385,4518,2777,919,2277,8,2796,1593,1279,2212,530,149,1943,517,1466,56,4258,109,3405,606,2023,1777,520,4269,328,1284,8789,605,2624,2843,7,5599,6755,5096,7876,3748,1181,108,1483,1924,908,2,941,5011,7468,1,2844,432,3,1590,1,820,1,4624,148,5990,5333,2647,4,504,1029,2304,1238,5225,576,74,1717,266,2626,2015,4067,7434,2110,1714,1297,1753,2658,4243,518,912,564,1119,31,3854,4275,3285,2214,1590,715,638,37,7043,9765,763,672,651,1494,3667,413,2132,2953,1141,20,3118,6,908,3,1902,1639,1,4174,1175,726,3273,5368,1,1809,36,245,38,874,60,5932,1260,1194,2,367,2171,1760,402,30,2859,1351,1130,2,1394,756,769,8,1,1272,1715,2,488,1922,647,2548,2713,454,440,627,4,32,4,59,3,471,1710,2,557,2384,295,530,2,61,174,268,176,166,88,167,493,354,2,593,504,467,456,80,14,30,169,1845,287,578,696,1262,69,1070,1771,406,43,1672,378,254,194,127,1029,563,225,2,2,2,659,569,2,885,2,848,251,683,13,863,54,92,1,3,211,1304,527,165,834,782,879,108,274,1,201,1817,96,1001,679,331,674,5653821,13,3892,226,63,30,8797692,882,444,1,2,80,1,1796,1,9,2,2551,1,748,141,795,563,1,4265,1,1,2,1331,3299,843,1,2608,155,17,13,72,139,4,2,20,2,169,13,19,46,5,39,96,73,4,47,160,4,4,4,4,4,4,8,4,4,4,24,68,128,29,2,2,1,2,1,2,2,7,4,1,2,4,2,59,31,2,6,51,1,24,17,5,42,60,4,13,21,6,23955890,150,2774104,1236020,268,26800,579,2,832,2319,1'
Length 2836
closing the socket
"""
