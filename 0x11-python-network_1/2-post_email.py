#!/usr/bin/python3
"""A file that contains urlib methods"""

import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    value = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(value)
    data = data.encode('UTF-8')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        email = response.read()
    print(email.decode('UTF-8'))
