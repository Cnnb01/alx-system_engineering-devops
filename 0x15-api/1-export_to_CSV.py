#!/usr/bin/python3
"""
This script fetches and displays information about an
employee's todo list progress.
"""
from requests import get
from sys import argv

if __name__ == "__main__":
    users_id = argv[1]

    # fething user's info
    users_url = "https://jsonplaceholder.typicode.com/users/{}".format
    (users_id)
    response = get(users_url)
    username = response.json().get("username")

    # fething user's todo list
    users_todos = "https://jsonplaceholder.typicode.com/users/{}/todos".format
    (users_id)
    response = get(users_todos)
    tasks = response.json()

    with open('{}.csv'.format(users_id), 'w') as file:
        for task in tasks:
            file.write('"{}","{}","{}","{}"\n'
                       .format(users_id, username, task.get('completed'),
                               task.get('title')))
