#### Higher-Order Functions

## Key Ideas:
# - abstraction
# - Nested Definitions and Closures
# - Currying
# - Lambda Expressions
# - First class status of functions
# - Function Decorators



def summation(n, term):
    total, k = 0, 1
    while k <= n:
        total, k = total + term(k), k + 1
    return total

def cube(x):
    return x*x*x

def sum_cubes(n):
    return summation(n, cube)

result = sum_cubes(3)

# In this example, we generalise a process 
# by separating the control logic from the specific update or comparison rules
# summation here can be used to add the products of any function applied to a series of numbers

def improve(update, close, guess=1):
    while not close(guess):
        guess = update(guess)
    return guess

def golden_update(guess):
    return 1/guess + 1

def square_close_to_successor(guess):
    return approx_eq(guess * guess,
                     guess + 1)

def approx_eq(x, y, tolerance=1e-3):
    return abs(x - y) < tolerance

phi = improve(golden_update,
              square_close_to_successor)

from math import sqrt
phi = 1/2 + sqrt(5)/2
def improve_test():
        approx_phi = improve(golden_update, square_close_to_successor)
        assert approx_eq(phi, approx_phi), 'phi differs from its approximation'

improve_test()

# above is another example of extraction using a phi approximation example


def square(x):
    return x * x

def successor(x):
    return x + 1

def compose1(f, g):
    def h(x):
        return f(g(x))
    return h

def f(x):
    """Never called."""
    return -x

square_successor = compose1(square, successor)
result = square_successor(12)

# Defining functions inside other functions solves 
# "namespace clutter" and allows for Lexical Scoping
# This means that Inner functions have access to the environment 
# in which they were defined, not where they are called
# This means that:
# - The names of a local function do not interfere with names external to the function in which it is defined
# - A local function can access the environment of the enclosing function

# In the example above, Functions can return other functions while f and g are resolved correctly



def curry2(f):
    """Return a curried version of the given two-argument function."""
    def g(x):
        def h(y):
            return f(x, y)
        return h
    return g

def uncurry2(g):
    """Return a two-argument version of the given curried function."""
    def f(x, y):
        return g(x)(y)
    return f

def map_to_range(start, end, f):
    while start < end:
        print(f(start))
        start = start + 1

pow_curried = curry2(pow)
pow_curried(2)(5) == uncurry2(pow_curried)(2, 5)

map_to_range(0, 10, pow_curried(2))

# We make use of nested functions here to allow for Currying: 
# The process of converting a function that takes multiple arguments 
# into a chain of functions that each take a single argument (f(x,y)→g(x)(y))
# This is useful for adapting functions to interfaces that expect single-argument inputs.



# Lambda expressions allow for the creation of anonymous functions on the fly in the following syntax:
# lambda <parameters>: <return_expression>
#      lambda            x            :          f(g(x))
# "A function that    takes x    and returns     f(g(x))"
# This is best used for immmediate arguments while def notation is better for readability

def compose1(f, g):
    return lambda x: f(g(x))

compose1 = lambda f,g: lambda x: f(g(x))

f = compose1(lambda x: x * x,
             lambda y: y + 1)

# Here are some ways lambda can be used for the composite function creator


# In Python, functions are first-class elements, meaning they possess the following "rights":
# - They may be bound to names.
# - They may be passed as arguments to functions.
# - They may be returned as the results of functions.
# - They may be included in data structures.


# Decorators provide a shorthand syntax (@) for applying higher-order functions to a definition
# These 2 syntaxes are equal:


# @trace
# def triple(x):
#     return 3 * x

# def triple(x):
#    return 3 * x
# triple = trace(triple)

