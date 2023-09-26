import os

# Define the filename for storing the To-Do List
todo_file = "todo.txt"

def show_menu():
    print("To-Do List Menu:")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Mark Task as Done")
    print("4. Remove Task")
    print("5. Exit")
    choice = input("Enter your choice: ")
    return choice

def view_todo_list():
    if os.path.exists(todo_file):
        with open(todo_file, "r") as file:
            tasks = file.readlines()
        if tasks:
            print("To-Do List:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task.strip()}")
        else:
            print("Your To-Do List is empty.")
    else:
        print("No To-Do List found. Create a new one.")

def add_task():
    task = input("Enter the task: ")
    with open(todo_file, "a") as file:
        file.write(task + "\n")
    print("Task added to the To-Do List.")

def mark_task_done():
    view_todo_list()
    task_num = int(input("Enter the task number to mark as done: "))
    with open(todo_file, "r") as file:
        tasks = file.readlines()
    if 1 <= task_num <= len(tasks):
        tasks[task_num - 1] = "DONE: " + tasks[task_num - 1]
        with open(todo_file, "w") as file:
            file.writelines(tasks)
        print("Task marked as done.")
    else:
        print("Invalid task number.")

def remove_task():
    view_todo_list()
    task_num = int(input("Enter the task number to remove: "))
    with open(todo_file, "r") as file:
        tasks = file.readlines()
    if 1 <= task_num <= len(tasks):
        removed_task = tasks.pop(task_num - 1)
        with open(todo_file, "w") as file:
            file.writelines(tasks)
        print(f"Removed task: {removed_task.strip()}")
    else:
        print("Invalid task number.")

def main():
    while True:
        choice = show_menu()
        if choice == "1":
            view_todo_list()
        elif choice == "2":
            add_task()
        elif choice == "3":
            mark_task_done()
        elif choice == "4":
            remove_task()
        elif choice == "5":
            print("Exiting the To-Do List application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()