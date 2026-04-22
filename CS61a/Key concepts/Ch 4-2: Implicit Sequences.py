#### Implicit Sequences

## Key Ideas:
# - Iterables and iterators
# - Generators and yield statements



# Iterable are any object that can produce an iterator (e.g., lists, strings, dictionaries, ranges),
# implemented through the __iter__ method
# Iterators are objects that track a position in a sequence

primes = [2, 3, 5, 7]
type(primes)
iterator = iter(primes)
type(iterator)
try:
    next(iterator)
except StopIteration:
    print('No more values')

# Calling iter on an iterator will return that iterator, not a copy
# This behavior is included so that one can call iter on a value to get an iterator without having to worry about whether it is an iterator or a container

# map, filter, zip and reversed functions are examples of functions that return iterables 

items = primes.__iter__()
try:
    while True:
        item = items.__next__()
        print(item)
except StopIteration:
    pass

# here we can implement a for loop using iterators


# A generator is an iterator returned by a special class of function called a generator function
# Generator functions are distinguished from regular functions in that 
# they use yield statement to return elements of a series rather than return statements

def letters_generator():
    current = 'a'
    while current <= 'd':
        yield current
        current = chr(ord(current)+1)

for letter in letters_generator():
    print(letter)

letters = letters_generator()
type(letters)
letters.__next__()
letters.__next__()

# When a generator’s __next__ method is called, the function executes until it hits yield, then "pauses",
# saving its entire environment. It resumes from that exact spot on the next call

# While an iterator is "used up" after one pass
# an iterable class (using yield inside its __iter__ method) can produce fresh generators, 
# allowing for multiple passes over the same data


# 'yield from' can be used to establish a transparent, bidirectional connection 
# between the caller and the sub-generator

def reader():
    """A generator that fakes a read from a file, socket, etc."""
    for i in range(4):
        yield '<< %s' % i

def reader_wrapper(g):
    # Manually iterate over data produced by reader
    for v in g:
        yield v

def reader_wrapper(g):
    yield from g

# These 2 reader_wrapper functions act the same
# manually iterating over reader(), we can just yield from it
# This can be used to implement generative functions recursively

def hailstone(n):
    yield n
    if n == 1:
        yield from hailstone(n)
    elif n % 2 == 0:
        yield from hailstone(n//2)
    else:
        yield from hailstone(3*n + 1)

# The first yield returns the current number in the hailstone sequence while the second yield re-calls the function


# Streams are a functional, recursive approach to lazy evaluation, similar to linked lists but with deferred computation
# A Stream object stores a first element and a compute_rest function (usually a lambda)
# The "rest" of the list is not computed until the .rest property is accessed
# Caching (Memoization): Once the rest of a stream is computed, the result is stored so that subsequent lookups do not re-run the computation

'''class Stream:
    """A lazily computed linked list."""
    class empty:
        def __repr__(self):
            return 'Stream.empty'
    empty = empty()
    def __init__(self, first, compute_rest=lambda: empty):
        assert callable(compute_rest), 'compute_rest must be callable.'
        self.first = first
        self._compute_rest = compute_rest
    @property
    def rest(self):
        """Return the rest of the stream, computing it if necessary."""
        if self._compute_rest is not None:
            self._rest = self._compute_rest()
            self._compute_rest = None
        return self._rest
    def __repr__(self):
        return 'Stream({0}, <...>)'.format(repr(self.first))'''


