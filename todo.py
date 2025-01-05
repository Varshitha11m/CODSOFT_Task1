# Simple To-Do List App


todo_list = []

def show_menu():
    print("\n=== To-Do List Menu ===")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

def view_tasks():
    if not todo_list:
        print("\nNo tasks in the list!")
    else:
        print("\nYour To-Do List:")
        for idx, task in enumerate(todo_list, start=1):
            print(f"{idx}. {task}")

def add_task():
    task = input("\nEnter the task: ")
    todo_list.append(task)
    print(f'"{task}" has been added!')

def remove_task():
    view_tasks()
    if todo_list:
        try:
            task_num = int(input("\nEnter the task number to remove: "))
            removed_task = todo_list.pop(task_num - 1)
            print(f'"{removed_task}" has been removed!')
        except (ValueError, IndexError):
            print("Invalid task number!")

while True:
    show_menu()
    choice = input("\nEnter your choice (1-4): ")
    
    if choice == "1":
        view_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        print("Exiting To-Do List. Goodbye!")
        break
    else:
        print("Invalid choice. Please select 1-4.")
