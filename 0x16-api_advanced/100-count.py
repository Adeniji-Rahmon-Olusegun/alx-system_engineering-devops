#!/usr/bin/python3
"""Module contains functions count_words and sorted_counts_prints"""

from collections import Counter
import re
import requests


def count_words(subreddit, word_list=[], counts=None, after=None):
    """
    Parses the title of all hot articles,
    and prints a sorted count of given keywords
    by quering the Reddit API

    Args:
        subreddit (str): Name of the subreddit
        word_list (list): List to store title of articles
        counts: Stores counts of unique keywords
        after (str): Pagination Identifier to get next set of results
    """
    if counts is None:
        counts = Counter()

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    header = {'User-Agent': 'Custom-User-Agent'}

    params = {'limit': 100}

    if after:
        params['after'] = after

    response = requests.get(url, headers=header, params=params)

    if response.status_code != 200:
        return counts

    data_info = response.json()

    articles = data_info['data']['children']

    if not articles:
        return counts

    collection_word_list = [word.lower() for word in word_list]
    unique_word_list = set(collection_word_list)

    for article in articles:
        title = article['data']['title'].lower()
        word_title = re.findall(r'\b\w+\b', title)

        for word in word_title:
            if word in unique_word_list:
                counts[word] += 1

    after = data_info['data']['after']

    if after:
        return count_words(subreddit, word_list, counts, after)
    else:
        return counts


def sorted_counts_prints(counts):
    sort_counts = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    for word, count in sort_counts:
        if count > 0:
            print(f"{word}: {count}")
