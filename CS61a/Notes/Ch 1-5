#### Control

## Key Ideas:
# - simple and compound statements
# - conditionals
# - iterations
# - testing functions


# Here is the structure for headers and compound statements:
# <header>:
#    <statement>
#    <statement>
#    ...
#<separating header>:
#    <statement>
#    <statement>
#    ...
#...


def fib(n):
	"""Compute the nth Fibonacci number, for n >= 2."""
	if n == 1:
		return 1
	pred, curr = 0, 1
	k = 2
	while k < n:
		pred, curr = curr, pred + curr
		k = k + 1
	return curr

result = fib(8)
	
# Here, we make use of conditionals (if, elif, else), iterators (while)
# and boolean operators (==, True, False) to write the functions


assert fib(8) == 13
# this has no effect unless the assertion is wrong,
# this will result in an assertion error


def sum_naturals(n):
        """Return the sum of the first n natural numbers.

        >>> sum_naturals(10)
        55
        >>> sum_naturals(100)
        5050
        """
        total, k = 0, 1
        while k <= n:
            total, k = total + k, k + 1
        return total


# Another way to test is using the doctest module

from doctest import testmod
testmod() 
# this will run the tests in the docstrings of all functions in this file


from doctest import run_docstring_examples
run_docstring_examples(sum_naturals, globals(), True)

# here we can test a single function using the run_docstring examples
# first argument is the function we want to test
# second argument is the global environment
# the third argument is to say we would like a 'verbose' output

