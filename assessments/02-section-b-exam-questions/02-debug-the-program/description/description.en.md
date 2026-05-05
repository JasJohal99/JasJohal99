> **Marks:** 6
{: .callout-info}

The following program is supposed to ask for the user's age and then print `Adult` if they are over `18`, and `Child` otherwise. As written it does not work — it contains **three** errors:

```python
age = input("Enter age: ")
if age > 18
print("Adult")
else:
print("Child")
```

The errors are:

1. The value returned by `input()` is a **string**, but the program compares it to the **integer** `18` — that comparison won't work.
2. The line `if age > 18` is missing something Python requires at the end of every `if` header.
3. The two `print(...)` lines aren't in the right place — they need to belong to their `if` and `else` branches.

The broken code has been pre-loaded into the answer box below — edit it in place so the program runs correctly, then submit your fix.
