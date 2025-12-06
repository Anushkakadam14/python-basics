password = input("Enter your password: ")

if len(password) > 6 and "@" in password:
    print("Strong password")
else:
    print("Weak password")
