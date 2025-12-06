#Q15. Check traffic light signal. User enters: "red", "yellow", "green" Output: red → STOP yellow → WAIT green → GO
signal = input("Enter the traffic signal (red / yellow / green): ").lower()

if signal == "red":
    print("STOP")
elif signal == "yellow":
    print("WAIT")
elif signal == "green":
    print("GO")
else:
    print("Invalid signal")
