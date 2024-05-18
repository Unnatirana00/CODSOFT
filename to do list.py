def add_task(tasks, task, priority):
    tasks[task] = priority

def remove_task(tasks, task):
    if task in tasks:
        del tasks[task]
    else:
        print("Task not found.")

def display_tasks(tasks):
    if tasks:
        print("Tasks:")
        for task, priority in tasks.items():
            print(f"- {task}: Priority {priority}")
    else:
        print("No tasks to display.")

def main():
    tasks = {}
    while True:
        print("\n1. Add Task")
        print("2. Remove Task")
        print("3. Display Tasks")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter task: ")
            priority = input("Enter priority: ")
            add_task(tasks, task, priority)
        elif choice == '2':
            task = input("Enter task to remove: ")
            remove_task(tasks, task)
        elif choice == '3':
            display_tasks(tasks)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
    

