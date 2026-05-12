
## In Java, a variable is a container of a specific size and shape.

In Python, this is fine:
```
x = 10 
x = "ten" 
```


In Java, x can only ever hold an integer: 
```
int x = 10;
```

Java must be compiled into bytecode before it runs.

Source (.java) $\rightarrow$ Compiler (javac) $\rightarrow$ Bytecode (.class) $\rightarrow$ JVM (java)

<br>
<br>

## Everything must belong to a Class. 
You cannot have a "floating" function like in Python.
An algorithm isn't just a script, it’s usually a method inside a class.

Java splits data into Primitives (int, double, boolean), and Objects (String, Arrays, Classes).
Primitives are stored directly in the "Stack" (fast) such that passing it to a function copies the value while objects are stored in the "Heap" where the variable only holds a reference (pointer) and passing it to a function copies the reference

When making functions in Java, one must declare the visibility, the return type, and the parameter types. The keyword 'static' is used to associate a member with a class rather than with an instance of the class, ie. an object. Instance variables or non-static variables store data unique to each instance. To instantiate an object, the 'new' keyword is used. This allocates memory for the object and returns a reference to it. In classes, constructors can be implemented similar to python.

<br>

```
public int add(int a, int b) {
    return a + b;
}
```
<br>

The ```public static void main(String[] args)``` method is static so that the Java Virtual Machine (JVM) can call it to start the program without needing to create an instance of the class

public: Accessible from anywhere

static: Called by the Java interpreter without needing to instantiate the class first

void: Returns no value

main: This is the name of the method

String[] args: An array of strings representing Command Line Arguments passed to the main method during execution

