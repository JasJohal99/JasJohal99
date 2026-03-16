number = int(input("Enter a number between 10 and 30: "))
while number < 10 or number > 30:
    print("Invalid! Please enter a number between 10 and 30.")
    number = int(input("Enter a number between 10 and 30: "))
print("You entered", number)
