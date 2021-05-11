#!/usr/bin/env python3

import urllib.request
from urllib.request import Request

url = 'http://python.org'
USER_AGENT = 'Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Mobile Safari/537.36'

def chrome_user_agent():
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-agent', USER_AGENT)]
    urllib.request.install_opener(opener)
    response = urllib.request.urlopen(url)
    print("Response headers")
    print("--------------------")
    for header,value in response.getheaders():
        print(header + ":" + value)

    request = Request(url)
    request.add_header('User-agent', USER_AGENT)
    print("\nRequest headers")
    print("--------------------")
    for header,value in request.header_items():
	    print(header + ":" + value)

if __name__ == '__main__':
    chrome_user_agent()

"""
In this script, we are customizing the User-agent header with a specific version of Chrome browser.

To change User-agent, there are two alternatives:
1. Use the `addheaders` property from the `opener` object.
2. Using the `add_header()` method from the `Request` object to add headers at the same time that we create the request object.

Then we will obtain the site headers through the response object's headers.
* `getheaders()`returns the headers as a list of tuples in the format (header name, header value).

$ p3 get_headers_response_request.py
Response headers
--------------------
Connection:close
Content-Length:49981
Server:nginx
Content-Type:text/html; charset=utf-8
X-Frame-Options:DENY
Via:1.1 vegur, 1.1 varnish, 1.1 varnish
Accept-Ranges:bytes
Date:Tue, 11 May 2021 07:41:56 GMT
Age:2235
X-Served-By:cache-bwi5173-BWI, cache-ewr18168-EWR
X-Cache:HIT, HIT
X-Cache-Hits:3, 1
X-Timer:S1620718917.639960,VS0,VE1
Vary:Cookie
Strict-Transport-Security:max-age=63072000; includeSubDomains

Request headers
--------------------
User-agent:Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Mobile Safari/537.36
"""