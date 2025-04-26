#Gavin Pierce To Do List
import os

# File to store the to-do list
TASK_FILE = "tasks.txt"


def read_tasks():
    """
    Reads the tasks from the file and returns a list of tasks.
    Each task is represented as a dictionary with task details.
    """
    tasks = []
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as file:
            for line in file:
                task_details = line.strip().split(" - ")
                if len(task_details) == 2:
                    task_name, status = task_details
                    tasks.append({"task": task_name, "status": status})
    return tasks


def write_tasks(tasks):
    """
    Writes the list of tasks to the file.
    Each task is written as 'task_name - status' format.
    """
    with open(TASK_FILE, "w") as file:
        for task in tasks:
            file.write(f"{task['task']} - {task['status']}\n")


def add_task():
    """
    Prompts the user for a task name and adds it to the to-do list with a 'pending' status.
    """
    task_name = input("Enter the task name: ")
    if task_name.strip() == "":
        print("Task name cannot be empty.")
        return
    tasks = read_tasks()
    tasks.append({"task": task_name, "status": "pending"})
    write_tasks(tasks)
    print(f"Task '{task_name}' added.")


def view_tasks():
    """
    Displays all tasks with their current status (pending or completed).
    """
    tasks = read_tasks()
    if tasks:
        print("\nTo-Do List:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task['task']} - {task['status']}")
    else:
        print("Your to-do list is empty.")


def mark_task_complete():
    """
    Allows the user to mark a task as completed.
    """
    view_tasks()
    try:
        task_number = int(input("Enter the task number to mark as complete: "))
        tasks = read_tasks()
        if 0 < task_number <= len(tasks):
            task = tasks[task_number - 1]
            if task["status"] == "completed":
                print("This task is already completed.")
            else:
                task["status"] = "completed"
                write_tasks(tasks)
                print(f"Task '{task['task']}' marked as complete.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def delete_task():
    """
    Allows the user to delete a task from the to-do list.
    """
    view_tasks()
    try:
        task_number = int(input("Enter the task number to delete: "))
        tasks = read_tasks()
        if 0 < task_number <= len(tasks):
            task = tasks.pop(task_number - 1)
            write_tasks(tasks)
            print(f"Task '{task['task']}' deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def display_menu():
    """
    Displays the menu for user interaction.
    """
    print("\nTo-Do List Menu:")
    print("1. View tasks")
    print("2. Add task")
    print("3. Mark task as complete")
    print("4. Delete task")
    print("5. Exit")
    choice = input("Choose an option: ")
    return choice


def list_main():
    """
    Main function that runs the program.
    """
    # Ensure the tasks file exists
    if not os.path.exists(TASK_FILE):
        with open(TASK_FILE, "w") as file:
            file.write("")  # Create the file if it doesn't exist

    while True:
        user_choice = display_menu()

        if user_choice == "1":
            view_tasks()
        elif user_choice == "2":
            add_task()
        elif user_choice == "3":
            mark_task_complete()
        elif user_choice == "4":
            delete_task()
        elif user_choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    list_main()
