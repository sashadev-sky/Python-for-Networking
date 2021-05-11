#!/usr/bin/env python3

import urllib.request
import urllib.error

def count_words_file(url):
    try:
        file_response = urllib.request.urlopen(url)
    except urllib.error.URLError as error:
        print('Exception', error)
        print('reason', error.reason)
    else:
        content = file_response.read()
        return len(content.split())


print(count_words_file('https://www.gutenberg.org/cache/epub/2000/pg2000.txt'))

count_words_file('https://not-exists.txt')

"""
This script receives the URL of a text file as a parameter and returns the number of words it
contains. If the URL does not exist, then raise the `urllib.error.URLError` exception.

$ p3 count_words_file.py
Exception HTTP Error 406: Not Acceptable
reason Not Acceptable
None
Exception <urlopen error [Errno 8] nodename nor servname provided, or not known>
reason [Errno 8] nodename nor servname provided, or not known
"""