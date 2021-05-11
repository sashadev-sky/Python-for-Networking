import urllib.request
import urllib.parse

#POST request

data_dictionary = {'id': '0123456789'}
data = urllib.parse.urlencode(data_dictionary)
data = data.encode('ascii')

with urllib.request.urlopen('http://httpbin.org/post', data) as response:
	print(response.read().decode())

"""
$ p3 urllib_post_request.py
{
  "args": {},
  "data": "",
  "files": {},
  "form": {
    "id": "0123456789"
  },
  "headers": {
    "Accept-Encoding": "identity",
    "Content-Length": "13",
    "Content-Type": "application/x-www-form-urlencoded",
    "Host": "httpbin.org",
    "User-Agent": "Python-urllib/3.9",
    "X-Amzn-Trace-Id": "Root=1-609a31d8-0c838507115597be5be46519"
  },
  "json": null,
  "origin": "96.250.166.132",
  "url": "http://httpbin.org/post"
}
"""