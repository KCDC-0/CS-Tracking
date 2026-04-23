#### Object Abstraction

## Key Ideas:
# - string coversion
# - special methods
# - class interface
# - generic functions



# Python stipulates that all objects should produce two different string representations: 
# one that is human-interpretable text and one that is a Python-interpretable expression
# The constructor function for strings, str, returns a human-readable string
# Where possible, the repr function returns a Python expression that evaluates to an equal object

from datetime import date
tues = date(2011, 9, 12)
repr(tues) == tues.__repr__()
str(tues) == tues.__str__()



# Python uses "special methods" (dunder methods) to provide a consistent interface for built-in behaviors.
# __repr__: Returns a "canonical" string for the interpreter (ideally an expression to recreate the object).
# __str__: Returns a human-readable string.
# Here are others:
# Truth Values __bool__: Objects can define their own logic for truthiness (e.g., an instance is False if a certain attribute is 0).
# Sequence Behavior: __len__ defines the result of len(), and __getitem__ enables element selection via brackets [].
# Callable Objects: Implementing __call__ allows an instance of a class to be invoked like a function




# A shared set of attribute names and behaviors is called an interface 
# and allows different classes to be used interchangeably
# The @property Decorator allows methods to be accessed like attributes 
# (e.g., obj.magnitude instead of obj.magnitude()), 
# enabling "on-the-fly" computation to keep different representations consistent

from math import atan2, sin, cos, pi

class Number:
    def __add__(self, other):
        return self.add(other)
    def __mul__(self, other):
        return self.mul(other)
        
class Complex(Number):
    def add(self, other):
        return ComplexRI(self.real + other.real, self.imag + other.imag)
    def mul(self, other):
        magnitude = self.magnitude * other.magnitude
        return ComplexMA(magnitude, self.angle + other.angle)
    
class ComplexRI(Complex):
        def __init__(self, real, imag):
            self.real = real
            self.imag = imag
        @property
        def magnitude(self):
            return (self.real ** 2 + self.imag ** 2) ** 0.5
        @property
        def angle(self):
            return atan2(self.imag, self.real)
        def __repr__(self):
            return 'ComplexRI({0:g}, {1:g})'.format(self.real, self.imag)

class ComplexMA(Complex):
    def __init__(self, magnitude, angle):
        self.magnitude = magnitude
        self.angle = angle
    @property
    def real(self):
        return self.magnitude * cos(self.angle)
    @property
    def imag(self):
        return self.magnitude * sin(self.angle)
    def __repr__(self):
        return 'ComplexMA({0:g}, {1:g} * pi)'.format(self.magnitude, self.angle/pi)

num = ComplexRI(1, 2) + ComplexMA(2, pi/2)
random_num = num.imag + num.angle

# Here, we are able to use the interface approach to encoding multiple representations of complex numbers



# Generic functions allow operations to work across heterogeneous types, here are some implementation methods:
# Shared Interfaces: Different types implement the same method names, allowing a single function to work on any type that follows the interface
# Type Dispatching: The function explicitly checks the "type tag" or class of the arguments, through a lookup table such as a dict
# to find the specific function designed to handle that pair of types
# Type Coercion: Instead of writing functions for every possible combination, one type is "coerced", or converted, into another

# Here is an example:

from typing import TypeVar

T = TypeVar('T')
U = TypeVar('U')

def combine(a: T, b: U) -> str:
    return str(a) + str(b)

combine('hello', 2020)

# Python's TypeVar is used to denote the placeholder type T
# The function above concatenates two different data types T and U into a string



