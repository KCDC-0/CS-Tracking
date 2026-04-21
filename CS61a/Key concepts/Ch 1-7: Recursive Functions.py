#### Recursive Functions

## Key Ideas:
# - anatomy of recursion
# - types of recursive functions
# - iteration vs recursion


def sum_digits(n):
    """Return the sum of the digits of positive integer n."""
    if n < 10:
        return n
    else:
        all_but_last, last = n // 10, n % 10
        return sum_digits(all_but_last) + last
    
# A recursive function such as the one above is one that calls upon itself
# The execution environment creates a new local frame for every call
# Each call has its own distinct arguments and local scope

# A recursive function typically consists of two main parts:
# Base Case: A conditional statement that handles the simplest possible input without a recursive call, preventing infinite loops
# Recursive Step: One or more calls to the function itself with "simpler" arguments moving the state toward the base case


def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)

# Here is an example of linear recursion, where each self-call reduces the problem incrementally

def is_even(n):
    if n == 0:
        return True
    else:
        return is_odd(n-1)

def is_odd(n):
    if n == 0:
        return False
    else:
        return is_even(n-1)

# This is an example of mutual recursion, where two or more functions call each other in a circular dependency

def fib(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    else:
        return fib(n-2) + fib(n-1)

# This is an example of tree recursion, where a function calls itself multiple times within a single execution frame


# The computational process evolved by a recursive function can often be visualized using calls to print
# Tree recursion can be less efficient than iteration for certain problems 
# but offers a significantly simpler and more elegant implementation for complex problems

# Iterative functions use local variables to track state
# Recursive functions store state within the environment structure and return values.



