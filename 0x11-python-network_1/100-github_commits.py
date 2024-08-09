#!/usr/bin/python3
"""Time for an interview!
"""
import requests
import sys


def get_commits(repo_name, owner_name):
    url = f'https://api.github.com/repos/{owner_name}/{repo_name}/commits'
    response = requests.get(url)

    if response.status_code == 200:
        commits = response.json()
        for commit in commits[:10]:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f"{sha}: {author_name}")
    else:
        print(f"""Statuscode: {response.status_code}""")


if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]
    get_commits(repo_name, owner_name)
