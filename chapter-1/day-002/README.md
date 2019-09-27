# Day 002 - Eliminating Redundancy

The purpose of this day is to discuss the difference between **internal correctness** and **external correctness**. Although the solution provided for the previous day's challenge is externally correct (it produces the correct output), it leaves a lot of room for improvement. The major problem with the code is that it is very redundant. 

There are other things other than just eliminating redundancy that make up the internal correctness of your code. For example, commenting your code is an important practice for working in industry, because it allows others to more easily understand code that you've written.

For this challenge, you will be introducing more static methods to eliminate the redundancy in the existing solution. The way you will know that you have successfully completed this task is if no two consecutive and identical `System.out.println("text");` statements appear in multiple places in your code. We will provide examples of this further down for clarification.

## Starter Code

This day includes a single file in the starter-code folder titled `Starter.java`. This is the same file as `Solution.java` from the previous day.

It's encouraged that you either start working with this file, or modify your existing solution to resemble this `Starter.java` file. This will give you a good foundational start for completing today's challenge.

## Redundancy

If you recall, our current working definition of redundancy is two or more identical and consecutive lines of code that appear in more than one place in your program. There is an important distinction to make here:

```
System.out.println("On the first day of Christmas,");
System.out.println("my true love sent to me");

...

System.out.println("On the second day of Christmas,");
System.out.println("my true love sent to me");
```

This code is **not** redundant, because the two lines of code are not entirely identical. We haven't learned the tools to eliminate this type of redundancy quite yet. However, the example below would be considered redudnant:

```
System.out.println("Two turtle doves,");
System.out.println("And a partridge in a pear tree.");

...

System.out.println("Two turtle doves,");
System.out.println("And a partridge in a pear tree.");
```

This is because the two lines of code are identical.

## Naming Conventions

Another important practice in Java is to follow the naming conventions. In general, method names in Java follow the **camel casing** naming convention. This looks like this:

### Syntax

```
public static void theFirstWordIsLowercaseAndEverythingAfterIsUppercase() {

}
```

Although it's not the best method name, it hopefully illustrates the convention. Program names on the other hand in Java follow a slightly different naming convention, in which each word is capitalized.

### Syntax

```
public class ThisIsMyProgramName {

}
```

There are other practices that are more common sense, like giving appropriate and descriptive names to your programs and methods, and not writing everything on the same line. All of the sample solutions are good examples to look at to model your code after.
