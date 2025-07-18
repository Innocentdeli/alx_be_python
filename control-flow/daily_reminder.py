# Prompt the user for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

# Start generating the reminder based on priority
match priority:
    case "high":
        reminder = f"High priority task: '{task}'"
    case "medium":
        reminder = f"Medium priority task: '{task}'"
    case "low":
        reminder = f"Low priority task: '{task}'"
    case _:
        reminder = f"Task: '{task}' (Unknown priority)"

# Add urgency if the task is time-bound
if time_bound == "yes":
    reminder += " that requires immediate attention today!"

# Display the reminder
print("Reminder: ", reminder)
