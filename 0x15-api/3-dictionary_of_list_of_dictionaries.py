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

    users_info = fetch_info(
            "https://jsonplaceholder.typicode.com/users"
    )

    tasks = fetch_info(
            "https://jsonplaceholder.typicode.com/todos"
    )

    file_name = "todo_all_employees.json"

    user_task = dict()

    for user in users_info:
        user_id = user.get("id")
        user_name = user.get("username")
        tasks_of_user = [
                task for task in tasks if task.get("userId") == user_id
        ]

        user_task[user_id] = [{
            "username": user_name,
            "task": task.get("title"),
            "completed": task.get("completed")
        } for task in tasks_of_user]

    with open(file_name, "w") as file_obj:
        json.dump(user_task, file_obj)
