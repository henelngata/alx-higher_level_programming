#!/usr/bin/python3
"""
script that takes in a letter and sends a
POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""
import requests
import sys

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) > 1:
        letter = sys.argv[1]
        q = letter
        r = requests.post(url, data={'q': q})
        try:
            res = r.json()
            if len(res) > 0:
                print("[{}] {}".format(res["id"], res["name"]))
            else:
                print("No result")
        except ValueError:
            print("Not a valid JSON")
    else:
        q = ""
        r = requests.post(url, data={'q': q})
        try:
            res = r.json()
            if len(res) > 0:
                print("[{}] {}".format(res.get(["id"]), res.get(["name"])))
            else:
                print("No result")
        except ValueError:
            print("Not a valid JSON")
