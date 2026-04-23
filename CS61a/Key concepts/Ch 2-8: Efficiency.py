#### Efficiency

## Key Ideas:
# - Measuring efficiency
# - Memoization
# - Orders of Growth (Θ Notation)


# Efficiency is defined by the computational resources (time and memory) required by a process
# Since exact timing depends on hardware, efficiency is more reliably measured by counting events, such as function calls
# Time Requirements are often measured by the total number of recursive calls or operations
# Space Requirements are measured by the maximum number of active environment frames required simultaneously

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-2) + fib(n-1)

def count(f):
    def counted(*args):
        counted.call_count += 1
        return f(*args)
    counted.call_count = 0
    return counted

def count_frames(f):
    def counted(*args):
        counted.open_count += 1
        counted.max_count = max(counted.max_count, counted.open_count)
        result = f(*args)
        counted.open_count -= 1
        return result
    counted.open_count = 0
    counted.max_count = 0
    return counted


fib1 = count(fib)
fib2 = count_frames(fib)
fib1(19)
fib2(19)
fib1.call_count
fib2.max_count

# Here, the higher-order count function returns an equivalent function to its argument that also maintains a call_count attribute
# The higher-order count_frames function tracks open_count, the number of calls to the function f that have not yet returned
# The max_count attribute is the maximum value ever attained by open_count
# We use these functions to determine the efficiency of a fibonacci function

# From the result we can conclude that in functions like the recursive fib(n),
# time grows exponentially due to redundant calculations, 
# while space grows linearly because the interpreter only tracks nodes along the current path to the root



# Memoization is an optimization technique that stores the results of expensive function calls in a cache, such as a dict
# When a function is called with a previously seen argument, it returns the cached value instead of re-computing it
# This transforms exponential-time tree recursions into linear-time processes by ensuring each unique input is processed only once

def memo(f):
    cache = {}
    def memoized(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    return memoized

counted_fib = count(fib)
fib  = memo(counted_fib)
fib(19)
fib(34)
counted_fib.call_count

# The fib function will make less calls that expected in fib(34) due to the cached data



# Orders of growth categorize processes by how their resource requirements scale as the input n increases
# A process is Θ(f(n)) if its requirement R(n) is "sandwiched" between k1​⋅f(n) and k2​⋅f(n) for large n (big O and big Omega)
# It is often used to describe the average-case complexity, providing a more precise analysis than Big O alone
# as it signifies that an algorithm's growth rate is bounded both from above and below by the same function

# Key Analysis Rules:
# Constants: Ignored (e.g., Θ(500n) simplifies to Θ(n))
# Logarithms: The base does not matter; all logarithmic growth is Θ(logn)
# Nesting: If an inner process of Θ(n) is repeated by an outer process of Θ(m), the total is Θ(m⋅n)
# Lower-order Terms: Only the fastest-growing term is kept (e.g., Θ(n2+n) becomes Θ(n2))

# Common Growth Categories:
'''
Category 	    Theta Notation 	    Growth Description 	                        Example

Constant 	    Θ(1) 	            Growth is independent of the input 	        abs
Logarithmic 	Θ(logn) 	        Multiplying input increments resources 	    fast_exp
Linear 	        Θ(n) 	            Incrementing input increments resources 	exp
Quadratic 	    Θ(n^2) 	            Incrementing input adds n resources 	    one_more
Exponential 	Θ(b^n) 	            Incrementing input multiplies resources 	fib
Others          Θ(sqrt(n)) etc.     Depends on function                         count_factors
'''

