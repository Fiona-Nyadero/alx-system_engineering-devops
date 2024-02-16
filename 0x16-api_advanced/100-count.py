#!/usr/bin/python3
"""Queries the Reddit API and parses it for given keywords"""

import json
import requests


def count_words(subreddit, word_list, after="", count=[]):
    """Count appearance of keywords on hot articles' titles"""

    if after == "":
        count = [0] * len(word_list)

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    reqst = requests.get(url,
                         params={'after': after},
                         allow_redirects=False,
                         headers={'user-agent': 'bhalut'})

    if reqst.status_code == 200:
        data = reqst.json()

        for topic in (data['data']['children']):
            for word in topic['data']['title'].split():
                for keyword in range(len(word_list)):
                    if word_list[keyword].lower() == word.lower():
                        count[keyword] += 1

        after = data['data']['after']
        if after is None:
            save = []
            for keyword in range(len(word_list)):
                for kw in range(keyword + 1, len(word_list)):
                    if word_list[keyword].lower() == word_list[kw].lower():
                        save.append(kw)
                        count[keyword] += count[kw]

            for keyword in range(len(word_list)):
                for kw in range(keyword, len(word_list)):
                    if (count[kw] > count[keyword] or
                            (word_list[keyword] > word_list[kw] and
                             count[kw] == count[keyword])):
                        aux = count[keyword]
                        count[keyword] = count[kw]
                        count[kw] = aux
                        aux = word_list[keyword]
                        word_list[keyword] = word_list[kw]
                        word_list[kw] = aux

            for keyword in range(len(word_list)):
                if (count[keyword] > 0) and keyword not in save:
                    print("{}: {}".format(word_list[keyword].lower(),
                          count[keyword]))
        else:
            count_words(subreddit, word_list, after, count)
