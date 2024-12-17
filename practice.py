# Count vowels

def vowels():
    total = 0
    alphabets = "aeiouAEIOU"
    user = input("Enter a word: ")
    for char in user:
        if char in alphabets:
            total += 1
            print(f"The total number of vowels: {total}")
    return total


vowels()
