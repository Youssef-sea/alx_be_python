# daily_reminder.py

# Prompt for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Initialize the reminder message
reminder_message = ""

# Process the task based on priority using a Match Case statement
match priority:
    case 'high':
        reminder_message = f"Reminder: '{task}' is a **high priority** task"
    case 'medium':
        reminder_message = f"Note: '{task}' is a **medium priority** task"
    case 'low':
        reminder_message = f"Note: '{task}' is a **low priority** task"
    case _: # Handles any other input for priority
        reminder_message = f"Note: '{task}' has an **unspecified priority**"

# Modify the reminder based on time sensitivity
if time_bound == 'yes':
    reminder_message += " that requires immediate attention today!"
else:
    # Adding specific advice for non-time-bound tasks, especially low priority ones
    if priority == 'low':
        reminder_message += ". Consider completing it when you have free time."
    else:
        reminder_message += "."

# Print the customized reminder
print(reminder_message)