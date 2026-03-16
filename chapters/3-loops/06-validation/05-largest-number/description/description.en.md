Write a program that asks the user to enter 8 numbers (positive integers). Validate each input using `.lstrip("-").isdigit()` to ensure it is a valid number. After all 8 numbers are entered, display the largest number.

### Input/Output

- Prompt: `Enter number X: ` (where X is 1 to 8)
- Error message: `Invalid! Please enter a valid number.`
- Output: `The largest number is X`

### Example

```
Enter number 1: 5
Enter number 2: 12
Enter number 3: abc
Invalid! Please enter a valid number.
Enter number 3: 3
Enter number 4: 8
Enter number 5: 20
Enter number 6: 1
Enter number 7: 15
Enter number 8: 7
The largest number is 20
```
