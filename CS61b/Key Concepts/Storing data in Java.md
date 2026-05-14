## Memory and Primitive Types
All information in a computer is stored as bits (0s and 1s). Java uses Types to determine how to interpret these bits. There are 8 primitive types: byte, short, int, long, float, double, boolean, and char

Java sets aside a "box" of memory bits when declaring variables depending on the type (eg: 32 bits for an int, 8 bits for a byte). Java provides no way for you to know the location of the box, as the exact memory address is below the accessible level of abstraction.

The Golden Rule of Equals (GRoE): In Java, the assignment operator = always copies the bits from one memory box to another.

```
char c = 'H';
int x = c;
```
In this case, x is returned as 72 since the same bits, 01001000, are used to store the char H and the integer 72


<br>
<br>

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

Here is an implemenation of linked lists:

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