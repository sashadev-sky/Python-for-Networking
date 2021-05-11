#!/usr/bin/env python3

import requests

domain = input('Enter the hostname http://')
response = requests.get(f'http://{domain}')
print(response.json)
print(f'Status code: {response.status_code}')

print()

print('Headers response: ')
for header, value in response.headers.items():
  print(header, '-->', value)

print()

print('Headers request: ')
for header, value in response.request.headers.items():
  print(header, '-->', value)

"""
$ p3 requests_headers.py
Enter the hostname http://python.org
<bound method Response.json of <Response [200]>>
Status code: 200

Headers response:
Connection --> keep-alive
Content-Length --> 49981
Server --> nginx
Content-Type --> text/html; charset=utf-8
X-Frame-Options --> DENY
Via --> 1.1 vegur, 1.1 varnish, 1.1 varnish
Accept-Ranges --> bytes
Date --> Tue, 11 May 2021 08:04:14 GMT
Age --> 3573
X-Served-By --> cache-bwi5173-BWI, cache-ewr18180-EWR
X-Cache --> HIT, HIT
X-Cache-Hits --> 3, 2
X-Timer --> S1620720254.108184,VS0,VE0
Vary --> Cookie
Strict-Transport-Security --> max-age=63072000; includeSubDomains

Headers request:
User-Agent --> python-requests/2.25.1
Accept-Encoding --> gzip, deflate
Accept --> */*
Connection --> keep-alive
"""
