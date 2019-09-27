# Day 017 - Object Oriented Programming

The purpose of this day is to introduce an almost entirely new concept: object-oriented programming. Even though this chapter is based on procedural programming, object oriented programming is an incredibly important concept and one of the most relevant for Java. Almost all of the things we learned up to this point were not really unique to Java. Every programming concept we learned (if statements, loops, booleans, arrays) can be written in slightly different ways in other programming languages. Once you understand the concept, it's easy to transfer over your understanding to other languages. You'll find that Java is more strict than most programming languages, so other languages will be a relief in terms of syntax.

Object-oriented programming is something that Java thrives in. It's a different way of thinking about a problem. No longer are we going to be writing the program that does all of the work of taking user input and calculating information and whatnot. For this challenge, there will be a distinction between the **client** program and the **implementer** program.

If you want to think of an immediate example, back in the early chapters when were doing simple animations, we were clients of the `DrawingPanel` object. This is because our program used another class to accomplish a task. That's the essence of object oriented programming. Instead of starting from scratch, I was able to use an existing class that greatly simplified my task. And the nicest part about it was that we didn't have to understand a single line of code in the `DrawingPanel.java` file. There was a level of abstraction between the client and the implementer (whoever wrote `DrawingPanel`) that allowed me to just know what the methods were and how to use them.

You can imagine your boss came to you and asked you for some functionality of your object. He wants to be able to write `drawRect` in his program and for a rectangle to appear on the screen. That's now our job to make that happen.

Imagine you want an object that can store information about a coordinate. It stores two pieces of information together (an x and y coordinate). You also want certain functionality out of your object. You want there to be methods available that tell you information about that coordinate. For example, we want there to be a method called `distanceFromOrigin` that we can call at any time that will return that point's distance from the origin as a `double`. 

Later we are going to actually implement this, but for now we want to write testing code so that we can test what we write later. This may seem counter-intuitive, but it's actually very common programming practice. We're the ones implementing the code anyways; we get to decide what correct means. For this challenge, you will be writing testing code for a `Point` object. 

## Starter Code

This day includes a single file in the starter-code folder titled `Starter.java`. This includes the
boilerplate structure of a Java program.

All of the code that you write will go inside of the main method.

Imagine another file exists in the same directory as your file called `Point.java`. 

Here's the syntax for making a new `Point`:

### Syntax
```
Point p1 = new Point(4, 8);
```

Notice how this is very similar to how we've created objects like `DrawingPanel` and `Scanner` in the past. The two parameters signify the initial x and y coordinates of the point object.

You can optionally create a point at the origin by omitting the parameters like so:

### Syntax
```
Point p1 = new Point();
```

Here are the methods that the `Point` class has available to use:

* `translate(int x, int y)`
  * adds the given values to the x and y coordinates of the point
* `distanceFromOrigin()`
  * returns a `double` representing the distance from the point to the origin
* `toString()`
  * returns a `String` representation of the point
  * Ex. (3, 6)
* `distanceFrom(Point otherPoint)`
  * returns a `double` representing the distance from this point to the given point
* `getX()`
  * returns the x coordinate
* `getY()`
  * returns the y coordinate
* `setLocation(int x, int y)`
  * changes the x and y coordinates to the given values

Your code should test all of the aforementioned functionality of the Point class.

## Getting Started

Let's talk about some of the terminology of object oriented programming:

We've been talking about objects this whole chapter, and now we can finally start to define them. **Objects** are entities that contain **data** and **behavior**. A `Scanner` is an example of an object. The data it holds is all in the cursor pointer. The `Scanner` remembers where it currently is in the file. In terms of behavior, the `Scanner` has several methods for consuming input token by token. 

The data is hidden from the client, but the methods are made available to use. We shouldn't have to worry about the cursor pointer; we can just trust that it works. However, we need to know how the methods work.

### Object Construction
```
Type objectName = new Type(parameters);
```

### Object Behavior
```
objectName.methodName(parameters);
```

A **client program** is a program that uses other objects. We have already been a client of `DrawingPanel`, `Scanner`, etc.

Like we talked about at the very beginning of this chapter, procedural programming refers to programs that perform behavior as a series of steps. **Object oriented programming** refers to programs that perform their behavior as interactions between objects. This definition is a little bit murky, but it takes a while to fully grasp it.

**Abstraction** refers to the concept that we can use objects without knowing how they work. We see many examples of this in our day-to-day lives. You understand the external behavior of your car and phone, but probably don't understand its inner mechanisms.

A **class** is a template for new type of objects. An object on the other hand is an instance of a class. The `DrawingPanel` class is a template for creating instances of `DrawingPanel` objects. The individual objects may be slightly different from each other (different height, width, background color) but they were all made from the same template. It's like a blueprint as opposed to the actual house.

When we implement `Point.java` ourselves, we'll get an opportunity to talk about more class-specific vocabulary.
