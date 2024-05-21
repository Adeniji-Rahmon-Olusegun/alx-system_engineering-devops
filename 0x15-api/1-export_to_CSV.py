#!/usr/bin/python3
"""Module contains script to fetch employee ID"""

import csv
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

    employee = user_info.get("username")

    tasks = fetch_info(
            f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"
    )

    file_name = f"{user_id}.csv"

    with open(file_name, mode="w", newline="") as file_obj:
        write_csv = csv.writer(file_obj, quoting=csv.QUOTE_ALL)
        for task in tasks:
            write_csv.writerow(
                    [
                        user_id,
                        employee,
                        task.get("completed"),
                        task.get("title")
                    ]
            )
