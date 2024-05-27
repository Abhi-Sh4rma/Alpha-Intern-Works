
char = input("Enter a character: ").lower()  


if char.isalpha() and char in 'aeiou':
    print("Vowel")
elif char.isalpha():
    print("Consonant")
else:
    print("Please enter a valid letter.")
