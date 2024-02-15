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

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "My API Client"}

    resp = get(url, headers=headers)

    if resp.status_code == 200:
        data = resp.json()
        subscribers = data["data"]["subscribers"]
        return subscribers
    else:
        return 0
