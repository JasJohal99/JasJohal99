smallest = None
for i in range(1, 9):
    value = input("Enter number " + str(i) + ": ")
    while not value.lstrip("-").isdigit():
        print("Invalid! Please enter a valid number.")
        value = input("Enter number " + str(i) + ": ")
    value = int(value)
    if smallest is None or value < smallest:
        smallest = value
print("The smallest number is", smallest)
