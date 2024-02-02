#!/usr/bin/python3
"""Consumimos API para extraer información ficticia"""
import json
import requests
from sys import argv


def main():
    """Consultamos el nombre y las tareas de un empleado."""
    if len(argv) >= 2 and argv[1].isdigit():
        id = argv[1]

        url_id = f"https://jsonplaceholder.typicode.com/users/{id}"
        url_todos = f"https://jsonplaceholder.typicode.com/users/{id}/todos"

        response = requests.get(url_id)

        if response.status_code != 200:
            print(f"Ups... tuvimos un problema par consultar el {id}")
            exit()

        data = response.json()
        EMPLOYEE_NAME = data['username']

        response = requests.get(url_todos)

        if response.status_code != 200:
            print(f"Ups... tuvimos un problema par consultar el {id}")
            exit()

        todos = response.json()
        list_todos = []
        dict_todos = {}

        all_tasks = [todo['title'] for todo in todos]
        status_task = [todo['completed'] for todo in todos]

        for index in range(0, len(all_tasks)):
            dict_todos = {
                'task': all_tasks[index],
                'completed': status_task[index],
                'username': EMPLOYEE_NAME}

            list_todos.append(dict_todos)

            employee_todos = {str(id): list_todos}

        name_file_json = f'{id}.json'

        with open(name_file_json, mode='w', newline='') as f:
            json.dump(employee_todos, f, indent=4)
    else:
        print("Se esperaba que ingresará un ID valido")


if __name__ == '__main__':
    main()
