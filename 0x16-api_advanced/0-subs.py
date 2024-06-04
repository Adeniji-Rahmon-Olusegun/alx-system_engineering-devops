#!/usr/bin/python3
"""Module contains function to pull number of subcribers from Reddit API"""

import requests

def number_of_subscribers(subreddit):
    """Pull number of subcribers from Reddit API"""

    url = f"https://www.reddit.com/r/{subreddit}"

    headers = {'User-Agent': 'Sub Agent'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        if response.status_code == 200:
            data_info = response.json()

            return data_info['data']['subscriber']
        else:
            return 0

    except requets.RequestException:
        return 0

