surname = input("Enter your surname: ")
while not surname.isalpha():
    print("Invalid! Please enter letters only.")
    surname = input("Enter your surname: ")
first_name = input("Enter your first name: ")
while not first_name.isalpha():
    print("Invalid! Please enter letters only.")
    first_name = input("Enter your first name: ")
print("Hello", first_name, surname + ", how are you today?")
