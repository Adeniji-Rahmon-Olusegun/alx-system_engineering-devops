#!/usr/bin/python3
"""Module contains script to fetch employee ID"""

import requests
import sys


def fetch_info(rest_url):
    """Gets information or data from the desired url"""
    response = requests.get(rest_url)

    return response.json()


if __name__ == "__main__":

    user_id = int(sys.argv[1])
    user_info = fetch_info(
            f"https://jsonplaceholder.typicode.com/users/{user_id}"
    )

    employee = user_info.get("name")

    tasks = fetch_info(
            f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"
    )

    finished_tasks = [done.get("title") for done in tasks if done.get("completed")]

    all_task = len(tasks)

    done_tasks = len(finished_tasks)

    print(
            f"Employee {employee} is done with tasks({done_tasks}/{all_task}):"
    )

    for title in finished_tasks:
        print(f"\t {title}")
