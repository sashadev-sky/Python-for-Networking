import requests

if __name__ == '__main__':
    domain = input('Enter the hostname http://')
    response = requests.get(f'http://{domain}')
    for header in response.headers.keys():
        print(header + ":" + response.headers[header])

"""
$ p3 requests_headers_keys.py
Enter the hostname http: // python.org
Connection: keep-alive
Content-Length: 49828
Server: nginx
Content-Type: text/html
charset = utf-8
X-Frame-Options: DENY
Via: 1.1 vegur, 1.1 varnish, 1.1 varnish
Accept-Ranges: bytes
Date: Tue, 11 May 2021 08: 10: 29 GMT
Age: 348
X-Served-By: cache-bwi5132-BWI, cache-ewr18165-EWR
X-Cache: HIT, HIT
X-Cache-Hits: 1, 1
X-Timer: S1620720629.373086, VS0, VE0
Vary: Cookie
Strict-Transport-Security: max-age = 63072000
includeSubDomains
"""