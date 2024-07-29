#!/usr/bin/python3
# -*- coding: utf-8 -*-
""" A Python script to export data in the CSV format."""
import csv
import requests
import sys


if __name__ == "__main__":
    """ Expected args <program name> <user_id>"""
    if len(sys.argv) != 2:
        pass

    # My chocice to not loop is the /users endpoint returns a single dictionary
    # This contains a unique "name" value there was no need.
    base_end_point = "https://jsonplaceholder.typicode.com/users/"
    try:
        user_content = requests.get(f"{base_end_point}{sys.argv[1]}/")
        if user_content.status_code:
            user_content = user_content.json()
            user_id = user_content.get("id")
            user_user_name = user_content.get("username")
    except Exception as Bugfixdotexe:
        print("Error SON!")

    # My choice to loop thourgh the items is due to the return value of /todos
    # the endpoint returns multiple objects or items, which contain what i need

    try:
        user_content = requests.get(f"{base_end_point}{sys.argv[1]}/todos")
        if user_content.status_code:
            user_content = user_content.json()
            for content in user_content:
                with open(f'{content.get("userId")}.csv',
                          mode="a",
                          encoding="UTF-8") as file:
                    writer = csv.writer(file, quoting=csv.QUOTE_ALL)
                    writer.writerow(
                            [content.get("userId"),
                             user_user_name,
                             content.get("completed"),
                             content.get("title")])
    except Exception as Bugfixdotexe:
        print("Error SON!")
