# python quiz game

questions = (("1. What is the capital of USA?"),
             ("2. Which country was the first to gain independence in Africa?"),
             ("3. Who discovered gravity?"),
             ("4. Who is not a football player"),
             ("5. What is the tallest mountain in the world?"))

options = (("A. New York", "B. Washington D.C", "C. Illinois", "D. Michigan"),
           ("A. Ghana", "B. Nigeria", "C. South Africa", "D. Gambia"),
           ("A. Einstein", "B. Nietsche", "C. Newton", "D. Nepolio"),
           ("A. Messi", "B. Sane", "C. Xavi", "D. Kobe"),
           ("A. Afadza", "B. Kilimanjaro", "C. Everest", "D. Wli"))

answers = ("B", "A", "C", "D", "C")
guesses = []
score = 0
question_num = 0

for question in questions:
    for i in question:
        print(i, end="")
    print()
    for option in options[question_num]:
        print(option)
    print()

    guess = input("Enter (A,B,C,D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("Correct")
    else:
        print("Incorrect")
        print(f"The correct answer is {answers[question_num]}")


    question_num += 1

print(f"Your score is {score} out of 5")
if score >= 3:
    print("Well done!")
else:
    print("Better luck next time")