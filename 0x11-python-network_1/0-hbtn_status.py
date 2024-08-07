#!/usr/bin/python3
"""A file that contains urlib methods"""

import urllib.request

if __name__ == "__main__":
    req = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(req) as response:
        html = response.read()

    print('Body response:')
    print('\t- type: {}'.format(type(html)))
    print('\t- content: {}'.format(html))
    print('\t- utf8 content: {}'.format(html.decode('UTF-8')))
