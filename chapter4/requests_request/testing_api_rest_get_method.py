import requests
import json

response = requests.get("http://httpbin.org/get", timeout=5)

print("HTTP Status Code: " + str(response.status_code))
print(response.headers)

if response.status_code == 200:

    results = response.json()
    for result in results.items():
	    print(result)

    print()
    print("Headers response: ")
    for header, value in response.headers.items():
	    print(header, '-->', value)
    print()
    print("Headers request : ")
    for header, value in response.request.headers.items():
	    print(header, '-->', value)

    print("Server:" + response.headers['server'])
else:
	print("Error code %s" % response.status_code)

"""
$ p3 testing_api_rest_get_method.py

HTTP Status Code: 200
{'Date': 'Tue, 11 May 2021 08:15:39 GMT', 'Content-Type': 'application/json', 'Content-Length': '307', 'Connection': 'keep-alive', 'Server': 'gunicorn/19.9.0', 'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Credentials': 'true'}
('args', {})
('headers', {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Host': 'httpbin.org', 'User-Agent': 'python-requests/2.25.1', 'X-Amzn-Trace-Id': 'Root=1-609a3d2b-14a1a0fa074d33e00492ef2c'})
('origin', '96.250.166.132')
('url', 'http://httpbin.org/get')
Headers response:
Date --> Tue, 11 May 2021 08:15:39 GMT
Content-Type --> application/json
Content-Length --> 307
Connection --> keep-alive
Server --> gunicorn/19.9.0
Access-Control-Allow-Origin --> *
Access-Control-Allow-Credentials --> true
Headers request :
User-Agent --> python-requests/2.25.1
Accept-Encoding --> gzip, deflate
Accept --> */*
Connection --> keep-alive
Server:gunicorn/19.9.0
"""
