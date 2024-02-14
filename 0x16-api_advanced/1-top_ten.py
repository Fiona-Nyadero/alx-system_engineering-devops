#!/usr/bin/python3
"""
Fetches top 10 hot posts for a subreddit
"""

from requests import get


def top_ten(subreddit):
    """
    Queries Reddit API for list of top 10 hot posts
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {"User-Agent": "My API Client"}
    params = {'limit': 10}

    resp = get(url, headers=headers, params=params)

    if resp.status_code == 200:
        data = resp.json()
        hotPosts = data["data"]["children"]

        for hotPost in hotPosts:
            posttitle = hotPost["data"]["title"]
            print(posttitle)

    else:
        print("None")
