### Exercises:

**Basic Function:**


Create a function that takes two parameters, performs arithmetic operation, and returns the result.


**String Manipulation:**


Write a function that takes a string as input and returns the same string reversed.


**List Processing:**

Create a function that accepts a list of numbers and returns the sum of all even numbers in the list.


**Conditional Logic:**


Write a function that takes an integer as input and returns "Even" if it's even and "Odd" if it's odd.


**Default Parameters:**


Design a function that takes two parameters, where the second parameter is optional and has a default value. The function should perform a specific operation on the parameters.


**Integrating Collatz and Linear Function:**



Create a function that utilizes both collatz and linear functions.


**Follow the sample code below:**
```
def integrated(num):
    """
    Algorithm:
        1. Call the collatz function. The collatz function must have a return statement (i.e, list).
        2. Iterate over the returned value from calling the collatz function;
        3. For each iteration, you must apply the linear function with the given values for m and b;
            m = 0.5
            b = 1
        4. Return all results from calling the linear function in a list.

    Example Output:
        linear_sequence = integrated(20)
        >>> [6.0, 3.5, 9.0, 5.0, 3.0, 2.0, 1.5]
    """
    pass
```
