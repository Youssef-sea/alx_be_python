# daily_reminder.py

# Prompt for a single task
task = input("Enter your task: ")

# Prompt for the task's priority
priority = input("Priority (high/medium/low): ").lower()

# Ask if the task is time-bound
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Initialize the reminder message
reminder_message = ""

# Process the task based on priority and time sensitivity using Match Case
match priority:
    case 'high':
        reminder_message = f"'{task}' is a high priority task"
    case 'medium':
        reminder_message = f"'{task}' is a medium priority task"
    case 'low':
        reminder_message = f"'{task}' is a low priority task."
    case _:
        reminder_message = f"'{task}' is a task" # Default case for invalid priority
        print("Invalid priority entered. Please use high, medium, or low.")

# Modify the reminder if the task is time-bound
if time_bound == 'yes':
    if priority in ['high', 'medium']: # Emphasize immediate attention for high/medium time-bound tasks
        reminder_message += " that requires immediate attention today!"
    else: # For low priority time-bound tasks, still mention it's time-sensitive
        reminder_message += " and it's time-sensitive, consider completing it soon."
elif time_bound == 'no' and priority == 'low':
    reminder_message += " Consider completing it when you have free time."
elif time_bound == 'no':
    reminder_message += "." # Add a period for non-time-bound tasks

# Provide a customized reminder
print(f"\nReminder: {reminder_message}")