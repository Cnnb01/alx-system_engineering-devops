#!/usr/bin/python3
"""

"""
from sys import argv
import requests

if __name__ == "__main__":
    main_url = "https://jsonplaceholder.typicode.com/"
    users_id = argv[1]
    users_id_url = requests.get (url + "users/{}".format(users_id)).json()
    users_todos = requests.get (url + "todos/userId{}".format(users_id)).json()
    total_tasks = len(users_todos)
    user_name = users_id.get("name")
    completed_ts = []
    for t in users_todos:
        if t.get("completed") is True:
            return completed.append(titlee = t.get("title"))
    print("Employee {} is done with tasks({}/{}):".format(
        user_name, completed_ts, total_tasks))

