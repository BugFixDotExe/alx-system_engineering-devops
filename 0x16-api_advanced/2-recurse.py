#!/usr/bin/python3
"""This script that queries the Reddit API
returns a list containing the titles of all
hot articles for a given subreddit, done
recursively.
"""

import requests


def recurse(subreddit, hot_list=[]):
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
