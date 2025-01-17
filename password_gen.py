# Creating a password generator
import string, random
from tkinter import *

class App:
    def __init__(self):
        self.windows = Tk()
        self.windows.title("Password Generator")
        self.windows.geometry("500x400")
        self.windows.config(bg="lightblue")

        #component creation
        self.label()
        self.entry()

    def label(self):
        label_title = Label(self.windows, text="Welcome to my password generator", font=("Courrier", 20), bg="beige", fg="black")
        label_title.pack()

    def entry(self):
        self.password_entry = Entry(self.windows, font=("courier", 25), bg="white", fg="black", width=30, relief="solid")
        self.password_entry.pack(pady=50)

    def function(self):

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


app = App()
app.windows.mainloop()




