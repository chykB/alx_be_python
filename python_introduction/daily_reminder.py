description = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time = input("Is it time-bound? (yes/no): ")

match priority:
    case "high":
        if time == "yes":
            print(f"Reminder: {description} is a high priority task that requires immediate attention today!")
        elif time == "no":
            print(f"Note: {description} is a high priority task. Consider completing it when you have free time")
    case "medium":
        if time == "yes":
            print(f"Note: {description} is a medium priority task. Consider looking into it before the time runs out")
        elif time == "no":
            print(f"Note: {description} is a medium priority task. Consider completing it when you have free time")
    case "low":
        if time == "yes":
            print(f"Reminder: {description} is a low priority task that requires immediate attention today!")
        elif time == "no":
            print(f"Note: 'Read a book' is a low priority task. Consider completing it when you have free time.")