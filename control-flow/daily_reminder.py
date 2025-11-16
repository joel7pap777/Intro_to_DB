task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Match Case for priority reaction
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
    case "medium":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        reminder = f"'{task}' is a low priority task"
    case _:
        reminder = f"'{task}' is a task"

# If statement to modify reminder if task is time-bound
if time_bound == "yes":
    reminder = f"{reminder} that requires immediate attention today!"
else:
    reminder = f"Note: {reminder}. Consider completing it when you have free time."

print(reminder)
