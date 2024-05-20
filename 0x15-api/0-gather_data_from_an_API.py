#!/usr/bin/python3
"""
This script fetches and displays information about an
employee's todo list progress.
"""
import requests
from sys import argv

if __name__ == "__main__":
    main_url = "https://jsonplaceholder.typicode.com/"
    users_id = argv[1]

    # fething user's info
    users_info = requests.get(main_url + "users/{}".format(users_id)).json()
    user_name = users_info.get("name")

    # fething user's todo list
    users_todos = requests.get(main_url + "todos?userId={}"
                               .format(users_id)).json()
    total_tasks = len(users_todos)

    # putting comp tasks in list
    completed_ts = [t for t in users_todos if t.get("completed") is True]
    num_completed_ts = len(completed_ts)

    print("Employee {} is done with tasks({}/{}):".format(
        user_name, num_completed_ts, total_tasks))

    for ts in completed_ts:
        print("\t {}".format(ts.get("title")))
