#!/usr/bin/python3
"""Module contains script to fetch employee ID"""

import json
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

    file_name = f"{user_id}.json"

    req_format = {
            user_id: [{
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": employee
            } for task in tasks]
    }

    with open(file_name, "w") as file_obj:
        json.dump(req_format, file_obj)
