**Validation** means checking that data entered by a user is correct or reasonable before using it in a program. Two common types of validation are **range checks** and **type checks**.

## Range Check

A **range check** ensures that a value falls within a specified range. For example, if you ask a user to enter a number between 10 and 20, you need to check that their input meets this requirement.

One approach uses a **flag variable** to track whether valid input has been received:

```python
valid = False
while not valid:
    number = int(input("Enter a number between 10 and 20: "))
    if number >= 10 and number <= 20:
        valid = True
    else:
        print("Invalid! Must be between 10 and 20.")
```

An alternative approach uses `while True` with `break`:

```python
while True:
    number = int(input("Enter a number between 10 and 20: "))
    if number >= 10 and number <= 20:
        break
    print("Invalid! Must be between 10 and 20.")
```

Both approaches keep asking for input until the user provides a valid value.

## Type Check

A **type check** ensures the user enters the correct type of data. For example, if you expect a number but the user types text, you need to catch that.

The `.isdigit()` method checks if a string contains only digits:

```python
value = input("Enter a number: ")
while not value.isdigit():
    print("That is not a valid number!")
    value = input("Enter a number: ")
```

Note that `.isdigit()` only works for positive whole numbers. To handle **negative numbers**, you can strip the leading minus sign before checking:

```python
value = input("Enter a number: ")
while not value.lstrip("-").isdigit():
    print("That is not a valid number!")
    value = input("Enter a number: ")
```

The `.lstrip("-")` method removes any leading `-` character, so `-5` becomes `5`, which `.isdigit()` can then validate.

## Checking for Text Input

The `.isalpha()` method checks if a string contains only letters (no numbers, spaces, or special characters):

```python
name = input("Enter your name: ")
while not name.isalpha():
    print("Invalid! Please enter letters only.")
    name = input("Enter your name: ")
```

This is useful when you want to ensure the user enters text-only input, such as a name.
