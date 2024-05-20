#!/usr/bin/python3
"""Module contains script to fetch employee ID"""

import requests
import sys


def fetch_info(rest_url):
    """Gets information or data from the desired url"""
    response = requests.get(rest_url)

    response.raise_for_status()

    return response.json()

if __name__ == "__main__":

    user_info = fetch_info(
            f"https://jsonplaceholder.typicode.com/users/{sys.argv[1]}"
    )

    employee = user_info.get("name")

    tasks = fetch_info(
            f"https://jsonplaceholder.typicode.com/todos?userId={sys.argv[1]}"
    )

    finished_tasks = [done.get("title") for done in tasks if done.get("completed")]

    all_task = len(tasks)

    done_tasks = len(finished_tasks)

    print(
            f"Employee {employee} is done with tasks({done_tasks}/{all_task}):"
    )

    for title in finished_tasks:
        print(f"\t {title}")
