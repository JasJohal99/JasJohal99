A **for loop** is used to repeat a block of code a fixed number of times. It is sometimes called a **counter-controlled loop** because a counter variable keeps track of how many times the loop has run.

The basic syntax uses the `range()` function:

```python
for count in range(10):
    print(count)
```

This loop runs 10 times. The variable `count` starts at **0** and increases by 1 each time, up to but **not including** 10. The output is:

```
0
1
2
3
4
5
6
7
8
9
```

Key points about `range(n)`:

- It generates numbers starting from **0**
- It stops **before** reaching `n` (so `range(10)` produces 0 through 9)
- It produces exactly `n` values
- The counter variable (here called `count`) automatically takes on each value in turn

This type of loop is also called a **fixed** or **unconditional** loop because the number of repetitions is determined before the loop starts — it will always run exactly the number of times specified, regardless of what happens inside the loop body.

The indented code below the `for` line is called the **loop body**. Everything indented at the same level will be repeated each time the loop runs.
