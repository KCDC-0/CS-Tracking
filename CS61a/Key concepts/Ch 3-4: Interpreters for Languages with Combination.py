#### Interpreters for Languages with Combination

## Key ideas
# - Expression Trees
# - Parsing expressions
# - Simplification
# - Calculator evaluation




# Parsing is the process of generating expression trees from raw text input
# A parser is a composition of two components: 
# a lexical analyzer and a syntactic analyzer
# First, the lexical analyzer partitions the input string into tokens, 
# which are the minimal syntactic units of the language such as names and symbols
# Second, the syntactic analyzer constructs an expression tree from this sequence of tokens 
# The sequence of tokens produced by the lexical analyzer is consumed by the syntactic analyzer


# Here is an example of expression trees being used in nested lists in scheme

class Pair(object):
    """A pair has two instance attributes: first and second.  For a Pair to be
    a well-formed list, second is either a well-formed list or nil.  Some
    methods only apply to well-formed lists.

    >>> s = Pair(1, Pair(2, nil))
    >>> s
    Pair(1, Pair(2, nil))
    >>> print(s)
    (1 2)
    >>> len(s)
    2
    >>> s[1]
    2
    >>> print(s.map(lambda x: x+4))
    (5 6)
    """
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def __repr__(self):
        return "Pair({0}, {1})".format(repr(self.first), repr(self.second))

    def __str__(self):
        s = "(" + str(self.first)
        second = self.second
        while isinstance(second, Pair):
            s += " " + str(second.first)
            second = second.second
        if second is not nil:
            s += " . " + str(second)
        return s + ")"

    def __len__(self):
        n, second = 1, self.second
        while isinstance(second, Pair):
            n += 1
            second = second.second
        if second is not nil:
            raise TypeError("length attempted on improper list")
        return n

    def __getitem__(self, k):
        if k < 0:
            raise IndexError("negative index into list")
        y = self
        for _ in range(k):
            if y.second is nil:
                raise IndexError("list index out of bounds")
            elif not isinstance(y.second, Pair):
                raise TypeError("ill-formed list")
            y = y.second
        return y.first

    def map(self, fn):
        """Return a Scheme list after mapping Python function FN to SELF."""
        mapped = fn(self.first)
        if self.second is nil or isinstance(self.second, Pair):
            return Pair(mapped, self.second.map(fn))
        else:
            raise TypeError("ill-formed list")

class nil(object):
    """The empty list"""

    def __repr__(self):
        return "nil"

    def __str__(self):
        return "()"

    def __len__(self):
        return 0

    def __getitem__(self, k):
        if k < 0:
            raise IndexError("negative index into list")
        raise IndexError("list index out of bounds")

    def map(self, fn):
        return self

nil = nil()

expr = Pair('+', Pair(Pair('*', Pair(3, Pair(4, nil))), Pair(5, nil)))


# Here are some aspects of simplification:
# Complex expressions are broken down into their constituent parts (sub-expressions)
# Each part is simplified until only atomic values (like numbers or strings) or built-in operators remain
# Once the operands are simplified, the interpreter applies the operator to the results
# The goal of simplification is often to reach a canonical form where no further evaluation rules can be applied

# By reducing expressions early, the interpreter avoids redundant calculations in later stages of execution,
# allows the language to handle nested logic and mathematical combinations by resolving internal dependencies in a specific order,
# while hiding the computation from the user

# In many functional interpreters, "simplify" is functionally synonymous with the Reduce step in the classic Read-Eval-Print Loop (REPL) or the Eval-Apply cycle.


# Below is another example of simplification

from operator import add, sub, mul, truediv

def simplify(value):
    """Return an int if value is an integer, or value otherwise.

    >>> simplify(8.0)
    8
    >>> simplify(2.3)
    2.3
    >>> simplify('+')
    '+'
    """
    if isinstance(value, float) and int(value) == value:
        return int(value)
    return value

def reduce(fn, scheme_list, start):
    """Reduce a recursive list of Pairs using fn and a start value.

    >>> reduce(add, as_scheme_list(1, 2, 3), 0)
    6
    """
    if scheme_list is nil:
        return start
    return reduce(fn, scheme_list.second, fn(start, scheme_list.first))

def calc_eval(exp):
    """Evaluate a Calculator expression."""
    if type(exp) in (int, float):
        return simplify(exp)
    elif isinstance(exp, Pair):
        arguments = exp.second.map(calc_eval)
        return simplify(calc_apply(exp.first, arguments))
    else:
        raise TypeError(exp + ' is not a number or call expression')

def calc_apply(operator, args):
    """Apply the named operator to a list of args."""
    if not isinstance(operator, str):
        raise TypeError(str(operator) + ' is not a symbol')
    if operator == '+':
        return reduce(add, args, 0)
    elif operator == '-':
        if len(args) == 0:
            raise TypeError(operator + ' requires at least 1 argument')
        elif len(args) == 1:
            return -args.first
        else:
            return reduce(sub, args.second, args.first)
    elif operator == '*':
        return reduce(mul, args, 1)
    elif operator == '/':
        if len(args) == 0:
            raise TypeError(operator + ' requires at least 1 argument')
        elif len(args) == 1:
            return 1/args.first
        else:
            return reduce(truediv, args.second, args.first)
    else:
        raise TypeError(operator + ' is an unknown operator')

def as_scheme_list(*args):
    """Return a recursive list of Pairs that contains the elements of args.

    >>> as_scheme_list(1, 2, 3)
    Pair(1, Pair(2, Pair(3, nil)))
    """
    if len(args) == 0:
        return nil
    return Pair(args[0], as_scheme_list(*args[1:]))





