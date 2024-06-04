#!/usr/bin/python3
"""Module contains function to pull top hot articles from Reddit API"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Returns a list containing the titles of
    all hot articles for a given subreddit

    Args:
        subreddit (str): Name of the subreddit
        hot_list (list): List to store title of articles
        after (str): Pagination Identifier to get next set of results
    """

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    header = {'User-Agent': 'Custom-User-Agent'}

    params = {'limit': 100}

    if after:
        params['after'] = after

    response = requests.get(url, headers=header, params=params)

    if response.status_code == 200:
        data_info = response.json()

        articles = data_info['data']['children']

        if not articles:
            return hot_list if hot_list else None

        for article in articles:
            hot_list.append(article['data']['title'])

        after = data_info['data']['after']

        if after:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    elif response.status_code == 404:
        return None
    else:
        return hot_list if hot_list else None
