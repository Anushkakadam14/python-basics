#Q5. Check if a character is uppercase, lowercase, or not an alphabet
char = input("Enter a character: ")

if char.isupper():
    print("The character is uppercase")
elif char.islower():
    print("The character is lowercase")
elif char.isalpha():
    print("It is an alphabet but not upper/lower case")   # rare case
else:
    print("The character is not an alphabet")
