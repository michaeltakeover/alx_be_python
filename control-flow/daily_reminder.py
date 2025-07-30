#Daily Reminder

task = input("Enter your task: ")
time_bound = input("Is it time-bound? (yes/no): ").lower()
priority = input("Priority (high/medium/low): ").lower()

match priority:
    case "high":
        reminder = f"Note: {task} is a high priority task."
    case "medium":
        reminder = f"'{task}' is a medium priority task."
    case "low":
        reminder = f"'{task}' is a low priority task."
    case __:
        reminder = f"'{task}' invalid informations.)"

if time-bound == "yes":
    reminder += " that requires immediate attention today!"
elif time-bound == "no":
    reminder += " Consider completing it when you have free time."
else:
    reminder += " But you entered an invalid time bound."

print("Reminder:", reminder)