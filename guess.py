# Python guessing game

import random

guess = random.randint(1, 20)

for x in range(5):
    num = int(input("Guess a number between 1 and 20: "))
    if num == guess:
        print("You guessed right!")
        break
    elif num > guess:
        print("Your guess is too high")
    else:
        print("Your guess is too low")

