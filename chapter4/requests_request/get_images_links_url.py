#!/usr/bin/env python3

import requests
import re

url = input("Enter URL > ")
var = requests.get(url).text

print("Images:")
print("#########################")
for image in re.findall("<img (.*)>", var):
    for images in image.split():
        if re.findall("src=(.*)", images):
            image = images[:-1].replace("src=\"", "")
            if(image.startswith("http")):
                print(image)
            else:
                print(url+image)

print("#########################")
print("Links:")
print("#########################")
for link, name in re.findall("<a (.*)>(.*)</a>", var):
    for a in link.split():
        if re.findall("href=(.*)", a):
            url_image = a[0:-1].replace("href=\"", "")
            if(url_image.startswith("http")):
                print(url_image)
            else:
                print(url+url_image)

"""
Extract images and links using requests and regular expressions modules.
The easy way to extract images from a URL is to use the re module to
find img and href HTML elements in the target URL.

$ p3 get_images_links_url.py
Enter URL > http://python.org
Images:
#########################
http://python.org/static/img/python-logo.png
#########################
Links:
#########################
http://browsehappy.com/
http://python.org#content
http://python.org/
http://python.org/psf-landing/
https://docs.python.org
https://pypi.org/
http://python.org/jobs/
http://python.org/community-landing/
http://python.org/"><im
https://psfmember.org/civicrm/contribute/transact?reset=1&id=2
http://python.org#site-map"><spa
http://python.org#
http://python.orgjavascript:;
http://python.orgjavascript:;
http://python.orgjavascript:;
http://python.org#
https://www.facebook.com/pythonlang?fref=ts"><spa
https://twitter.com/ThePSF"><spa
http://python.org/community/irc/"><spa
http://python.org/about/
http://python.org/about/apps/
http://python.org/about/quotes/
http://python.org/about/gettingstarted/
http://python.org/about/help/
...//
"""
