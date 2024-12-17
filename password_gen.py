# Creating a password generator
import string, random, time

possible_combos = string.ascii_letters + string.punctuation + string.digits

is_running = True

while is_running:

    user = input("Enter 'y' to generate password or 'n' to quit: ").lower()

    if user == "y":
        password = []
        for i in range(0, 12):
            generator = random.choice(possible_combos)
            password.append(generator)
        print("Your generated password is:", "".join(password))
    elif user == "n":
        print("Thank you for using our generator!")
        is_running = False
    else:
        print("Invalid input")





