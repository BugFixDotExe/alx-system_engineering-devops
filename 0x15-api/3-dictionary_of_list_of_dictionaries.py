#!/usr/bin/python3
# -*- coding: utf-8 -*-
""" A Python script to export data in the CSV format
Records all tasks from all employees """
import json
import requests


parent_dict = {}
user_ids = []
if __name__ == "__main__":
    # My chocice to not loop is the /users endpoint returns a single dictionary
    # This contains a unique "name" value there was no need.
    base_end_point = "https://jsonplaceholder.typicode.com/users"
    try:
        user_content = requests.get(f"{base_end_point}")
        if user_content.status_code:
            user_content = user_content.json()
            for content in user_content:
                user_ids.append(content.get("id"))
                parent_dict[content.get("id")] = []
    except Exception as Bugfixdotexe:
        print("Error SON!")

    # My choice to loop thourgh the items is due to the return value of /todos
    # the endpoint returns multiple objects or items, which contain what i need

    try:
        for ids in user_ids:
            user_content = requests.get(f"{base_end_point}/{ids}")
            user_content = user_content.json()
            user_todo_content = requests.get(f"{base_end_point}/{ids}/todos")
            if user_todo_content.status_code:
                user_todo_content = user_todo_content.json()
                for content in user_todo_content:
                    child_dict = {}
                    child_dict["task"] = content.get("title")
                    child_dict["completed"] = content.get("completed")
                    child_dict["username"] = user_content.get("username")
                    parent_dict[content.get("userId")].append(child_dict)
        json_string = json.dumps(parent_dict)
        with open("todo_all_employees.json",
                  mode="a",
                  encoding="UTF-8") as outfile:
            outfile.write(json_string)
    except Exception as Bugfixdotexe:
        print("Error SON!")
