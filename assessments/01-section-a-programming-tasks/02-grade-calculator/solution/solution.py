score = int(input("Enter score: "))

if score < 0 or score > 100:
    print("Invalid input")
elif score >= 70:
    print("A")
elif score >= 50:
    print("B")
elif score >= 40:
    print("C")
else:
    print("U")
