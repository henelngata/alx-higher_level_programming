#!/usr/bin/python3
"""Time for an interview!
"""
import requests
import sys

if __name__ == "__main__":
    r = requests.get('https://api.github.com/repos/{}/{}/commits'
                     .format(sys.argv[1], sys.argv[2]))
    resp = r.json()
    for responce in resp:
        sha = responce.get("sha")
        name = responce["commit"]["author"]["name"]
        print("{}: {}".format(sha, name))
