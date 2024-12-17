# Python Banking Program

def show_balance(balance):
    print(f"Your balance is GHC{balance:.2f}")

def deposit():
    amount = float(input("Enter the amount you want to deposit: "))

    if amount < 0:
        print("That is not a valid amount.")
        return 0
    else:
        print("Successfully Deposited!")
        return amount

def withdraw(balance):
    amount = float(input("Enter the amount you want to withdraw: "))

    if amount > balance:
        print("Insufficient funds")
        return 0
    elif amount < 0:
        print("That is not a valid amount.")
        return 0
    else:
        print("Withdrawal was successful!")
        return amount

def main():
    balance = 0
    is_running = True

    while is_running:
        print("Banking Program")
        print("1.Show Balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            show_balance()
        elif choice == "2":
            balance += deposit()
        elif choice == "3":
            balance -= withdraw()
        elif choice == "4":
            print("Thank you for your time")
            is_running = False
        else:
            print("Invalid Input")

if __name__ == "__main__":
    main()
