#Q8. Check whether a given letter is a vowel or consonant.
a = input("Enter the letter: ")
vowels = ["a", "e", "i", "o", "u"]

if a.lower() in vowels:
    print("Given letter is vowel")
else:
    print("Given letter is consonant")

