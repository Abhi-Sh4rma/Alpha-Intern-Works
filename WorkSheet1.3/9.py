
char = input("Enter a character: ")


if char.isdigit():
    print("Digit")
elif char.isalpha():
    print("Alphabet")
else:
    print("Special character")
