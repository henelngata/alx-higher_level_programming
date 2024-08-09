#!/usr/bin/python3
"""fetches url with requests"""

import requests

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    body = requests.get(url).text
    print('Body response:')
    print('\t- type: {}'.format(type(body)))
    print('\t- content: {}'.format((body)))
