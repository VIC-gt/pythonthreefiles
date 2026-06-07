from datetime import datetime

# Import validation functions
from validation import validate_task_title, validate_task_description, validate_due_date

# Define tasks list
tasks = []

# Implement add_task function
def add_task(title, description, due_date):
    # Format the structure to store tasks as a dictionary
    new_task = {
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False
    }
    tasks.append(new_task)
    print("Task added successfully!")
    
# Implement mark_task_as_complete function
def mark_task_as_complete(index, tasks=tasks):
    # Check if the index provided exists in the list
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        print("Task marked as complete!")
    else:
        print("Error: Invalid task index.")
    
# Implement view_pending_tasks function
def view_pending_tasks(tasks=tasks):
    # Filter tasks to find ones where 'completed' is False
    pending_tasks = [task for task in tasks if not task["completed"]]
    
    if len(pending_tasks) == 0:
        print("No pending tasks found.")
    else:
        print("--- Pending Tasks ---")
        # Loop through and display the pending tasks
        for idx, task in enumerate(tasks):
            if not task["completed"]:
                print(f"[{idx}] {task['title']} - Due: {task['due_date']}")

# Implement calculate_progress function
def calculate_progress(tasks=tasks):
    # Avoid division by zero if there are no tasks
    if len(tasks) == 0:
        return 0.0
    
    # Count how many tasks are marked as completed
    completed_count = sum(1 for task in tasks if task["completed"])
    
    # Calculate the percentage
    progress_percentage = (completed_count / len(tasks)) * 100
    return progress_percentage