#!/usr/bin/python3
"""sends a request to the URL and displays the body of the response
(decoded in utf-8)."""

import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as res:
            body = res.read().decode('UTF-8')
        print(body)
    except urllib.error.HTTPError as er:
        print("Error code: {}".format(er.code))
