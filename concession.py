# concession stand program

menu = {"pizza": 3.00,
        "burger": 2.50,
        "popcorn": 4.00,
        "fries": 6.00,
        "soda": 3.00,
        "lemonade": 2.00,
        "chips": 1.00,
        "pretzel": 3.50}

cart = []
total_sum = 0

print("-------------Menu-------------")
for key, value in menu.items():
    print(f"{key:10}: ${value: .2f}")

print("------------------------------")

while True:
    food = input("Select an item (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("------- YOUR ORDER ------")
for food in cart:
    total_sum += menu.get(food)
    print(food, end=" ")

print()
print(f"Total is: ${total_sum: .2f}")