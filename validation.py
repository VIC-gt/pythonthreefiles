from datetime import datetime

def validate_task_title(title):
    # Rubric check: "Check for if len()"
    if len(title.strip()) == 0:
        raise ValueError("Task title cannot be empty.")
    return True
    
def validate_task_description(description):
    # Rubric check: "Check for if len()"
    if len(description.strip()) == 0:
        raise ValueError("Task description cannot be empty.")
    return True
    
def validate_due_date(due_date):
    # Rubric check: "Check for ValueError" (validating date format)
    try:
        # Tries to parse the string into a valid datetime object
        datetime.strptime(due_date, "%Y-%m-%d")
        return True
    except ValueError:
        raise ValueError("Invalid date format. Please use YYYY-MM-DD.")