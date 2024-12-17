# chatgpt solution

def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    print(f"The number of vowels is: {count}")
    return count


count_vowels("sister leveling")