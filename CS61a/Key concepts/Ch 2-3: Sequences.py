#### Sequences

## Key ideas:
# - lists and strings
# - sequence abstraction
# - common operations
# - Trees
# - linked lists



# All sequences share two primary behaviors:
# Length: A finite number of elements (empty sequences have length 0)
# Element Selection: Access to elements via non-negative integer indices starting at 0

# Here are some examples of built-in sequence types (lists, ranges, strings) and their abstractions:

digits = [1, 8, 2, 8]
len(digits)
[2, 7] + digits[1:] * 2   # [2, 7, 8, 2, 8, 8, 2, 8]
1828 not in digits   # True

pairs = [[10, 20], [30, 40]]

str(2) + ' is an element of ' + str(digits)  # '2 is an element of [1, 8, 2, 8]'
'here' in "Where's Waldo?"  # True

list(range(5, 8))  # [5, 6, 7]

# Here, we can see that values can be checked for membership in a sequence,
# a sequence can be sliced, nested, combined and iterated



# Programs often process sequences through a pipeline of modular operations such as:
# Map (List Comprehensions): Applying an expression to every element in a sequence
# Filter: Selecting a subset of elements that satisfy a specific condition
# Reduce: Applying a function of two arguments cumulatively to the elements of an iterable
# Aggregation: Reducing a sequence to a single value

# Here is the structure for list comprehensions:
# [<map expression> for <name> in <sequence expression> if <filter expression>]

def divisors(n):
    return [1] + [x for x in range(2, n) if n % x == 0]
[n for n in range(1, 1000) if sum(divisors(n)) == n] 

# This example returns a list of perfect numbers from 1 to 1000


# Here are examples of the map, filter and reduce functions:

apply_to_all = lambda map_fn, s: list(map(map_fn, s))
keep_if = lambda filter_fn, s: list(filter(filter_fn, s))

circle_areas = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.00013]
result = list(map(round, circle_areas, range(1, 7)))

pair = lambda l1, l2: list(map(lambda x, y: [x, y], l1, l2))  # same as zip function but pairs in lists instead of tuples
# Python allows for sequence unpacking, which binds multiple names to the elements of a fixed-length sequence in a single step (e.g., for x, y in pairs:)

dromes = ("demigod", "rewire", "madam", "freer", "anutforajaroftuna", "kiosk")
palindromes = list(filter(lambda word: word == word[::-1], dromes))

from functools import reduce
numbers = [1, 3, 5, 7, 9, 11]
result = reduce(lambda x, y: x+y, numbers, 0)


# The tree is a hierarchical data abstraction where:
# Each tree has a root label and a sequence of branches
# Each branch is itself a tree; a tree with no branches is a leaf

def tree(root_label, branches=[]):
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [root_label] + list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def fib_tree(n):
    if n == 0 or n == 1:
        return tree(n)
    else:
        left, right = fib_tree(n-2), fib_tree(n-1)
        fib_n = label(left) + label(right)
        return tree(fib_n, [left, right])
    
# Here we have a function that returns the nth-fibonacci number tree


# A linked list is a manual sequence representation built from nested pairs
# A pair contains the first element and the rest of the list
# The rest of a linked list is either another linked list or an empty value
# Operations like finding length or selecting elements are performed by 
# "peeling away" layers of nested pairs, either through iteration or recursion.

def first(s):
    return s[0]
def rest(s):
    return s[1]

def getitem_link(s, i):
    while i > 0:
        s, i = rest(s), i - 1
    return first(s)

four = [1, [2, [3, [4, 'empty']]]]
getitem_link(four, 1)




