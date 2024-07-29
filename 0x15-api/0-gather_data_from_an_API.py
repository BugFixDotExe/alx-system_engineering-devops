#!/usr/bin/python3
# -*- coding: utf-8 -*-
""" A Python script that, using this REST API
    for a given employee ID, returns information
    about his/her TODO list progress.
"""
import requests
import sys

completed = 0
pending = 0
task_list = []
if __name__ == "__main__":
    """ Expected args <program name> <user_id>"""
    if len(sys.argv) != 2:
        pass
    # My choice to loop thourgh the items is due to the return value of /todos
    # the endpoint returns multiple objects or items, which contain what i need
    base_end_point = "https://jsonplaceholder.typicode.com/users/"
    try:
        user_content = requests.get(f"{base_end_point}{sys.argv[1]}/todos")
        if user_content.status_code:
            user_content = user_content.json()
            for item in user_content:
                if item.get("completed") is True:
                    completed += 1
                    task_list.append(item.get("title"))
                elif item.get("completed") is False:
                    pending += 1

    except Exception as Bugfixdotexe:
        print("Error SON!")

    # My chocice to not loop is the /users endpoint returns a single dictionary
    # This contains a unique "name" value there was no need.
    try:
        user_content = requests.get(f"{base_end_point}{sys.argv[1]}/")
        if user_content.status_code:
            user_content = user_content.json()
            total_tasks = completed + pending
            print("Employee {} is done with tasks({}/{}):".format(
                user_content.get("name"), completed, total_tasks))
            for task in task_list:
                print("\t {}".format(task))
    except Exception as Bugfixdotexe:
        print("Error SON!")
