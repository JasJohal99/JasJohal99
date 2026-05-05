```python
if age > 12 and height > 1.4:
    print("You can ride.")
else:
    print("You cannot ride.")
```

The key construct is the logical operator **`and`** — it combines the two checks so that **both** must be true for the user to ride. If either one fails, the whole condition is `False` and the `else` branch runs.

Note on the comparison operators: the question says "over 12 years old" and "taller than 1.4 m", which both suggest **strict** inequality (`>`). A solution using `>=` for either check is also defensible if the student justifies their interpretation — accept it provided the use of `and` is correct.
