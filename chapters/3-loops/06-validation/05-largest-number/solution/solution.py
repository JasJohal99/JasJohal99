largest = 0
for i in range(1, 9):
    value = input("Enter number " + str(i) + ": ")
    while not value.lstrip("-").isdigit():
        print("Invalid! Please enter a valid number.")
        value = input("Enter number " + str(i) + ": ")
    value = int(value)
    if value > largest:
        largest = value
print("The largest number is", largest)
