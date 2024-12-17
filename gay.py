# Use of match case

def day_of_week(day):
    match day:
        case "Sunday":
            return "It is a weekend"
        case "Monday":
            return "It is a weekday"
        case "Tuesday":
            return "It is a weekday"
        case "Wednesday":
            return "It is a weekday"
        case "Thursday":
            return "It is a weekday"
        case "Friday":
            return "It is a weekday"
        case "Saturday":
            return "It is a weekend"
        case _:
            return "Invalid input"


print(day_of_week("Saturday"))