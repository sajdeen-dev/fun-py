tasks = []

def show_menu():
    print("1. Add a task")
    print("2. View all tasks")
    print("3. Delte a task ")
    print("4. Exit")


def add_task():
        task = input("Enter the task: ")
        tasks.append(task)
        print("Task added successfully!")
def delete_task():
    print("Enter the task to delete: ")
    task = input("Enter the task to delete: ")
    tasks.remove(task)
def view_tasks():
    print("Your tasks: ")

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