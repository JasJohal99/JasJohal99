> **Marks:** 12
{: .callout-info}

Write a program that:

- repeatedly asks the user for a number until they enter one between `10` and `20` (inclusive),
- prints `Out of range, try again.` (and re-prompts) whenever the entered number is outside that range,
- once a valid number is entered, prints `Thank you, you entered <n>` (with `<n>` replaced by the value) and stops,
- does **not** crash if the user types something that is not a whole number (re-prompt instead).

## Example interactions

```console
Enter a number between 10 and 20: 15
Thank you, you entered 15
```

```console
Enter a number between 10 and 20: 5
Out of range, try again.
Enter a number between 10 and 20: 25
Out of range, try again.
Enter a number between 10 and 20: 15
Thank you, you entered 15
```
