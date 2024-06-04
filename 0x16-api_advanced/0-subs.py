#!/usr/bin/python3
"""Module for task 0"""


def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers
    to the subreddit"""
    import requests

    data_info = requests.get("https://www.reddit.com/r/{}/about.json"
                            .format(subreddit),
                            headers={"User-Agent": "My-User-Agent"},
                            allow_redirects=False)
    if data_info.status_code >= 300:
        return 0

    return data_info.json().get("data").get("subscribers")

"""
#!/usr/bin/python3
Module contains function to pull number of subcribers from Reddit API


def number_of_subscribers(subreddit):
    
    Pull number of subcribers from Reddit API

    Args:
        subreddit (str): Name of the subreddit

    Returns:
        int: Number of subscribers if subreddit is valid and 0 otherwise
    

    import requests

    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    header = {'User-Agent': 'Custom-User-Agent'}

    try:
        response = requests.get(url, headers=header, allow_redirects=False)

        if response.status_code == 200:
            data_info = response.json()

            return data_info.get('data').get('subscribers')
        else:
            return 0

    except requests.RequestException:
        return 0
"""