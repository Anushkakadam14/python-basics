#Check if a person gets a discount based on age < 12 → "50% discount"

'''age < 12 → "50% discount"
age between 12–18 → "20% discount"
age > 60 → "30% discount"
otherwise → "No discount" '''

age=int(input("Enter person age:"))
if age < 12:
    print("50% Disscount")
elif age >= 12 and age <= 18:
    print("20% Disscount")
elif age < 60:
    print("30 % Disscount")
else:
    print("No disscount")
