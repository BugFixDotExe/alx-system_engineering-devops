#!/usr/bin/python3
"""This script strives to  queries the Reddit API
and returns the number of subscribers
(not active users, total subscribers)
for a given subreddit."""

import requests


def number_of_subscribers(subreddit):
    """
        number_of_subscribers: a func that retirves the count of subscribers
        Args:
            subreddit(string): a string of a valid subreddit
        Return:
            An int of the number of subscribers or 0 for none
    """
    response = requests.get(f'https://www.reddit.com/r/{subreddit}/about.json',
                            allow_redirects=False)
    if response.status_code == requests.codes.ok:
        response = response.json()
        for key, value in response.items():
            if key == "data":
                sub_count = response.get("data").get("subscribers")
                return (sub_count)
    return (0)
