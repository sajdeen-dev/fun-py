tasks = []

def show_menu():
    print("1. Add a task")
    print("2. View all tasks")
    print("3. Delte a task ")
    print("4. Exit")


def add_task():
        pass

def delete_task():
            pass

def view_tasks():
                pass

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