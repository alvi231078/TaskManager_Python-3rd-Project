from datetime import datetime

tasks = []

class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.creation_time = datetime.now()

def addTask():
    title = input("Enter the task title: ")
    description = input("Enter the task description: ")
    task = Task(title, description)
    tasks.append(task)
    print("Task added successfully.")

def removeTask():
    if len(tasks) == 0:
        print("No tasks to remove.")
        return

    print("Current Tasks:")
    seeTask()
    task_index = int(input("Enter the index of the task to remove: ")) - 1
    if 0 <= task_index < len(tasks):
        removed_task = tasks.pop(task_index)
        print(f"Task '{removed_task.title}' removed successfully.")
    else:
        print("Invalid task index.")

def seeTask():
    if len(tasks) == 0:
        print("No tasks to display.")
        return

    print("Tasks:")
    for index, task in enumerate(tasks):
        print(f"{index + 1}. {task.title} - {task.description} (Created: {task.creation_time})")

def main():
    while True:
        print("\nTask Manager Menu:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. See Tasks")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            addTask()
        elif choice == "2":
            removeTask()
        elif choice == "3":
            seeTask()
        elif choice == "4":
            print("Exiting Task Manager...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
