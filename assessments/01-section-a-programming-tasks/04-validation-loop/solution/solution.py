while True:
    try:
        n = int(input("Enter a number between 10 and 20: "))
    except ValueError:
        print("Out of range, try again.")
        continue

    if 10 <= n <= 20:
        print(f"Thank you, you entered {n}")
        break
    else:
        print("Out of range, try again.")
