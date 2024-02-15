#!/usr/bin/python3
"""
Fetches number of subscribers for a subreddit
"""

from requests import get


def number_of_subscribers(subreddit):
    """
    Queries Reddit API to return no. of subreddit subscribers
    """

    if subreddit is None or not isinstance(subreddit, str):
        return 0

    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {"User-Agent": "Google Chrome Version 81.0.4044.129"}

    resp = get(url, headers=headers)

    res = resp.json()

    subscribers = data["data"]["subscribers"]
    try:
        return subscribers

    except Exception:
        return 0
