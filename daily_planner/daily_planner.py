def load_tasks():
    try:
        with open("tasks.txt", "r") as f:
            lines = f.readlines()
            return [line.strip() for line in lines]
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open("tasks.txt", "w") as f:
        for task in tasks:
            f.write(task + "\n")

def show_tasks(tasks):
    print("\nYour Tasks:")
    if not tasks:
        print("- No tasks yet!")
    for i, task in enumerate(tasks):
        print(f"{i + 1}. {task}")

def main():
    
    # Ensures the file exists before loading
    open("tasks.txt", "a").close()
    
    tasks = load_tasks()
    
    while True:
        print("\n--- Daily Planner ---")
        print("1. View tasks")
        print("2. Add a task")
        print("3. Mark task as done")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            show_tasks(tasks)

        elif choice == "2":
            task = input("Enter your task: ")
            tasks.append(task)
            save_tasks(tasks)
            print("Task added.")

        elif choice == "3":
            show_tasks(tasks)
            task_num = int(input("Enter task number to mark as done: "))
            if 1 <= task_num <= len(tasks):
                tasks[task_num - 1] += " DONE"
                save_tasks(tasks)
                print("Task marked as done.")
            else:
                print("Invalid task number.")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid input. Try again.")

if __name__ == "__main__":
    main()