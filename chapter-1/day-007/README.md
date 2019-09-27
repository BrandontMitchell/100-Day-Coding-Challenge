# Day 007 - Interactive Programs

The purpose of this day is to learn one of the ways we can add **user interaction** to our programs. This brings a lot of concepts along with it, because we now need a way to stop execution of our program to wait for the user to type something in, save what they type in, and then react accordingly in our program.

For this challenge, you will be writing a simple calculator program. It first asks how many numbers you would like to add together, and then proceeds to add them up and report what the total was. The program should be able to accept both whole and decimal numbers. Here's a sample log of execution:

```
How many numbers? 5
    Next number? 12.3
    Next number? 4
    Next number? 7
    Next number? 23.75
    Next number? 45

Total     = 92.05
```

A **sample log of execution** is an example of what you would expect to see in your console when you run the program. Note that this should not always be the output; it should be dependent on the numbers that the user types in.

## Starter Code

This day includes a single file in the starter-code folder titled `Starter.java`. This includes some structure to your program that will help guide you to writing good code. There are two functions that you will need to complete: `getTotal` and `intro`. The `intro` method should not be any different from anything that we've done so far, but the `getTotal` method will use a lot of new concepts.

Asides from completing these two methods, you will also have to add some code to your main method that reports the total at the end.
  
## Getting Started

Let's start by revisiting the concept of **variables**, since although we've seen them before, we haven't really gotten a chance to work with them directly. We'll first talk about how to make a new variable.

### Syntax
```
type name;
```

### Example
```
int zipcode;
double myGPA;
```

This is called **variable declaration**. It sets aside memory for storing value of a specific type. Variables must be declared before they can be used. The reason we have to specifiy the type is because everything will eventually be represented by 0's and 1's behind the scenes by the computer. Java needs a way to distinguish between the different types of data that we can store (text, integers, real numbers, etc.).

There are two variable types in Java for storing numbers: **int** and **double**. The prior stores whole numbers, while the latter stores real numbers.

Since Java allows us to distinguish between integers and real numbers, try to use the appropriate data type for the thing that you're trying to represent. For example, a person's age would probably be represented by an `int`. Your GPA on the other hand should be represented by a `double` since it is not always a whole number.

Next, we can talk about **variable assignment**.

### Syntax
```
name = expression;
```

### Example 
```
int zipcode;
zipcode = 90210;
double myGPA;
myGPA = 1.0 + 2.25;
```

This process stores a value into a variable. The value can also be an expression; in this case Java will first figure out what the value of the expression is, and then store the result into the variable. **Expressions** are just an operation or series of operations that computes a value. In the example above, zipcode will store the value 90210 and myGPA will store the value 3.25.

Once given a value, a variable can later be used in expressions.

### Example

```
int x;
x = 3;
System.out.println(x + " here");     // x is 3 here
x = 4 + 7;
System.out.println("now x is " + x); // now x is 11
```

The example above also demonstrates how to include variables inside of calls to `System.out.println()`. Java requires that you perform what is called **String concatenation**. **Strings** are the Java name for variables that store text. Here are some examples:

### String Concatenation
```
"hello" + 42   // "hello42"
1 + "abc" + 2  // "1abc2"
"abc" + 1 + 2  // "abc12"
1 + 2 + "abc"  // "3abc"
"1" + 1        // "11"
4 - 1 + "abc"  // "3abc"
```

### Example
```
System.out.println(3 * 4);   // prints 12
System.out.println("3 * 4"); // prints 3 * 4
```

It involves using `+` between a `String` and another value to make a longer `String`. Make sure that you look at each of these examples carefully, and make sure you understand why the expression evaluates to what it does. Notice that Java evaluates expressions from left to right. 

On top of addition, Java has all of the normal arithmetic operators including a few extra that you can use with variables.

### Arithmetic Operators

* `+`
  * addition
* `-` 
  * subtraction
* `*` 
  * multiplication
* `/`
  * division
* `%` 
  * modulus (a.k.a. remainder)
  
The only two that work different than you may expect are division and modulus. When we divide integers, the quotient is also an integer.

### Integer Division

```
32 / 5 is 6
84 / 10 is 8
156 / 100 is 1
```

The `%` operator computes the remainder from integer division.

### Modulo

```
14 % 4 is 2
218 % 5 is 3
```

Since there are multiple arithmetic operators, Java uses precedence to figure out which operators are evaluated first. Java uses normal the normal order of operations. 

1. In general, operators evaluate from left to right.

2. Operations inside of parantheses have the highest level of precedence.

2. Multiplication, division, and modulo have the next highest precedence.

3. Addition and subtraction have the lowest level of precedence.

Operations between variables of different types also have their own level of precedence. Here's a helpful chart:

```
String > double > int
```

What this is saying is that operations between a `String` and a `double` or `int` will result in a `String` as the result. This coincides with the String concatenation examples that we saw earlier. The other important thing to note is that operations between a `double` and `int` will produce a `double` as the result. This also implies that a `double` can store `int` values, but not vice-versa. The reason it's called `double` is because it takes twice the amount of space to store all of the real numbers, and so an `int` doesn't reserve enough space for us to store a real number.

One last thing about variables is that the declaration and initialization steps can happen in the same line. This is common practice and often preferred over the previous way since it saves space.

### Syntax
```
type name = expression;
```

### Example
```
int x = (11 % 3) + 12; // x stores 14
double myGPA = 3.95;   // myGPA stores 3.95
```

There's a few more things we have to talk about: the **cumulative sum algorithm**, **returns**, and how to take in user input.

### Cumulative Sum Algorithm

Let's jump right in to the algorithm:

```
int sum = 0;
for (int i = 1; i <= 1000; i++) {
  sum = sum + i;
}
System.out.println("The sum of all integers from 1 to 1000 is " + sum);
```
One weird thing about this code is the line `sum = sum + i`. In order to understand this, remember that this is an assignment statement. In assignment, Java evaulates the righthand side of the equals sign first, and then stores the result of the expression into the variable on the lefthand side. In this case, what is being stored into the sum variable is the old value of sum added to the current value of i.

The **cumulative sum** is a variable that keeps a sum in progress and is updated repeatedly until summing is finished. The `sum` variable in the above code represents a cumulative sum. This variable must be declared outside the loops that update them, so that they still exist after the loop. This is related to the concept of scoping that we talked about on day 5. The fact that the sum variable exists outside of the loop sets us up nicely to incorporate a return value. We'll first talk about the syntax of return statements.

### Syntax
```
type name = name(expression);
```

### Example
```
double result = Math.max(1, 5);
```

In the example above, `result` will store the value of 5. `Math.max()` is a useful Java function included in the Java libraries that returns the larger of the two values passed in. Returning refers to the process of sending a value out of a method. You can think of it as the opposite of a parameter. The method call `Math.max(1, 5)` becomes an expression that evaluates to 5. That's how we're able to assign it to a variable. Let's revisit our cumulative sum algorithm, but this time return the `sum` variable.

### Cumulative Sum Algorithm with Return
```
public static void main(String[] args) {
    int sum = getSum();
    System.out.println("The sum of all integers from 1 to 1000 is " + sum);
}
public static int getSum() {
    int sum = 0;
    for (int i = 1; i <= 1000; i++) {
      sum = sum + i;
    }
    return sum;
}

```

Notice how the method header of the `getSum` method is no longer `void`; it has changed to match the variable type of the returned value. The reason we were writing `void` on all of our previous methods is because they didn't have any return value.

The last thing you'll need to know is how to take user input. We'll be using a built in Java class called the `Scanner`. Here's an example of how it works:

### Example
```
Scanner console = new Scanner(System.in);
System.out.print("What is your name? ");
String answer = console.next();
System.out.println("Hello " + answer + "!");
```

### Sample Output
```
What is your name? Fadel
Hello Fadel!
```

Almost all of your use of the `Scanner` object will look exactly like this example. However, there are some important things to mention. The declaration of the `Scanner` variable is something that's not necessary to understand at this point. That's how we connect a `Scanner` to user input, and it is called console because that's where the user will be typing their input.

The prompting step that happens on line 2 is a `System.out.print()` statement and not a `System.out.println()` call purely for formatting purposes. That way, the user input will appear on the same line as the question. On the next line, when we call `console.next()` the program will pause execution and wait to continue until the user types something in. `console.next()` is a method with a return value, and so we store it's result into a variable called `answer` so that we can use it later. Then later in our code we use the value of `answer` to do something.

The `Scanner` has a method for each type of data that it can read in. It is necessary to use the appropriate method, but they all have pretty much the same behavior.

### Scanner Methods
* `nextInt()` 
    * reads an `int` from the user and returns it
* `nextDouble()` 
    * reads a `double` from the user
* `next()` 
    * reads a one-word `String` from the user
* `nextLine()` 
    * reads a one-line `String` from the user
    
Feel free to refer back to this page if you get stuck, but now you have all the information you need to complete today's challenge. Good luck!






