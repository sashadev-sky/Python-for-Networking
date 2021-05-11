#!/usr/bin/env python3

import urllib.request
import json

url= 'http://httpbin.org/get'

with urllib.request.urlopen(url) as response_json:
    data_json= json.loads(response_json.read().decode())
    print(data_json)

"""
$ p3 json_response.py
{'args': {}, 'headers': {'Accept-Encoding': 'identity', 'Host': 'httpbin.org', 'User-Agent': 'Python-urllib/3.9', 'X-Amzn-Trace-Id': 'Root=1-609a34ad-1833cebd3a7a0fa17f636558'}, 'origin': '96.250.166.132', 'url': 'http://httpbin.org/get'}
"""