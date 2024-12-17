# Creating a To-do-list
import random, time

your_list = []
is_running = True

# Various modes that are implemented based on user's choice
def out():
    print("Thanks for using iOrganizer!")
    is_running = False

def randomiser():
    print("You are to:", "".join(random.choice(your_list)))

def normal():
    task_done = input("Enter the task you completed: ").lower()

    if task_done in your_list:
        your_list.remove(task_done)
        print(f"Congratulations on completing {task_done} 😊!")
    else:
        print("Task not found!")

def timer():
    task_timer = input("Select a task to time: ")

    if task_timer not in your_list and task_timer.isalpha():
        print("Task not found!")
    elif  task_timer in your_list and not task_timer.isdigit():
        countdown = int(input("Enter the time in seconds: "))
        for x in range(countdown, 0, -1):
            seconds = x % 60
            minutes = int(x / 60) % 60
            hours = int(x / 3600)
            print(f"{hours:02}:{minutes:02}:{seconds:02}")
            time.sleep(1)

        print("TIME UP!")

        user_done = input("Did you complete the task? (Y/N): ").upper()

        if user_done == "Y":
            your_list.remove(task_timer)
            print("Congratulations!🎉🎉🎉")
        elif user_done == "N":
            print("😞😞😞")
        else:
            print("Invalid input")

    else:
        print("Invalid input")


# computer asks user to select a mode and implements that mode
def options():
    print("---------------")
    print(" Select a mode ")
    print("---------------")
    print("1. Normal mode")
    print("2. Random mode")
    print("3. Timer mode")
    print("4. Exit")

    user_choice = int(input("Enter your choice: "))

    if user_choice == 1:
        normal()
    elif user_choice == 2:
        randomiser()
    elif user_choice == 3:
        timer()
    elif user_choice == 4:
        print("Thanks for using iOrganizer!")
        global is_running
        is_running = False
    else:
        print("Invalid input")

while is_running:
    print("-----------")
    print(" iOrganize ")
    print("-----------")

    #user enters his tasks
    to_do = input("Enter the tasks you want to do or 'done' to continue: ").lower()

    if to_do == "done":
        options()
    else:
        your_list.append(to_do)



