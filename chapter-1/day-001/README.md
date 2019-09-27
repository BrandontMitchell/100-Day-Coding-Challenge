# Day 001 - Introduction to Java

The purpose of this day is to introduce Java, as well as the concept of procedural programming. Java is one of the most widely used programming languages, but it is oftentimes not people's first language. The reason we chose to start with Java is similar to the reason that the introductory courses at the University of Washington use Java: it is a strict language and provides many opportunities to discuss different coding concepts.

For this challenge, you will be producing the lyrics to the classic Christmas song: "Twelve Days of Christmas." This day shouldn't be immensely challenging; it should more just be an introduction to Java syntax and text editors.

Here's what your program's output will look like:

```
On the first day of Christmas,
my true love sent to me
A partridge in a pear tree.

On the second day of Christmas,
my true love sent to me
Two turtle doves,
And a partridge in a pear tree.

On the third day of Christmas,
my true love sent to me
Three French hens,
Two turtle doves,
And a partridge in a pear tree.

On the fourth day of Christmas,
my true love sent to me
Four calling birds,
Three French hens,
Two turtle doves,
And a partridge in a pear tree.

On the fifth day of Christmas,
my true love sent to me
Five golden rings,
Four calling birds,
Three French hens,
Two turtle doves,
And a partridge in a pear tree.

On the sixth day of Christmas,
my true love sent to me
Six geese a-laying,
Five golden rings,
Four calling birds,
Three French hens,
Two turtle doves,
And a partridge in a pear tree.

On the seventh day of Christmas,
my true love sent to me
Seven swans a-swimming,
Six geese a-laying,
Five golden rings,
Four calling birds,
Three French hens,
Two turtle doves,
And a partridge in a pear tree.

On the eighth day of Christmas,
my true love sent to me
Eight maids a-milking,
Seven swans a-swimming,
Six geese a-laying,
Five golden rings,
Four calling birds,
Three French hens,
Two turtle doves,
And a partridge in a pear tree.

On the ninth day of Christmas,
my true love sent to me
Nine ladies dancing,
Eight maids a-milking,
Seven swans a-swimming,
Six geese a-laying,
Five golden rings,
Four calling birds,
Three French hens,
Two turtle doves,
And a partridge in a pear tree.

On the tenth day of Christmas,
my true love sent to me
Ten lords a-leaping,
Nine ladies dancing,
Eight maids a-milking,
Seven swans a-swimming,
Six geese a-laying,
Five golden rings,
Four calling birds,
Three French hens,
Two turtle doves,
And a partridge in a pear tree.

On the eleventh day of Christmas,
my true love sent to me
Eleven pipers piping,
Ten lords a-leaping,
Nine ladies dancing,
Eight maids a-milking,
Seven swans a-swimming,
Six geese a-laying,
Five golden rings,
Four calling birds,
Three French hens,
Two turtle doves,
And a partridge in a pear tree.

On the twelfth day of Christmas,
my true love sent to me
Twelve drummers drumming,
Eleven pipers piping,
Ten lords a-leaping,
Nine ladies dancing,
Eight maids a-milking,
Seven swans a-swimming,
Six geese a-laying,
Five golden rings,
Four calling birds,
Three French hens,
Two turtle doves,
And a partridge in a pear tree.
```

## Starter Code

This day includes a single file in the starter-code folder titled `Starter.java`. This includes the
**boilerplate** structure of an Java program. Boilerplate refers to code that you write over and over again.

All of the code that you write will go inside of what is called the main method. It looks like this:

```
public static void main(String[] args) {
  // your code goes here...
}
```

You can think of this as where the computer starts reading to find out what it has to do when you run the program.
  
## Getting Started

Before going more in-depth into Java syntax, the first thing you'll need to do is download an **integrated development environment** (IDE) to write your Java code in. An IDE is to programs as Microsoft Word is to essays. It's the program that we'll be writing and running our code in. There are many different types of IDEs, and people have their own preference about which one they like to use. Our recommendation is jGRASP, because it gets the job done without overwhelming you with extra features that you won't be using.
  
You will need to download and install two pieces of software: the Java compiler (known as the JDK) and jGRASP. Some users already have the JDK installed on their computers, because of other software that they use that is written in Java. If you think this applies to you, you can safely skip the JDK installation, although you may find that you need to come back and complete it anyway.

1. [Installing JDK](https://courses.cs.washington.edu/courses/cse14x/software/jdk.html)

2. [Installing jGRASP](https://courses.cs.washington.edu/courses/cse14x/software/jgrasp.html)

In order to complete the challenge (and all future challenges):

1. Create a new folder somewhere on your computer to hold the starter code.

2. Download all of the files located in the starter-code folder into the folder you just created.

3. Open jGRASP, and then click File, Open, and open all of the files in the starter-code folder.

There are two main interaction panes in jGRASP: the **workspace**, and the **console**. The workspace is where you will see the contents of the file that you are editing. This is where you will be writing your code. The console is the smaller white box towards the bottom of the screen that is initially empty but will display any output generated by your program.

## Procedural Programming

Before we get started with this first chapter, it's useful to talk about what the idea of procedural programming is. The word **program**, can really be thought of as a set of instructions to be carried out by the computer. Running your program is the act of carrying out the instructions contained in a program. **Procedural programming** is the idea that we will write our program like a table of contents, read from top to bottom, and all of the necessary code will stay within a single file.

A **programming language** is a systematic set of rules used to describe different instructions in a format that is editable and readable by humans. We will be studying a programming language called Java for this first chapter.

Things to keep in mind if it's your first time programming:

1. Computers are stupid.

2. Computers can't read minds.

3. Computers don't make mistakes.

4. If the computer is not doing what you want, it's because ***you*** made a mistake

## Java Overview

Java is referred to as what is called a compiled language. While it's not necessary to go into the implications of this, the relevant part to us is that before your program can run, some other software will proof-read the code that you've writting for any syntax errors. You must fix all of them before the IDE will allow you to run your program. This may seem cumbersome, but it actually ends up saving you a lot of time in locating bugs, or problems, with your code.

As mentioned before, all of the code that you write will be located inside of the main method. Here's what that looks like:

### Syntax

```
public class Hello {
  public static void main(String[] args) {
    System.out.println("Hello, world!");
  }
}
```

This is an example of a complete Java program that will produce the output `Hello, world!`. Java is intimidating because there is a lot of boilerplate code that you have to write before you can get started. For now, you can ignore the semantics of what it all means, and by the end of this chapter, hopefully you'll have a pretty good idea.

For now, you can think of `public class` as "My program will be called...".  

When you want to run your program, you click the red running man icon above the workspace. Note that the first time that you try to run your program, you may be prompted to save the file beforehand. You can name your program whatever you want but there are a few important details to keep in mind. The name of your program must exactly match the name of the file that is saved in. For example, the program above must be saved in a file called `Hello.java` or it will not work.

Now might be a good time to talk about some Java vocabulary. 

**Statements** in Java are one line commands that specify something that the computer should do. For example, the program above contains one statement: `System.out.println("Hello, world!");`. This is the way that whoever made Java decided you would produce output to the console. Statements must end with semicolons. 

The **main method** that we've been talking about is a special type of method, because it contains the code that gets executed when our program is run. **Methods** in Java are just named groups of statements. Later we'll see that we can introduce methods other than the main method.

**Keywords** in Java are something that are easier to notice within your IDE. In jGRASP, they are the words that show up as purple. Certain words are referred to as reserved keywords in Java, meaning that they have special designated meaning within the programming language and cannot be used for anything else. Words like `public`, `class`, `static`, `void`, etc. are reserved, and cannot be used for the name of your program or anyting else.

Java is case-sensitive, and so while you can use things like `CLAss` or `claSS` as your program name, it is very confusing and strongly discouraged. This also means that when writing statements you must be precise in your captilization, or the **compiler** will tell you that you made a mistake. The compiler is the software that proofreads your code and tells you what mistakes you made. For example, `system.out.println();` will not be recognized as a Java command because the 's' is supposed to capitalized.

## System.out.println()

This is the only command you will need to know to complete the first two challenges. There are two ways to use this command:

### Syntax

```
System.out.println("text");
```
This will print the given message as output.

```
System.out.println();
```
This will print a blank line of output.

One thing to be aware of is that when producing non-blank output, you must surround your text with quotation marks. This becomes problematic when you want quotation marks to appear in your output.

### Incorrect Example
```
System.out.println(""Hello, world!"");
```

While this may seem like the correct way to produce the output `"Hello, world!"`, it will actually give you a compiler error. You must use what are called **escape sequences** to produce quotation marks in your output. Escape sequences are when you put a backslash before a character with special meaning to indicate to Java that you actually want that character to appear in your output.

### Correct Example
```
System.out.println("\"Hello, world!\"");
```

This leads to an annoying chain reaction where you must now use two backslashes if you want a backslash to appear in your output. For a full list of characters that require escape sequences, you can refer [here](https://docs.oracle.com/javase/tutorial/java/data/characters.html). However, this shouldn't be a problem for the first today's challenge.

## Static Methods

Methods, or static methods, will allow us to do two main things: provide structure to our code, and eliminate redundancy. In one analogy, you can think of our main method like a table of contents, and static methods like chapters in our program. Static methods are named, which helps with the overall readability of our program.

### Syntax

```
public static void name() {
  statement;
  ...
}
```

Once I've introduced this method, I can invoke all of the statements contained within it anywhere in my program (including the main method) by simply writing:
`name();` as a statement.

Here's an example:

### Program with redundancy
```
public class BakeCookies {
  public static void main(String[] args) {
    System.out.println("Mix the dry ingredients.");
    System.out.println("Cream the butter and sugar.");
    System.out.println("Beat in the eggs.");
    System.out.println("Stir in the dry ingredients.");
    System.out.println("Set the oven temperature.");
    System.out.println("Set the timer for 10 minutes.");
    System.out.println("Place a batch of cookies into the oven.");
    System.out.println("Allow the cookies to bake.");
    System.out.println("Set the oven temperature.");
    System.out.println("Set the timer for 10 minutes.");
    System.out.println("Place a batch of cookies into the oven.");
    System.out.println("Allow the cookies to bake.");
    System.out.println("Mix ingredients for frosting.");
    System.out.println("Spread frosting and sprinkles.");
  }
}
```

There are two things bad about this program: it is **redundant**, and difficult to read. By redundant, we mean that two or more identical and consecutive lines of code are repeated in different places in the program. Introducing static methods can solve both of these problems.

### Fixed program

```
public class BakeCookies3 {
  public static void main(String[] args) {
    makeBatter();
    bake(); // 1st batch
    bake(); // 2nd batch
    decorate();
  }
  
  // Step 1: Make the cake batter.
  public static void makeBatter() {
    System.out.println("Mix the dry ingredients.");
    System.out.println("Cream the butter and sugar.");
    System.out.println("Beat in the eggs.");
    System.out.println("Stir in the dry ingredients.");
  }
  
  // Step 2: Bake a batch of cookies.
  public static void bake() {
    System.out.println("Set the oven temperature.");
    System.out.println("Set the timer for 10 minutes.");
    System.out.println("Place a batch of cookies into the oven.");
    System.out.println("Allow the cookies to bake.");
  }
  
  // Step 3: Decorate the cookies.
  public static void decorate() {
    System.out.println("Mix ingredients for frosting.");
    System.out.println("Spread frosting and sprinkles.");
  }
}
```

Try to introduce methods when writing your solution to day 1. It will help with the readability of your program. In day 2, we'll worry about redundancy.
