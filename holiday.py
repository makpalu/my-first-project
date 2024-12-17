#Creating an acceptance program

#Taking input of user name
name= str(input("Enter your name: "))

#taking user input of scores
english= int(input("English: "))
maths= int(input("Maths: "))
science= int(input("Science: "))
social= int(input("Social: "))

#creating grading system for English

if english > 100:
    print("English: Invalid")
elif english >= 89:
    print("English: A")
elif english >= 79:
    print("English: B")
elif english >= 69:
    print("English: C")
elif english >= 59:
    print("English: D")
elif english >= 49:
    print("English: E")
else:
    print ("English: F")

#creating grading system for maths

if maths > 100:
    print("Maths: Invalid")
elif maths >= 89:
    print("Maths: A")
elif maths >= 79:
    print("Maths: B")
elif maths >= 69:
    print("Maths: C")
elif maths >= 59:
    print("Maths: D")
elif maths >= 49:
    print("Maths: E")
else:
    print ("Maths: F")

#creating grading system for science

if science > 100:
    print("Science: Invalid")
elif science >= 89:
    print("Science: A")
elif science >= 79:
    print("Science: B")
elif science >= 69:
    print("Science: C")
elif science >= 59:
    print("Science: D")
elif science >= 49:
    print("Science: E")
else:
    print ("Science: F")

#creating grading system for social

if social > 100:
    print("Social: Invalid")
elif social >= 89:
    print("Social: A")
elif social >= 79:
    print("Social: B")
elif social >= 69:
    print("Social: C")
elif social >= 59:
    print("Social: D")
elif social >= 49:
    print("Social: E")
else:
    print ("Social: F")

#Creating school selection

average = (english + maths + science + social) / 2

if average <= 200 and average >= 150 :
    print("You have been admitted")
elif average <150:
    print("Try again next year")
else:
    print("Invalid scores")

