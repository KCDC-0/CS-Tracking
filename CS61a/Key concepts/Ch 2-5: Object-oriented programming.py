#### Object-Oriented Programming

## Key Ideas
# - structure of classes
# - key notation
# - inheritance



# Defining a class is structured as such:
# class <name>:
#     <suite>
# the constructor for the class initialises objects (__init__) 
# Object methods are also defined by a def statement in the suite of a class statement
# Dot Notation (object.attribute) is used to access attributes and invoke methods
# Class names are conventionally written using the CapWords convention

class Account:
    """A bank account that has a non-negative balance."""
    interest = 0.02            # A class attribute
    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder
    def deposit(self, amount):
        """Increase the account balance by amount and return the new balance."""
        self.balance = self.balance + amount
        return self.balance
    def withdraw(self, amount):
        """Decrease the account balance by amount and return the new balance."""
        if amount > self.balance:
            return 'Insufficient funds'
        self.balance = self.balance - amount
        return self.balance

a = Account('John')
b = Account('Harry')
a.balance = 200
b.deposit(100)
a.withdraw(90)
[acc.balance for acc in (a, b)]

a is b  # False
c = a
c is a  # True

# Here, a class is a template (e.g., Account), while an instance is a specific object created from that template (e.g., a,b)
# Instance Attributes are pecific to an individual object (e.g., a specific account balance),
# Class Attributes are shared across all instances of a class

# We can use the build-in funcions getattr and hasattr to access or check attributes of an object using a string
getattr(a, 'balance')
hasattr(b, 'balance')

# Methods are functions defined within a class that operate on instances
# When invoked via dot notation, the instance is implicitly passed as the first argument (self)

'''
Account.deposit(a, 1001)
a.deposit(1000) 

These 2 perform the same action
'''

# It is important to distuingish between class attributes and instance attributes, 
# and what changing each one does

Account.interest = 0.04

# this changes the class attribute 'interest' for all instances of the class
# dot notation is still used (<expression> . <name>)


# Inheritance allows a subclass to take on the attributes and methods of a base class.
# Subclasses can redefine specific methods (e.g., CheckingAccount redefining withdraw) 
# to specialize behavior while inheriting the rest from the parent

# Interfaces are a collection of expected attributes and methods
# Code is more robust when it depends on an object’s interface rather than its specific type

class CheckingAccount(Account):
    """A bank account that charges for withdrawals."""
    withdraw_charge = 1
    interest = 0.01
    def withdraw(self, amount):
        return Account.withdraw(self, amount + self.withdraw_charge)
        

# Python supports the concept of a subclass inheriting attributes from multiple base classes, 
# a language feature called multiple inheritance

class SavingsAccount(Account):
    deposit_charge = 2
    def deposit(self, amount):
        return Account.deposit(self, amount - self.deposit_charge)

class AsSeenOnTVAccount(CheckingAccount, SavingsAccount):
    def __init__(self, account_holder):
        self.holder = account_holder
        self.balance = 1

# Python resolves name conflicts using Method Resolution Order (MRO),
# typically searching from left to right and then upward


# Ultimately, OOP is useful when modeling programs where many systems are interacting with one another
# Although, Python is multi-paradigm; functional abstractions are often better for simple input-output relationships