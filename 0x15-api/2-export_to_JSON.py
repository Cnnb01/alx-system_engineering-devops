#!/usr/bin/python3
"""
This script fetches and displays information about an
employee's todo list progress as a json.
"""
from json import dump
from requests import get
from sys import argv

if __name__ == "__main__":
    users_id = argv[1]

    # fething user's info
    url = "https://jsonplaceholder.typicode.com/users/{}".format(users_id)
    response = get(url)
    username = response.json().get("username")

    # fething user's todo list
    td = "https://jsonplaceholder.typicode.com/users/{}/todos".format(users_id)
    response = get(td)
    tasks = response.json()
    dictionary = {users_id: []}
    for task in tasks:
        dictionary[users_id].append({
                                    "task": task.get('title'),
                                    "completed": task.get('completed'),
                                    "username": username
                                    })
    with open('{}.json'.format(users_id), 'w') as file:
        dump(dictionary, file)
