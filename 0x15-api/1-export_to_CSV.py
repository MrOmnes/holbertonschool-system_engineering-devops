#!/usr/bin/python3
"""This is a comment"""

import csv
import requests
import sys

if __name__ == "__main__":
    ID = sys.argv[1]
    filename = ID + ".csv"
    f = open(filename, 'w')
    writer = csv.writer(f, quoting=csv.QUOTE_ALL)
    link = "https://jsonplaceholder.typicode.com/"
    name = requests.get("{}users/{}".format(link, ID)).json()['username']
    todo_url = requests.get("{}users/{}/todos".format(link, ID)).json()
    i = 0
    while i < len(todo_url):
        header = [ID, name, todo_url[i]['completed'], todo_url[i]['title']]
        writer.writerow(header)
        i += 1
