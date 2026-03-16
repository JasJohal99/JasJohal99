n = int(input("Enter the number of terms: "))
while n < 2:
    print("Invalid! Please enter a number greater than or equal to 2.")
    n = int(input("Enter the number of terms: "))
a = 0
b = 1
for i in range(n):
    print(a)
    a, b = b, a + b
