#!/usr/bin/python

import urllib.request

print('starting download....')

url = 'https://www.python.org/static/img/python-logo.png'

# download file with urlretrieve
urllib.request.urlretrieve(url, 'python.png')

# download file with urlopen
with urllib.request.urlopen(url) as response:
    print("Status:", response.status)
    print("Downloading python.png")
    with open("python.png", "wb" ) as image:
        image.write(response.read())

"""
Download a file using:
  1. urlretrieve(): use directly
  2. urlopen(): using the returned response

After runniing this script, will see 'python.png' added to this folder

$ p3 download_file.py
starting download....
Status: 200
Downloading python.png
"""