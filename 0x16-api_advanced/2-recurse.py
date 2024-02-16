#!/usr/bin/python3
"""
Fetches a list of hot articles for a subreddit
"""
import requests
after = None


def recurse(subreddit, hot_list=[]):
    """Returns top ten post titles recursively"""
    global after
    header = {'User-Agent': 'api_advanced-project'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    param = {'after': after}
    resp = requests.get(url, params=param, headers=header,
                        allow_redirects=False)

    if resp.status_code == 200:
        after_data = resp.json().get("data").get("after")
        if after_data is not None:
            after = after_data
            recurse(subreddit, hot_list)
        hot_titles = resp.json().get("data").get("children")
        for hot_title in hot_titles:
            hot_list.append(hot_title.get("data").get("title"))
        return hot_list
    else:
        return (None)
