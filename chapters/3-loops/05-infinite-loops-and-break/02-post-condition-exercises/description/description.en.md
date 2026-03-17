Now that you know about `while True` and `break`, try rewriting the previous exercises using the **post-condition** pattern. Since we cannot verify the loop structure through output testing, these are presented as examples with solutions you can reveal.

## Exercise 3.12: Hello Four Times

Rewrite the "Hello Four Times" program using `while True` and `break` instead of a regular `while` loop.

<details markdown="1">
<summary>Show solution</summary>

```python
count = 0
while True:
    print("hello")
    count = count + 1
    if count == 4:
        break
```

</details>

## Exercise 3.13: Repeat Message

Rewrite the "Repeat Message" program using `while True` and `break`.

<details markdown="1">
<summary>Show solution</summary>

```python
message = input("Enter a message: ")
times = int(input("Enter the number of times to display: "))
count = 0
while True:
    print(message)
    count = count + 1
    if count == times:
        break
```

</details>

## Exercise 3.14: Sum Until Zero

Rewrite the "Sum Until Zero" program using `while True` and `break`.

<details markdown="1">
<summary>Show solution</summary>

```python
total = 0
while True:
    number = int(input("Enter a number: "))
    if number == 0:
        break
    total = total + number
print("The total is", total)
```

</details>
