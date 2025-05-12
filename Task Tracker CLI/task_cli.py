# task_cli.py
import sys
import json
import os
from datetime import datetime

TASK_FILE = 'tasks.json'

def load_tasks():
    if not os.path.exists(TASK_FILE):
        return []
    with open(TASK_FILE, 'r') as f:
        return json.load(f)

def save_tasks(tasks):
    with open(TASK_FILE, 'w') as f:
        json.dump(tasks, f, indent=2)

def get_new_id(tasks):
    return max([task['id'] for task in tasks], default=0) + 1

def add_task(description):
    tasks = load_tasks()
    new_task = {
        "id": get_new_id(tasks),
        "description": description,
        "status": "todo",
        "createdAt": datetime.now().isoformat(),
        "updatedAt": datetime.now().isoformat()
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print(f'Task added successfully (ID: {new_task["id"]})')

def list_tasks():
    tasks = load_tasks()
    for task in tasks:
        print(f"[{task['id']}] {task['description']} - {task['status']}")

# Entry point
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python task_cli.py <command> [arguments]")
        sys.exit(1)

    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) < 3:
            print("Error: Task description required.")
        else:
            add_task(" ".join(sys.argv[2:]))
    elif command == "list":
        list_tasks()
    else:
        print(f"Unknown command: {command}")