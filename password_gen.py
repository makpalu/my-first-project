# Creating a password generator
import string
from random import choice
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
        self.button()

    def label(self):
        label_title = Label(self.windows, text="Welcome to my password generator", font=("Courrier", 20), bg="beige", fg="black")
        label_title.pack()

    def entry(self):
        self.password_entry = Entry(self.windows, font=("courier", 25), bg="white", fg="black", width=30, relief="solid")
        self.password_entry.pack(pady=50)

    def button(self):
        password_generator = Button(self.windows, text="Generate password", font=("Courier", 12), bg="white", fg="black", width=25, command=self.function)
        password_generator.pack()

    def function(self):

        possible_combos = string.ascii_letters + string.punctuation + string.digits
        password=[]

        for i in range(12):
            password+=choice(possible_combos)

        self.password_entry.delete(0, END)
        self.password_entry.insert(0, password)

app = App()
app.windows.mainloop()




