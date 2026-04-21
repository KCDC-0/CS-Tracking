#### Elements of Programming

## Key ideas:
# - importing Library Functions
# - call Expressions
# - idenitfying nested functions
# - names and environment
# - pure vs non pure functions





# Examples of  expressions and operands

42
total = 2 + 3 + 4 + 5

# these expressions are structured in infix notation where:
# the operator is placed in between the operands

# the math module provides access to common mathematical functions and names

from math import pi
max(3, pi)

# call expressions are structured in Function notation where: 
# the operator is an expression that precedes parentheses, 
# which enclose a comma-delimited list of operand expressions
# the operator and operands are subexpressions


# function notation rather than infix notation allows for:
# - more variables
# - clear nested functions
# - easier expression and more operator types


# the operator module provides access to functions corresponding to infix operators:

from operator import add, sub, mul
my_own_add_func = add
goofy_num = my_own_add_func(14, mul(28, pi))


# Here, we bind the name 'goofy_num' to the value on the left of the =
# Names are also bound via import statements, such as the value for pi
# Names can also be bound to functions, such as for add, sub, mul

num1, num2 = 3, add(mul(2, 4), 3)
num2, num1 = num1, num2
print(goofy_num, num2)

# Names are often refered to as variables, and can be rebound,
# and multiple can be assigned at the same time

# Nested functions work such that python will:
# Evaluate the operator and operand subexpressions, then
# Apply the function that is the value of the operator subexpression 
# to the arguments that are the values of the operand subexpressions,
# repeasting this process recursively if the operands are operators themselves
# this is recursive in nature
# Imagine nested functions as a 'tree' of functions (expression tree)

old_variable = add(2,3)
new_variable = print(2)
print(new_variable)             # this returns 'None', a special Python value that represents nothing

# Functions can be split into pure and non-pure:
# Pure functions (eg: add) have some input and return some output
# Non-pure functions (eg:print), in addition to returning a value, 
# can generate side effects which make some change to 
# the state of the interpreter or computer

# Pure functions are restricted in that 
# they cannot have side effects or change behavior over time
# They tend tend to be simpler to test 
# and can be composed more reliably into compound call expressions

# Non pure funcions tend to have more specific use cases such as print

