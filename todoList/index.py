tasks = []

def show_menu():
    print("1. Add a task")
    print("2. View all tasks")
    print("3. Delete a task")
    print("4. Exit")


def add_task():
    task = input("Enter the task: ")
    tasks.append(task)
    print("Task added successfully!")

def delete_task():
    if not tasks:
        print("No tasks to delete.")
        return
    view_tasks()
    task = input("Enter the task to delete: ")
    if task in tasks:
        tasks.remove(task)
        print(f"Task '{task}' deleted successfully!")
    else:
        print("Task not found.")

def view_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        print("Your tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

while True:
    show_menu()
    choice = input("Enter your choice: ")
    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        break
    else:
        print("Invalid choice")