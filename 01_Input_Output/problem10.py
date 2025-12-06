#Q9. Write a program to check if a number is even and divisible by 5.
num = int(input("Enter a number: "))

if num % 2 == 0 and num % 5 == 0:
    print("The number is even and divisible by 5")
else:
    print("The number does not satisfy the condition")
