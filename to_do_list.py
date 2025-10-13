tasks = []

#Function to load options
def display_menu():
    print("\nTo-Do List Application")
    print("1. Add a new task")
    print("2. View all tasks")
    print("3. Mark a task as completed")
    print("4. Delete a task")
    print("5. Exit")

#Function to store tasks
def add_task():
    task_description = input('Input task description: ')
    while task_description == "":
        print('Task description cannot be empty.')
        task_description = input("Input task description: ")

    task = {'Task_Name': task_description, 'Completed': False}
    tasks.append(task)
    print(f'You have added {task_description} successfully. \n')

#Function to view tasks
def view_task():
    if not tasks:
        print("No tasks added. Add tasks to view them.")
    else:
        for i, task in enumerate(tasks, start=1):
            status = "✅" if task["Completed"] else "❌"
            print(f"{i}. Task: {task['Task_Name']}, Completed: {status}")

#Function to mark task as complete
def mark_task():
    view_task()
    while True:
        task_num = input("Type the task number of the task to mark as completed: ")
        try:
            num = int(task_num)
            break
        except ValueError:
            print("Task has to be a number")
    while num > len(tasks):
        print("Task not found. Enter a valid task number.")
        num = int(input("Enter Task Number: "))
    task = tasks[num - 1]
    task['Completed'] = True
    print(f"Task: {task['Task_Name']} has been marked as completed.\n")

#Function to delete task
def delete_task():
    view_task()
    while True:
        task_num = input("Type the task number of the task to delete: ")
        try:
            num = int(task_num)
            break
        except ValueError:
            print("Task has to be a number")
    while num > len(tasks):
        print("Task not found. Enter a valid task number.")
        num = int(input("Enter Task Number: "))
    tasks.pop(num-1)
    print('Task deleted successufully.\n')

