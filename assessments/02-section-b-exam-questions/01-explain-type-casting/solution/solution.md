In Python, `input()` always returns a value of type `str` (a string), even when the user types digits. If you want to use the entered value as a number — for arithmetic, comparison, or anything that expects an `int` or a `float` — you have to **cast** it to the right type first, using `int(...)` or `float(...)`.

Without casting, things go wrong in two main ways:

- Arithmetic on strings does the wrong thing or fails. For example, `"3" + 4` raises a `TypeError` because Python won't add a string and an integer, and `"3" + "4"` produces `"34"` (string concatenation), not `7`.
- Comparisons with numbers either fail or give surprising results. In Python 3, `"5" > 3` raises a `TypeError`.

Example:

```python
age = int(input("Enter your age: "))   # cast the input to an integer
next_year = age + 1                    # works because age is now an int
print(f"Next year you will be {next_year}.")
```

Without the `int(...)` cast, `age + 1` would raise `TypeError: can only concatenate str (not "int") to str`.
