import os
import json
from datetime import datetime

# Define the file to store tasks
task_file = 'tasks.json'

# Load tasks from file or create a new file
def load_tasks():
    if os.path.exists(task_file):
        with open(task_file, 'r') as file:
            tasks = json.load(file)
    else:
        tasks = []
    return tasks

# Save tasks to file
def save_tasks(tasks):
    with open(task_file, 'w') as file:
        json.dump(tasks, file, indent=4)

# Add a task
def add_task():
    task_description = input("Enter the task description: ")
    due_date = input("Enter the due date (YYYY-MM-DD) or press Enter to skip: ")
    task = {
        'description': task_description,
        'due_date': due_date if due_date else "No due date",
        'completed': False,
        'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task added: {task_description}")

# View all tasks
def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks available.")
        return

    print(f"\n{'ID':<5} {'Description':<30} {'Due Date':<15} {'Status':<10} {'Created At'}")
    print("-" * 80)

    for i, task in enumerate(tasks):
        status = 'Done' if task['completed'] else 'Pending'
        print(f"{i+1:<5} {task['description']:<30} {task['due_date']:<15} {status:<10} {task['created_at']}")

    print("-" * 80)

# Mark a task as complete
def complete_task():
    tasks = load_tasks()
    if not tasks:
        print("No tasks to complete.")
        return

    view_tasks()
    task_id = int(input("Enter the task ID to mark as complete: ")) - 1

    if 0 <= task_id < len(tasks):
        tasks[task_id]['completed'] = True
        save_tasks(tasks)
        print(f"Task '{tasks[task_id]['description']}' marked as complete.")
    else:
        print("Invalid task ID.")

# Delete a task
def delete_task():
    tasks = load_tasks()
    if not tasks:
        print("No tasks to delete.")
        return

    view_tasks()
    task_id = int(input("Enter the task ID to delete: ")) - 1

    if 0 <= task_id < len(tasks):
        removed_task = tasks.pop(task_id)
        save_tasks(tasks)
        print(f"Task '{removed_task['description']}' deleted.")
    else:
        print("Invalid task ID.")

# Main program loop
def main():
    while True:
        print("\nTask Manager")
        print("1. Add a Task")
        print("2. View All Tasks")
        print("3. Mark a Task as Complete")
        print("4. Delete a Task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            complete_task()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
