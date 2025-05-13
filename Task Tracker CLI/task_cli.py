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
    if not tasks:
        print("No tasks found.")
        return
    for task in tasks:
        print(f"[{task['id']}] {task['description']} - {task['status']}")

def delete_task(task_id):
    tasks = load_tasks()
    updated_tasks = [task for task in tasks if task['id'] != task_id]
    if len(tasks) == len(updated_tasks):
        print(f"No task found with ID {task_id}")
        return
    save_tasks(updated_tasks)
    print(f"Task with ID {task_id} deleted.")

def update_task(task_id, description=None, status=None):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            if description:
                task['description'] = description
            if status:
                task['status'] = status
            task['updatedAt'] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task {task_id} updated.")
            return
    print(f"No task found with ID {task_id}")

def mark_done(task_id):
    update_task(task_id, status="done")

def reset_tasks():
    confirm = input("Are you sure you want to delete ALL tasks? (yes/no): ")
    if confirm.lower() == "yes":
        save_tasks([])
        print("All tasks have been deleted.")
    else:
        print("Reset cancelled.")

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

    elif command == "delete":
        if len(sys.argv) < 3:
            print("Error: Task ID required.")
        else:
            try:
                task_id = int(sys.argv[2])
                delete_task(task_id)
            except ValueError:
                print("Error: Task ID must be an integer.")

    elif command == "update":
        if len(sys.argv) < 3:
            print("Error: Task ID required.")
        else:
            try:
                task_id = int(sys.argv[2])
                description = None
                status = None
                if "--desc" in sys.argv:
                    description = sys.argv[sys.argv.index("--desc") + 1]
                if "--status" in sys.argv:
                    status = sys.argv[sys.argv.index("--status") + 1]
                update_task(task_id, description, status)
            except ValueError:
                print("Error: Task ID must be an integer.")

    elif command == "done":
        if len(sys.argv) < 3:
            print("Error: Task ID required.")
        else:
            try:
                task_id = int(sys.argv[2])
                mark_done(task_id)
            except ValueError:
                print("Error: Task ID must be an integer.")

    elif command == "reset":
        reset_tasks()

    else:
        print(f"Unknown command: {command}")
