## Recursive Challenges

### Factorial

Write a recursive function that computes the factorial of a number `num` passed in as an argument. The factorial of a number is the product of that number multipled by every successive integer downward to 1. In mathematics, it is denoted by the `!` symbol (e.g. 5!). So 5! (spoken "five factorial") is equal to 5 * 4 * 3 * 2 * 1 or 120. 1! is equal to 1. Interestingly, 0! is also equal to 1 according to the official definition. You should also return 1 for any negative numbers entered, for the sake of simplicity.

```python
factorial(-1) # 1
factorial(0)  # 1
factorial(1)  # 1
factorial(2)  # 2
factorial(3)  # 6
factorial(4)  # 24
factorial(5)  # 120
```

### Fibonacci

Write a recursive function that accepts a positive number and returns the number at that place in the Fibonacci Sequence. Each term in the Fibonacci Sequence is the sum of the previous two terms. The sequence starts as follows:

```1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89...```

The sequence doesn't really make sense until you have at least two numbers to add so the definition of the Fibonacci Sequence states that the first two numbers are always 1 and 1 (or 0 and 1 by some definitions but we will use the "1, 1" starter definition).

With that in mind, for 0 or any negative argument just return 0. Since the first two positions are always defined to be 1 and 1 so you can set up your function to return 1 when the selected position is either 1 or 2. Any higher position will need to be calculated.

```python
fibonacci(-1) # 0
fibonacci(0) # 0
fibonacci(1) # 1
fibonacci(2) # 1
fibonacci(3) # 2
fibonacci(4) # 3
fibonacci(5) # 5
fibonacci(6) # 8
fibonacci(7) # 13
```

### Reverse String

Write a recursive function called `reverse` that accepts a string and returns
a reversed string.

```python
reverse("") # ""
reverse("a") # "a"
reverse("ab") # "ba"
reverse("computer") "retupmoc"
reverse("abcdefghijklmnopqrstuvwxyz") # "zyxwvutsrqponmlkjihgfedcba"
reverse(reverse("computer")) # "computer"
```

Is `reverse(reverse("computer"))` considered recursive? Why or why not?