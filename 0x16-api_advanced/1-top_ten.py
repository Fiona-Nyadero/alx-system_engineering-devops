#!/usr/bin/python3

"""
Fetches top 10 hot posts for a subreddit
"""

from requests import get


def top_ten(subreddit):
    """
    Queries Reddit API for list of top 10 hot posts
    """

    if subreddit is None or not isinstance(subreddit, str):
        print("None")

    header = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    param = {'limit': 10}
    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)

    resp = get(url, headers=header, params=param)
    res = resp.json()

    try:
        hot_posts = res.get('data').get('children')

        for hot_post in hot_posts:
            print(hot_post.get('data').get('title'))

    except Exception:
        print("None")
