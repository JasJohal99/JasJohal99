```python
age = int(input("Enter age: "))
if age > 18:
    print("Adult")
else:
    print("Child")
```

The three fixes:

1. **Cast the input to `int`** with `int(input(...))` so `age > 18` compares two numbers instead of a string with an integer.
2. **Add the `:`** at the end of `if age > 18` — every `if` header in Python ends with a colon.
3. **Indent the `print(...)` calls** so they belong to their `if` and `else` branches. Without the indentation, Python sees them as statements outside the `if/else` (and would raise an `IndentationError` after the missing colon is fixed).
