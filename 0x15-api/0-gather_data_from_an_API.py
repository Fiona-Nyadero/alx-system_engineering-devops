#!/usr/bin/python3
"""
Script uses REST API for employee ID
to return TODO list progress
"""

import requests
import sys


def fetch_employee_data(employee_id):
    """ Method fetches employee data from REST API """
    id_api_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"

    res = requests.get(id_api_url)

    if res.status_code == 200:
        employee_id_data = res.json()
        return employee_id_data
    else:
        print(f"Error: Unable to fetch data for employee ID {employee_id}")
        sys.exit(1)


def fetch_todo_list(employee_id):
    """ Method fetches employee todo list from REST API """
    todos_api_url = (
            f"https://jsonplaceholder.typicode.com/todos?userId="
            f"{employee_id}"
    )

    res = requests.get(todos_api_url)

    if res.status_code == 200:
        employee_todo_list = res.json()
        return employee_todo_list
    else:
        print(f"Error: Unable to fetch TODO list for \
                employee ID {employee_id}")
        sys.exit(1)


def display_todo_progress(employee_name, employee_todo_list):
    """ Method analyses the todo list progress """
    complete_tasks = sum(1 for task in employee_todo_list if task['completed'])

    all_tasks = len(employee_todo_list)

    print(f"Employee {employee_name} is done with tasks\
            ({complete_tasks}/{all_tasks}):")

    for task in employee_todo_list:
        if task['completed']:
            print(f"\t{task['title']}")


if __name__ == "__main__":
    """ Main function or project entry point """
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    employee_id_data = fetch_employee_data(employee_id)
    employee_todo_list = fetch_todo_list(employee_id)
    display_todo_progress(employee_id_data['name'], employee_todo_list)
