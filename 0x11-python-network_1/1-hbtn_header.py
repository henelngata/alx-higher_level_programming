#!/usr/bin/python3
"""A file that contains urlib methods"""

import urllib.request
import sys

if __name__ == "__main__":
    req = sys.argv[1]
    with urllib.request.urlopen(req) as response:
        pass

    print(response.headers["X-Request-Id"])
