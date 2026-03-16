A **nested loop** is a loop inside another loop. The inner loop runs completely for each iteration of the outer loop.

Here is an example that generates times tables from 1 to 12:

```python
for count in range(1, 13):
    print("Times Table for:", count)
    for count2 in range(1, 13):
        print(count, "*", count2, "=", count * count2)
```

The outer loop runs 12 times (once for each times table), and for each iteration, the inner loop also runs 12 times, producing all the multiplication results.

## The `continue` Statement

The `continue` statement skips the rest of the current iteration and moves on to the next one. For example, this code prints a string but skips all occurrences of the letter `"j"`:

```python
for letter in "An example with multiple letters jjjjjjjj removed":
    if letter == "j":
        continue
    print(letter, end="")
```

Output: `An example with multiple letters  removed`

## One-Line Nested Loops (List Comprehension)

You can write nested loops in a single line using a **list comprehension**:

```python
first = "ABCD"
second = "1234"
final = [temp1 + temp2 for temp1 in first for temp2 in second]
print(final)
```

This produces a list of all combinations: `['A1', 'A2', 'A3', 'A4', 'B1', 'B2', 'B3', 'B4', 'C1', 'C2', 'C3', 'C4', 'D1', 'D2', 'D3', 'D4']`.
