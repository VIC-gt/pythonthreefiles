# Import functions from task_manager.task_utils package
from task_manager.task_utils import add_task, mark_task_as_complete, view_pending_tasks, calculate_progress
from task_manager.validation import validate_task_title, validate_task_description, validate_due_date

# Define the main function
def main():
    while True:
        print("Task Management System")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. View Pending Tasks")
        print("4. View Progress")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            try:
                title = input("Enter task title: ")
                validate_task_title(title)
                
                description = input("Enter task description: ")
                validate_task_description(description)
                
                due_date = input("Enter due date (YYYY-MM-DD): ")
                validate_due_date(due_date)
                
                add_task(title, description, due_date)
            except ValueError as e:
                print(f"Error: {e}")
                
        elif choice == "2":
            try:
                index = int(input("Enter task index to mark as complete: "))
                mark_task_as_complete(index)
            except ValueError:
                print("Error: Please enter a valid number for the index.")
                
        elif choice == "3":
            view_pending_tasks()
            
        elif choice == "4":
            progress = calculate_progress()
            print(f"Task completion progress: {progress:.2f}%")
            
        elif choice == "5":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")
        
if __name__ == "__main__":
    main()
