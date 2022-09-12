#!/usr/bin/python3
"""This is a comment"""

import requests
import sys

if __name__ == "__main__":
    ID = sys.argv[1]
    todoCountComplete = 0
    todoCount = 0
    i = 0
    link = "https://jsonplaceholder.typicode.com/"
    api_url = "{}users/{}/todos?completed=true".format(link, ID)
    name = requests.get("{}users/{}".format(link, ID)).json()['name']
    todo_url = requests.get("{}users/{}/todos".format(link, ID)).json()
    todoComplete = requests.get(api_url).json()
    while todoCountComplete < len(todoComplete):
        todoCountComplete += 1
    while todoCount < len(todo_url):
        todoCount += 1
    print("Employee {} is done with tasks ({}/{}):"
          .format(name, todoCountComplete, todoCount))
    while i < todoCountComplete:
        print("\t " + todoComplete[i]['title'])
        i += 1
