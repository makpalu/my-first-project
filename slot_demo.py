import time, random

mylist = ["😭", "😂","😑"]
mychecker = []
balance = 0

for i in range(len(mylist)):
    myval = random.randint(0,2)
    mychecker.append(myval)
if mychecker[0] == mychecker[1] and mychecker[1] == mychecker[2]:
    print(mylist[mychecker[0]],mylist[mychecker[1]], mylist[mychecker[2]])
    print("You have won.")
else:
    print(mylist[mychecker[0]], mylist[mychecker[1]], mylist[mychecker[2]])
    print("Sorry, you have lost.")
