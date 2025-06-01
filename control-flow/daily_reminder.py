# daily_reminder.py

task = input("What is the task description? ")
priority = input("What is the priority level? (high, medium, low): ").lower()
time_bound = input("Is the task time-sensitive? (yes/no): ").lower()

reminder_message = ""

match priority:
    case 'high':
        reminder_message = f"Reminder: '{task}' is a **high priority** task"
    case 'medium':
        reminder_message = f"Reminder: '{task}' is a **medium priority** task"
    case 'low':
        reminder_message = f"Reminder: '{task}' is a **low priority** task"
    case _:
        reminder_message = f"Reminder: '{task}' has an **unspecified priority**"

if time_bound == 'yes':
    reminder_message += " that requires immediate attention today!"
else:
    reminder_message += "."

print(reminder_message)