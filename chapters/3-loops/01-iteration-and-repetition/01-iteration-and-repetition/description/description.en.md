In programming, there are two related but distinct concepts when it comes to executing code multiple times: **repetition** and **iteration**.

**Repetition** means simply repeating the same lines of code. For example, if you wanted to print a message five times, you could write the same `print()` statement five times. This works, but it is inefficient and difficult to maintain.

**Iteration** means processing a series of items or data values one at a time to produce output. Rather than just blindly repeating, iteration works through a sequence — such as the characters in a string, the items in a list, or a range of numbers.

**Loops** are the programming construct that enables both repetition and iteration. They are fundamental in programming because they allow you to:

- Repeat a block of code a set number of times
- Process each item in a data sequence
- Continue running code until a condition is met

Here is an example of iteration through a string. The loop processes each character in the string one at a time:

```python
my_string = "Hello"
for letter in my_string:
    print("The current letter is: " + letter)
```

This produces:

```
The current letter is: H
The current letter is: e
The current letter is: l
The current letter is: l
The current letter is: o
```

Instead of writing five separate `print()` statements, the loop handles each character automatically. This is far more efficient and flexible — if the string changes, the loop adapts without any changes to the code.
