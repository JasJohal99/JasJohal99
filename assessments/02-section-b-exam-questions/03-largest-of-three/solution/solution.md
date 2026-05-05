**Pseudocode answer:**

```text
INPUT a
INPUT b
INPUT c
largest = a
IF b > largest THEN largest = b
IF c > largest THEN largest = c
OUTPUT largest
```

**Python answer (explicit comparisons):**

```python
a = int(input("First number: "))
b = int(input("Second number: "))
c = int(input("Third number: "))

largest = a
if b > largest:
    largest = b
if c > largest:
    largest = c

print("Largest:", largest)
```

A solution using the built-in `max(a, b, c)` is also acceptable for full marks, since it produces the correct result.
