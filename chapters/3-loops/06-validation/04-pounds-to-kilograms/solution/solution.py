max_pounds = int(input("Enter the maximum pounds (10-250): "))
while max_pounds < 10 or max_pounds > 250:
    print("Invalid! Please enter a value between 10 and 250.")
    max_pounds = int(input("Enter the maximum pounds (10-250): "))
for i in range(1, max_pounds + 1):
    print(i, "pound =", round(i / 2.2, 2), "kgs")
