A **while loop** is a conditional (or indefinite) loop. It repeats a block of code as long as a condition is `True`. The condition is checked **before** each iteration (this is called a **pre-condition** loop). If the condition is `False` from the start, the loop body never executes.

Here is the basic syntax:

```python
count = 0
while count < 10:
    print(count)
    count = count + 1
```

This loop prints the numbers 0 through 9. Each time the loop runs, it checks whether `count < 10`. When `count` reaches 10, the condition becomes `False` and the loop stops.

## Counter-controlled while loop

You can use a while loop with user input to control how many times it runs:

```python
no_of_times = int(input("Please enter the number to count to: "))
counter = 1
while counter <= no_of_times:
    print("Number " + str(counter))
    counter = counter + 1
```

This asks the user for a number and then counts up to that number.

## The else clause

Python's `while` loop supports an optional `else` clause. The `else` block executes when the condition becomes `False` (i.e., when the loop finishes normally):

```python
count = 0
while count < 5:
    print(count)
    count += 1
else:
    print("Loop finished!")
```

The `else` block will **not** execute if the loop is exited with a `break` statement.
