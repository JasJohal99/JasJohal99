The `range()` function can take up to three arguments: `range(start, stop, step)`. This gives you much more control over the sequence of numbers generated.

**Two arguments — `range(start, stop)`:**

```python
for i in range(2, 10):
    print(i)
```

This prints the numbers 2 through 9. The range starts at `start` and stops **before** `stop`.

**Three arguments — `range(start, stop, step)`:**

```python
for i in range(0, 10, 2):
    print(i)
```

This prints even numbers: 0, 2, 4, 6, 8. The `step` value determines how much the counter increases each time.

You can also count **backwards** by using a negative step:

```python
for i in range(10, 0, -1):
    print(i)
```

This counts down from 10 to 1.

## Iterating through a string

A for loop can also iterate directly through the characters of a string:

```python
my_string = "Hello"
for letter in my_string:
    print("The current letter is: " + letter)
```

Output:

```
The current letter is: H
The current letter is: e
The current letter is: l
The current letter is: l
The current letter is: o
```

## Using user input with range

You can combine `input()` with `range()` to let the user control how many times a loop runs:

```python
no_of_times = int(input("Please enter number of times: "))
for count in range(no_of_times):
    print("Count", count + 1)
```

If the user enters `3`, the output is:

```
Count 1
Count 2
Count 3
```

Notice that `count + 1` is used in the print statement so the displayed count starts at 1 rather than 0.
