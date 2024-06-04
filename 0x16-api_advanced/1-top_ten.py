#!/usr/bin/python3
"""Module contains function to pull top ten hot posts from Reddit API"""


def top_ten(subreddit):
    """
    Prints top ten hot posts for a given subreddit from Reddit API

    Args:
        subreddit (str): Name of the subreddit
    """
    import requests

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"

    header = {'User-Agent': 'Custom-User-Agent'}

    try:
        response = requests.get(url, headers=header, allow_redirects=False)

        if response.status_code == 200:
            data_info = response.json()

            posts = data_info.get('data').get('children')

            for post in posts:
                print(post.get('data').get('title'))
        else:
            print(None)
    except requests.RequestException:
        return 0
