#!/usr/bin/python3
"""This script strives to  queries the Reddit API
and prints the titles of the first 10 hot posts
listed for a given subreddit
"""

import requests


def top_ten(subreddit):
    headers = {'limit': '10'}
    response = requests.get(f'https://www.reddit.com/r/{subreddit}/top.json',
                            headers, allow_redirects=False)
    if response.status_code == requests.codes.ok:
        response = response.json()
        for key, value in response.items():
            if key == 'data':
                children = response.get('data').get('children')
                for child in children:
                    print(child.get('data').get('title'))
    else:
        print(None)
