# Day 018 - Object Oriented Programming Cont'd

The purpose of this day is to finally become the implementer of a Java class. We will be implementing the `Point` class previously discussed and then testing it with the testing code we wrote the previous day.

It is recommended that you look at the solution from the previous day to make sure that your testing code adequately tests the correctness of your `Point` object.

## Starter Code

This day includes a single file in the starter-code folder titled `Point.java`. This includes the
boilerplate structure of an Java class.Most of the structure has been laid out for you, which we will discuss down below, it's your job to implement the methods.

As a reminder, here's the syntax for making a new point:

### Syntax
```
Point p1 = new Point(4, 8);
```

You can optionally create a point at the origin by omitting the parameters like so:

### Syntax
```
Point p1 = new Point();
```

Here are the methods that the Point class has available to use:

* `translate(int x, int y)`
  * adds the given values to the x and y coordinates of the point
* `distanceFromOrigin()`
  * returns a double representing the distance from the point to the origin
* `toString()`
  * returns a String representation of the point
  * Ex. (3, 6)
* `distanceFrom(Point otherPoint)`
  * returns a double representing the distance from this point to the given point
* `getX()`
  * returns the point's x coordinate
* `getY()`
  * returns the point's y coordinate
* `setLocation(int x, int y)`
  * changes the point's x and y coordinates to the given values
  
## Getting Started

The first thing to notice about the `Point.java` file is that there is no main method defined anywhere in the class. This is perfectly fine, because no one will ever run our program. Like we said before: we are no longer the client, we are now writing code for someone else to use.

Let's outline the overall structure of the class:

```
public class Name {

 // fields
 private type name;

 // constructors
 public Name( ... ) {
 
 }
 
 public Name() {
 
 }
 
 // methods
 public type name( ... ) {
 
 }
 
 public type name() {
 
 }
 
}
```

At the very top of the class we have our fields. **Fields** are variables inside an object that keep track of some important piece of information. Each object has its own copy of each field. Specifically for the `Point` class, we have two fields, one for keeping track of both the x and y coordinates.

### Syntax
```
private type name;
```

### Example
```
private int x;
```

The reason they are made `private` is a stylistic decision, and common practice in Java. A good analogy for this is the warranty placed on electronic devices. There is usually a message on the bottom of your phone/radio that says if you open the case and mess around with the insides then you will void the warranty. This is because once you start to mess with the inner state of the object, the program can no longer make guarantees that it will work anymore. We need to maintain control of our fields so that people can't maliciously or accidently mess them up.

The next thing to talk about are the **constructors**. These are special methods that are run exactly one time: when the object is first constructed. More specifically, when the client uses the `new` keyword, our constructor will be run, potentially taking in parameters. The constructors job is to initialize the value of the fields. If a `Point` object is constructed like so:

```
Point p1 = new Point(2, 6);
```

Then the x and y coordinate fields should be updated accordingly. The nice thing about fields is that they have **global scope** in your class. This means that they can be accessed anywhere, including in your constructor. You can modify your fields the same way you would modify a variable.

The final thing in classes are the **instance methods**. They follow the same syntax as the methods that you're used to, but without the `static` keyword.

### Syntax
```
public type name(parameters) {
 statement(s);
}
```

### Example
```
public void shout() {
 System.out.println("HELLO");
}
```

We've seen many examples of these types of methods with the classes we used previously. Things like `drawRect` from `DrawingPanel` or `nextInt` from `Scanner`.

It's normal to feel overwhelmed, since this is a lot of new information all at once. Refer back to this page if you get stuck, and good luck!



