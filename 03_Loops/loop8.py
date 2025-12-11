#Q4. Print the table of any number (e.g., 5)

num = int(input("Enter a number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)
