#### Exceptions

## Key Ideas:
# - Nature of exceptions
# - Exception objects
# - Advantages of exceptions 


# Exceptions are used to signal that an error has occurred and transfer control 
# directly to a designated part of the program equipped to handle it

# When an exception is raised, the current code block stops immediately
# If unhandled, the Python interpreter terminates or returns to the interactive loop and prints a stack backtrace

# All exceptions are objects. They must inherit (directly or indirectly) from the BaseException class

# raise Exception('An error occurred')



# An exception can be handled by an enclosing try statement as follows:
# try:
#     <try suite>
# except <exception class> as <name>:
#     <except suite>

def invert(x):
    try:
        return invert(x)
    except ZeroDivisionError as e:
        return str(e)

def check_zero(x):
    try:
        assert x == 0, 'number should be 0'
    except AssertionError as e:
        print('handling a', type(e))
        x = 0


# One can create custom exception classes by inheriting from Exception

class IterImproveError(Exception):
    def __init__(self, last_guess):
        self.last_guess = last_guess

def improve(update, done, guess=1, max_updates=1000):
    k = 0
    try:
        while not done(guess) and k < max_updates:
            guess = update(guess)
            k = k + 1
        return guess
    except ValueError:
        raise IterImproveError(guess)
    

# Exceptions allow long-running programs to log errors and continue serving requests instead of crashing

# Python'x exception handling separates the iterative improvement logic (try block)
# from the error-handling logic (the except block), 
# making code cleaner and easier to maintain

