#### Defining New Functions

## Key ideas:
# - defining functions
# - environment

def middle(x, y, z):
    l = [x, y, z]
    l.remove(max(x, y, z))
    l.remove(min(x, y, z))
    return l[0]


# Here is a simple function to find the middle of 3 values
# User defined functions on python follow the following syntax:
# def <name>(<formal parameters>):
#    return <return expression>
# where the contents of the function are indented
# Here, the other functions min and max are used as building blocks
# All functions, user-defined, in-built, and imported work this way
# Functions can have different function signatures, or parameters they are allowed to take


'''
f = max
max = 3
result = f(2, 3, 4)
max(1, 2)  # Causes an error
'''

# An environment in which an expression is evaluated consists of a sequence of frames
# Each frame contains bindings, 
# each of which associates a name with its corresponding value/function
# There is a single global frame.
# A def statement binds a name to a user-defined function created by the definition

# In the example in the mulit-line string above, max is now an integer and not a function,
# thus an error is returned, yet f acts as the original max function

from operator import add
def mean (x, y):
    return (add(x,y)/2)

result = mean(mean(2, 3), 5)
print(result)

# In the above example: A new local frame is introduced which binds x to 2 and y to 3
# Environment diagram:

# Global                |    Mean                 |   Mean                 |
# | add    | add func   |    | x            | 2   |   | x            | 2.5 |
# | mean   | mean func  |    | y            | 3   |   | y            | 5   |
# | result | 3.75       |    | return value | 2.5 |   | return value | 3.75|
# 
# Local frames keeps the names separate
# the scope of a local name is limited to the body of the user-defined function
# for example, x and y are out of scope outside the function mean
# This framework applies to all functions 


from operator import truediv, floordiv
remainder = truediv(5, 4) - floordiv(5, 4)
remainder = (remainder * 3) / 4

# infix operators require parenthesis for ordering, but also have call expression counterparts
