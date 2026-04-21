#### Mutable Data

## Key Ideas:
# - Object Metaphors
# - Identity vs equality
# - Tuples
# - Dictionaries
# - non-local assignment
# - dispatch functions


# Objects combine data values with behavior
# Object behavior is implemented in Python through specialized object syntax and associated terminology
# Here is the notation for object attributes:
# <expression> . <name>


from datetime import date
tues = date(2014, 5, 13)
tues.strftime('%A, %B %d')

# Here we see that Dates are objects, but numbers, strings, lists, and ranges are all objects as well

'1234'.isnumeric()  # True
'rOBERT dE nIRO'.swapcase()  # 'Robert De Niro'


# Identity (is): Checks if two expressions evaluate to the exact same object in memory.
# Equality (==): Checks if two objects currently have the same contents.

chinese = ['coin', 'string', 'myriad']
suits = chinese
suits.pop()
suits.remove('string')
suits.append('cup')
suits.extend(['sword', 'club'])
suits[2] = 'spade'
suits[0:2] = ['heart', 'diamond']
nest = list(suits)

suits is chinese  # True
suits is nest  # False
suits == nest  # True

# Here suits and chinese refer to the same value and thus they are both altered
# On the other hand, the list constructor function binds "nest" to a second list with the same elements


# Like lists, tuples have a finite length and support element selection, but are immutable

nest = (10, 20, [30, 40])
nest[2].pop()

# dictionary are a built-in data type containing key-value pairs, 
# where both the keys and values are objects
# The purpose of a dictionary is to provide an abstraction for storing and retrieving values that are indexed by descriptive keys instead of integers
# Dictionaries do have some restrictions:
# - A key of a dictionary cannot be or contain a mutable values (strings/tuples instead of lists/sets).
# - There can be at most one value for a given key.

numerals = {'I': 1, 'V': 5, 'X': 10}
numerals['L'] = 50

{x: x*x for x in range(3,6)}
# Here is an example fo dictionary comprehension



def make_withdraw(balance):
    """Return a withdraw function that draws down balance with each call."""
    def withdraw(amount):
        nonlocal balance                 # Declare the name "balance" nonlocal
        if amount > balance:
            return 'Insufficient funds'
        balance = balance - amount       # Re-bind the existing balance name
        return balance
    return withdraw

# This user-defined function is non-pure. 
# Calling the function not only returns a value, 
# but also has the side effect of changing the function in some way, 
# so that the next call with the same argument will return a different result

# The nonlocal statement declares that whenever we change the binding of the name balance, 
# the binding is changed in the first frame in which balance is already bound

# Without the nonlocal statement, UnboundLocalError appears because balance is assigned locally in the withdraw function, 
# and so Python assumes that all references to balance must appear in the local frame as well
# UnboundLocalError: local variable 'balance' referenced before assignment

# This allows for state to be encapsulated and hidden from the rest of the program, accessible only through specific functions
# However, introducing mutable data breaks referential transparency—the idea that an expression can be replaced by its value without changing the program's behavior
# Programs with mutation are harder to reason about because the value of an expression depends on the history of the environment

# The key to correctly analyzing code with non-local assignment is to remember that only function calls can introduce new frames
# Assignment statements always change bindings in existing frames



# Dispatch Functions is a technique where a single function manages data by receiving a "message" (usually a string) and a value
# This can be used to make complex data types like lists or dictionaries from scratch using functions and nonlocal state

def account(initial_balance):
    def deposit(amount):
        dispatch['balance'] += amount
        return dispatch['balance']
    def withdraw(amount):
        if amount > dispatch['balance']:
            return 'Insufficient funds'
        dispatch['balance'] -= amount
        return dispatch['balance']
    dispatch = {'deposit':   deposit,
                'withdraw':  withdraw,
                'balance':   initial_balance}
    return dispatch

def withdraw(account, amount):
    return account['withdraw'](amount)
def deposit(account, amount):
    return account['deposit'](amount)
def check_balance(account):
    return account['balance']

a = account(20)
deposit(a, 5)
withdraw(a, 17)
check_balance(a)



# Propogating constraints is form of declarative programming,
# where the relationships between variables rather than the specific steps to calculate them
# The Constraint Network Model is built using two primary components:
# Connectors: Objects that hold a value and link to various constraints. When a connector’s value is set, it notifies all linked constraints.
# Constraint Boxes: Primitive computational units (like an adder, multiplier, or constant) that enforce a mathematical relationship between the connectors attached to them



def connector(name=None):
    """A connector between constraints."""
    informant = None
    constraints = []
    def set_value(source, value):
        nonlocal informant
        val = connector['val']
        if val is None:
            informant, connector['val'] = source, value
            if name is not None:
                print(name, '=', value)
            inform_all_except(source, 'new_val', constraints)
        else:
            if val != value:
                print('Contradiction detected:', val, 'vs', value)
    def forget_value(source):
        nonlocal informant
        if informant == source:
            informant, connector['val'] = None, None
            if name is not None:
                print(name, 'is forgotten')
            inform_all_except(source, 'forget', constraints)
    connector = {'val': None,
                 'set_val': set_value,
                 'forget': forget_value,
                 'has_val': lambda: connector['val'] is not None,
                 'connect': lambda source: constraints.append(source)}
    return connector

def inform_all_except(source, message, constraints):
    """Inform all constraints of the message, except source."""
    for c in constraints:
        if c != source:
            c[message]()

from operator import add, sub
def adder(a, b, c):
    """The constraint that a + b = c."""
    return make_ternary_constraint(a, b, c, add, sub, sub)

def make_ternary_constraint(a, b, c, ab, ca, cb):
    """The constraint that ab(a,b)=c and ca(c,a)=b and cb(c,b) = a."""
    def new_value():
        av, bv, cv = [connector['has_val']() for connector in (a, b, c)]
        if av and bv:
            c['set_val'](constraint, ab(a['val'], b['val']))
        elif av and cv:
            b['set_val'](constraint, ca(c['val'], a['val']))
        elif bv and cv:
            a['set_val'](constraint, cb(c['val'], b['val']))
    def forget_value():
        for connector in (a, b, c):
            connector['forget'](constraint)
    constraint = {'new_val': new_value, 'forget': forget_value}
    for connector in (a, b, c):
        connector['connect'](constraint)
    return constraint