#### Data Abstraction


## Key ideas:
# - characteristics of data abstraction
# - abstraction barriers
# - benefits of using data abstraction



# Data abstraction is a methodology that separates how data is used from how it is represented
# Programs operate on data as high-level conceptual units without knowing the internal details
# The actual implementation (e.g., using a list or a function) is defined independently
# These layers are connected by a specific set of functions:
# Constructors: Functions that create the data (e.g., rational(n, d))
# Selectors: Functions that access specific parts of the data

# Abstraction barriers are used to seprarate higher and lower order functions on a data type
# Functions at a higher level should never "reach across" a barrier to use lower-level implementations,
# to make programs easier to maintain and to modify without needing to worry about lower level abstractions

# Here is an example of abstraction barriers using an implementation of the data type 'rational numbers':
# Parts of the program that... 	                        Treat rationals as... 	            Using only...
# Use rational numbers to perform computation 	        whole data values 	                add_rational, mul_rational, rationals_are_equal, print_rational
# Create rationals or implement rational operations 	numerators and denominators 	    rational, numer, denom
# Implement selectors and constructor for rationals 	two-element lists 	                list literals and element selection


# Here is another example of data abstraction:
def pair(x, y):
    """Return a function that represents a pair."""
    def get(index):
        if index == 0:
            return x
        elif index == 1:
            return y
    return get

def select(p, i):
    """Return the element at index i of pair p."""
    return p(i)

# Data abstraction allows for:
# - Modularity of code, each 'level' of abstraction can be altered without worrying about the others
# - High-level logic ca be written assuming the constructor and selectors already exist before actually implementing them
# - Logic can be centralized in the constructor without affecting the rest of the application