An **infinite loop** is a loop that runs forever because its condition is always `True`. In Python, this is written as:

```python
while True:
    print("This runs forever!")
```

This loop will never stop on its own. To exit a loop early, Python provides the `break` statement.

## The break statement

The `break` statement immediately exits the loop it is inside. This is useful for creating **post-condition loops** — loops where the condition is checked at the **end** rather than the beginning.

```python
while True:
    value = int(input("Please enter a number between 1 and 10: "))
    if value >= 1 and value <= 10:
        break
```

This pattern simulates the **REPEAT...UNTIL** construct found in other programming languages. The loop body always executes at least once, and the condition to exit is checked at the end of each iteration.

## When to use break

The `break` statement can exit any loop (both `while` and `for` loops), but it should be used sensibly to keep your code readable. A common and accepted use is the post-condition pattern shown above, where you need the loop body to run at least once before checking whether to stop.
