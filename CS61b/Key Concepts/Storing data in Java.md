## Memory and Primitive Types
All information in a computer is stored as bits (0s and 1s). Java uses Types to determine how to interpret these bits. There are 8 primitive types: byte, short, int, long, float, double, boolean, and char

- boolean: 1 bits, not signed (eg: true, false)
- byte: 8 bits, signed (eg: 3, (int)17)
- short: 16 bits, signed (must cast from int)
- char: 16 bits, not signed	(eg: \u0000 (default), ‘a’, ‘\n’)
- int: 32 bits, signed (eg: 0 (default), 123, 0100 (octal), 0xff (hex))
- long: 64 bits, signed (eg: 0 (default), 123L, 0100L, 0xffL)
- float: 32 bits, signed (eg: 0.0 (default), 1.23f, -1.23e10f, .001f)
- double: 64 bits, signed (eg: 0.0 (default), 1.23e256d, 1e1d, 1.2e-10d)

<br>

Java sets aside a "box" of memory bits when declaring variables depending on the type (eg: 32 bits for an int, 8 bits for a byte). Java provides no way for you to know the location of the box, as the exact memory address is below the accessible level of abstraction.

The Golden Rule of Equals (GRoE): In Java, the assignment operator = always copies the bits from one memory box to another.

```
char c = 'H';
int x = c;
```
In this case, x is returned as 72 since the same bits, 01001000, are used to store the char H and the integer 72


<br>
<br>

Type conversion between primitive tyoes occurs automatically when converting to a larger container (no information lost). However, explicit casting is required when converting from a larger to a smaller container.


## Reference Types

Any type that is not one of the 8 primitives (e.g., Objects, Arrays) is a Reference Type. A reference variable box does not store the object's data itself, but instead a 64-bit memory address (a pointer) to where the object exists in memory.

```
Walrus a = new Walrus(1000, 8.3);
Walrus b;
b = a;
b.weight = 5;
System.out.println(a);
System.out.println(b);

int x = 5;
int y;
y = x;
x = 2;
System.out.println("x is: " + x);
System.out.println("y is: " + y);
```

Due to this implementation, in the code above, a and b both change as they both contain a memory address refering to the same walrus instance, while y remains 5 as is a different integer instance than x.
A reference variable containing all zeros is represented as null


<br>
<br>

## Object class

In Java, all objects inherit from the master Object class. Here are som propertirs of the object type:

- toString(): Defaults to returning the class name and memory address - typically overridden to provide a user-friendly string representation
- equals(Object obj): Defaults to checking if memory addresses match - typically overridden to evaluate if the actual contents of the objects are equivalent
- hashCode(): Returns a numeric hash for the object. If you override equals(), you must also override this to ensure equal objects return the same hash code
- getClass(): Returns the specific class of the object

<br>
<br>


## Arrays

Arrays are reference types, thus declaring an array allocates 64 bits for the address. Using the keyword 'new' allocates the actual space for the array elements. When comparing arrays '==' compares the bits (the addresses) and only returns true if both variables point to the same object. Arrays.equals() compares the content of the arrays.

```
int[] x = new int[]{0, 1, 2, 95, 4};
int[] y = new int[]{0, 1, 2, 95, 4};
System.out.println(x == y);
System.out.println(Arrays.equals(x, y));
```

Thus, the first line will outpiut false and the second line will output true

<br>

Here is an implemenation of linked lists without using arrays:

```
public class IntList {
    public int first;
    public IntList rest;        

    public IntList(int f, IntList r) {
        first = f;
        rest = r;
    }
}

public int size() {
    if (rest == null) {
        return 1;
    }
    return 1 + this.rest.size();
}
```

<br>

Some features of arrays include:
- Arrays consist of a fixed integer length N
- They contain a numbered sequence of memory boxes indexed from 0 to N - 1
- All boxes within an array must contain data of the exact same type
- Unlike classes, arrays do not possess member methods
- Can be copied using System.arraycopy
- Indices can be dyncamicallly computed at runtime, unlike class fields

However unlike other languages, they do not support slicing syntax and cannot dynamically shrink or expand.

<br>

System.arraycopy takes five parameters:

The array to use as a source, where to start in the source array, the array to use as a destination, where to start in the destination array, how many items to copy


Here is an implementation of the key syntax involving arrays:
```
int[] z = null;
int[] x, y;

x = new int[]{1, 2, 3, 4, 5};
y = x;
x = new int[]{-1, 2, 5, 4, 99};
y = new int[3];
z = new int[0];
int xL = x.length;

String[] s = new String[6];
s[4] = "ketchup";
s[x[3] - x[1]] = "muffins";

int[] b = {9, 10, 11};
System.arraycopy(b, 0, x, 3, 2);
```

2D arrays can also be implemented as arrays of arrays

Since arrays in Java cannot be resized, a new array needs to be created each time we want to extend our list. Thus, array resizing (through a geometric factor or otherwise) may be considered to reduce the performance toll of creating new arrays.

<br>
<br>


## Testing

Testing is a way to reduce "cognitive load" by allowing one to focus on one small problem at a time, ensuring each "unit" of the program is a solid foundation before moving to the next.

<br>

Methodologies of testing include:
- Ad-hoc/Manual Comparison: writing custom loops to compare expected vs actual output using '==' and '.equals'
- Library-Based Testing: using libraries like Google Truth (eg assertThat(actual).isEqualTo(expected)) to automate comparison and get detailed failure messages, modern IDEs also support visual cues for errors
- Unit Testing: Verifying individual, isolated components
- Integration Testing: Verifying that multiple units interact correctly

Test-driven development is a philosophy where tests are written before the functional code.

<br>
<br>


## Access control and management

Private variables and methods can only be accessed by code inside the same .java file, and acts as a signal for users to ignore that function or variable. ON the other hand, the public keyword can be considered a signal that a method is available and will work forever exactly as it does now.

An invariant is a fact about a data structure that is guaranteed to be true.

Nested classes can also be implemented in Java as a way to organise code. If a nested class does not need to access the outer class's instance variables, it is declared static. This saves memory by eliminating the inner class's reference to its parent class.

Here is an implementation of a nested class
```
public class SLList {
       public class IntNode {
            public int item;
            public IntNode next;
            public IntNode(int i, IntNode n) {
                item = i;
                next = n;
            }
       }

       private IntNode first; 

       public SLList(int x) {
           first = new IntNode(x, null);
       } 
...
```
<br>
<br>


## Generic types

To allow data structures to hold any reference type rather than just integers, Java uses Generics with angle bracket syntax '<>'. 

```
public class SomeClass<SomeType> {
    private SomeType someThing;

    public void someMethod(SomeType stuff) {
        doStuff(stuff);
    }
}

...
/** Creates a new instance of SomeClass, setting SomeType to String.
    We don't need to put the type on the right since it's already
    defined on the left. */
SomeClass<String> aClass = new SomeClass<>();
```
<br>

To put constraints on what kinds of types can be passed into a generic typem one can either specify that a generic type must fit within a type bound, or specify that a type can be a supertype of a specified type.

Here is an example of both ways to apply constraints:
```
class SomeClass<T extends Number> {
    // A method that takes a type parameter T and takes any SUPERCLASS
    // of T as a list generic type.
    static <T> void doSomething(List<? super T> L) { ... }
}
```
<br>

Generics do not support primitives (e.g., int, double). Instead, use their corresponding object wrapper reference types (e.g., Integer, Double).

Additionally, the 'instanceof' operator does not work properly with generic types, and cannot differentiate between differently typed generic objects at runtime

<br>

