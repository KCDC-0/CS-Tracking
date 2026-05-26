## Inheritance

A mechanism to generalize behavior by relating specific subtypes to broader categories. It reduces code repetition by sharing common properties and methods. Thus, various distinct types inherit from a single generic class, known as polymorphism.

When a child class uses the 'extends' keyword, it inherits behaviors and state from a parent class. Specifically, all non-private instances and static variables, non-private methods, and nested classes are inherited, while private variable and methods, and consructors are not inherited.

As an example of this, every class in Java automatically extends the Object class.

<br>

By default,hild constructors automatically call the parent's default (no-argument) constructor first. To call a specific, non-default parent constructor, the  'super()' keyword must be used as the very first line of the child constructor.

Here is an example of inheritance
```
public class Parent {
    public Parent() {
        System.out.println("Default constructor");
    }
    public Parent(String say) {
        System.out.println(say);
    }
    void doStuff() { ... }
}

// Child inherits doStuff(), but not the constructors.
public class Child extends Parent {
    public Child() {
        System.out.println("Child")
    }
    public Child(String say) {
        super(say);
    }
}
    
public static void Main(String[] args) {
    Child c1 = new Child(); // will print "Default constructor" then "Child"
    Child c2 = new Child("Hi"); // will print "Hi"
}
```

<br>
<br>

Method overriding (using the @Override tag) can be used to redefine a parent's method in a child class to change its behavior. The parent's original behavior can still be accessed inside the child using super.parentMethod().

Method overloading (methods using the same name within a class) can be used to create multiple methods within the same class that share the same name but accept different parameters. However, it is highly repetitive, increases code maintenance, and is limited strictly to the explicitly defined data types.

<br>
<br>


## Interfaces and abstract classes

Interfaces act as a blueprint for an object, defining what it should do, not how. It acts similar to regular clases except:

- Variables are strictly constants (public static final)
- Methods have no bodies, only signatures (unless using the 'default' keyword, not encouraged)
- A class can implement multiple interfaces using the 'implements' keyword

<br>

This is an example of an interface:
```
public interface AnInterface<Item> {
  public void doStuff(Item x);
  public Item getItem();
  ...
}

public class Something implements AnInterface<Item> { // Note the IMPLEMENTS
 @Override
 public void doStuff(Item x) {
     // implement method
 }

 @Override
 public void getItem() {
     // implement method
 }
}

public class MainClass {
  public static void main(String[] args) {
      AnInterface<String> smth = new AnInterface<>(); // ERROR
      // (new can't be used with interfaces.)
      AnInterface<String> smthElse = new Something<String>(); // Will not error
      smth.getItem();
      ...
  }
}
```

<br>

Abstract classes on the other hand serve as a hybrid between interfaces and concrete classes:

- variables behave like normal instance variables
- they can contain both fully implemented methods and abstract methods (signatures with no bodies)
- A class can only extend one abstract class using the extends keyword

<br>

This is how it would be used in the same example as before
```
public abstract class AnAbstract<Item> {
  public abstract void doStuff(Item x);
  public abstract Item getItem();
  ...
}

public class Something extends AnAbstract<Item> { // EXTENDS, not implements
 @Override
 public void doStuff(Item x) {
     // implement method
 }

 @Override
 public void getItem() {
     // implement method
 }
}

public class MainClass {
  public static void main(String[] args) {
      AnAbstract<String> smth = new AnAbstract<>(); // ERROR
      // (new can't be used with abstract classes, just like interfaces.)
      AnAbstract<String> smthElse = new Something<String>(); // Will not error
      smth.getItem();
      ...
  }
}
```

<br>
<br>

## Access control

Access control allows for clean self-documentation and means that it’s safe to change private methods without worrying about breaking things. It also means that private and protected variables don’t need to be understood by users.

Levels of access control:

- Private: Only this class can see it
- Package Protected (the default level): All classes in the same package can see it
- Protected: Subclasses (that inherit from the parent) can also see it
- Public: All classes in the program can see it