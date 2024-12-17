# slot machine

import time, random

is_running = True

balance = 0
deposit = 0

# defining functions

def show_balance(balance):

    if balance < 0:
        return 0
    else:
        print(f"Your balance is GHC{balance:.2f}")
        return balance

def deposit():
    amount = float(input("Enter the amount you want to deposit: "))

    if amount < 0:
        print("That is not a valid amount.")
        return 0
    else:
        print("Successfully Deposited!")
        return amount

while is_running:
    mylist = ["😭", "😂", "😑"]
    mychecker = []

    #user interface

    print("-------------------")
    print("     LUCKY SLOT    ")
    print("-------------------")
    print("1.Deposit")
    print("2.Balance")
    print("3.Bet")
    print("4.Exit")

    #choosing of options

    user = input("Enter an option (1-4): ")

    #operations based on choice

    if user == "1":
       balance += deposit()
    elif user == "2":
        show_balance(balance)
    elif user == "3":
        bet = float(input("Enter the amount you want to bet: "))

        if bet == 0:
            print("You can't bet 0 amount")
        elif balance == 0:
            print("You have no money!")
        elif bet > balance and balance != 0:
            print("Insufficient funds!")
            continue
        else:
            for i in range(len(mylist)):
                myval = random.randint(0, 2)
                mychecker.append(myval)
            if mychecker[0] == mychecker[1] and mychecker[1] == mychecker[2]:
                print(mylist[mychecker[0]], mylist[mychecker[1]], mylist[mychecker[2]])
                print("You have won.")
                balance += 100 * bet
                print(f"You now have GHC{balance:.2f} in your account.")
            else:
                balance -= bet
                print(mylist[mychecker[0]], mylist[mychecker[1]], mylist[mychecker[2]])
                print("Sorry, you have lost.")
    elif user == "4":
        print("Thanks for playing!")
        is_running = False
    else:
        print("Invalid input")



