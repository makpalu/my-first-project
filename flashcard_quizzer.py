import random, time

your_list = []
is_running = True

# Various modes that are implemented based on user's choice
def complete():
    completed_to_do = []
    completed_to_do.append(task_done)

    if user_done == "Y":
        completed_to_do.append(task_timer)

    print("-----------------")
    print(" Completed Tasks ")
    print("-----------------")

    for word in completed_to_do:
        print(word)


def out():
    print("Thanks for using iOrganizer!")
    is_running = False

def randomiser():
    print("You are to:", "".join(random.choice(your_list)))

def normal():
    global task_done
    task_done = input("Enter the task you completed: ").lower()

    if task_done in your_list:
        your_list.remove(task_done)
        print(f"Congratulations on completing {task_done} 😊!")
    else:
        print("Task not found!")

def timer():
    global task_timer
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

        global user_done
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
    print("4. Completed tasks")
    print("5. Exit")

    user_choice = int(input("Enter your choice: "))

    if user_choice == 1:
        normal()
    elif user_choice == 2:
        randomiser()
    elif user_choice == 3:
        timer()
    elif user_choice == 4:
        complete()
    elif user_choice == 5:
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