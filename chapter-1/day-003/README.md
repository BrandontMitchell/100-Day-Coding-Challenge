# Day 003 - For Loops

The purpose of this day is to introduce one of the most fundamental control structures in Java and in many other languages: the **for loop**. A **control structure** is a programming construct that somehow affects the flow of a program's execution. We will learn other control structures in this chapter, but the for loop is probably the easiest to understand.

For this challenge, you will be recreating the [ASCII art](https://en.wikipedia.org/wiki/ASCII_art) shown below:

```
                   /======
                  ///======
                 /////======
                ///////======
               /////////======
              ///////////======
             //////#//////======
            //////###//////======
           //////#####//////======
          //////###### //////======
         //////######   //////======
        //////######     //////======
       //////######       //////======
      //////######         //////======
     //////######           //////======
    //////######=========================
   //////######===========================
  //////######=============================
 //////####################################
  ////####################################
   //####################################
```

This will be accomplished using a combination of for loops and the `System.out.println()` command that you already learned.

## Starter Code

This day includes a single file in the starter-code folder titled `Starter.java`. The code has been intentionally broken up into five methods, for reasons that will be explained later. Following this suggested structure will greatly simplify your task.
  
## Getting Started

Before explaining a development strategy for how to actually tackle this problem, let's first talk about the syntax of how to write a for loop.

### Syntax

```
for (initialization; test; update) {
  statement;
  ...
  statement;
}
```

### Example

```
for (int i = 1; i <= 4; i++) {
  System.out.println("I am so smart");
}
```

The for loop in this example will print out `I am so smart` 4 times. The initialization step will happen once, and then the following will be repeated:

1. Check if the test is true
2. Execute the statements inside the for loop
3. Perform the update
4. Go back to step 1

Let's go into more detail on what the different parts of a for loop actually are.

## Initialization

The purpose of the **initialization** step is to create a **variable** that Java can use to keep track of how many times we've executed the body of the for loop. This variable is oftentimes referred to as a **loop counter**. It can use any name, although `i` is used by convention. It can start at any value, but can only be used inside of the curly braces of the for loop. 

We'll revisit the idea of variables later in this chapter. For now, the most important part to remember about this step is that it only happens once as the loop begins.

## Test

The **test** of the for loop compares the loop counter against some limit. It uses Java **comparison operators**, which are as follows:

* `<`
  * less than
* `<=`
  * less than or equal to
* `>`
  * greater than
* `>=`
  * greater than or equal to
  
## Update

The **update** of the for loop is a simple expression that updates the loop counter variable to a new value. Most commonly it will be `i++` which means to increment the value of `i` by 1. However, the update can be whatever statement you want it to be.
  
If the initialization step is `int i = 1;`, the test is `<=`, and the update is `i++` then the number on the righthand side of the comparison operator is how many times the for loop will run, like in the very first example. In our case, instead of using just a number, we will be writing simple expressions to generate cool patterns.

## The Nested Loop Pattern

A **nested loop** looks pretty scary, but it's really just a for loop within another for loop. It's what we'll be using to generate the ASCII art pattern.

As mentioned before, the starter code is intentionally broken up into five sections to make the task simpler. Here's a helpful diagram of what the five sections are:

### Section 1
```
                   /======
                  ///======
                 /////======
                ///////======
               /////////======
              ///////////======
```
### Section 2
```
             //////#//////======
            //////###//////======
           //////#####//////======
```
### Section 3
```
          //////###### //////======
         //////######   //////======
        //////######     //////======
       //////######       //////======
      //////######         //////======
     //////######           //////======
```
### Section 4
```
    //////######=========================
   //////######===========================
  //////######=============================
```
### Section 5
```
 //////####################################
  ////####################################
   //####################################
```

The reason overall picture was broken up into these sections is because the number of characters that appear on each line follow a distinct pattern when you look at the picture in these smaller chunks. More specifically, it allows us to create a linear relationship between the current line number and the number of each character that appear on that line. 

This will be clearer with an example, so let's first walk through a **pseudocode** example of what the nested loop structure looks like, and then apply it to the first section to get you started. Pseudocode is a hybrid between English and Java code that is used in the drafting process. Here it is below:

```
for (int i = 1; i <= (# of lines in the pattern); i++) {
  for (int i = 1; i < expression; i++) {
    System.out.print("(a single character)");
  }
  
  ...
  
  for (int i = 1; i < expression; i++) {
    System.out.print("(a single character)");
  }
  System.out.println();
}
```

Notice that we have introduced a new command: `System.out.print()`. This command is exactly the same as `System.out.println()` except it does not complete the line of output. This means that the next thing we print will appear on the same line. The outer for loop runs six times, and we have a single `System.out.println()` statement inside the outer for loop, so that's how we know 6 lines of output will be produced. The inner for loops take care of producing the horizontal output of characters, and the `System.out.println()` at the end is like pressing enter to go to the next line.

The parts that we have to figure out are the number of lines that appear in the section, what to place inside of the calls to `System.out.print()`, and what the expressions will end up being.

The first part is easiest; you can just count the number of lines of output in the section, and fill in the outer for loop accordingly. Section 1 in this case has 6 lines of output. Next, we want to introduce one nested for loop for each distinct character that appears in the section. For section 1, there are three distinct characters: ` `, `/`, and `=` and so we will have two inner for loops. Here's what the structure looks like right now:

```
for (int i = 1; i <= 6; i++) {
  for (int i = 1; i < expression; i++) {
    System.out.print(" ");
  }
  for (int i = 1; i < expression; i++) {
    System.out.print("/");
  }
  for (int i = 1; i < expression; i++) {
    System.out.print("=");
  }
  System.out.println();
}
```

Notice that the order that the characters appear horizontally should be reflected in the order that the for loops appear in the nested structure. Also, spaces must be considered characters when forming your structure. Since the spaces come first (are on the left) in the drawing, that for loop is at the top. The next thing we need to do is figure out what the expressions are. The easiest way to go about doing that is by creating small tables like the one below:

| i (line number)  | number of characters | 2 * i | 2 * i - 1 |
| ---------------- | -------------------- | ------| --------- |
| 1                | 1                    | 2     | 1         |
| 2                | 3                    | 4     | 3         |
| 3                | 5                    | 6     | 5         |

This table was created for the forward slashes in section 1. The first two columns can be completed by observing the pattern, if you designate the first line of output as line 1. The third column is a preliminary expression that we generated by observing the difference between the number of characters that appear on each line. Since the second column is increasing by 2 each time the line number increases by 1, we write the expression `2 * i` to reflect this. However, this doesn't exactly give us what we want, and so we have to come up with a constant to either add or subtract from our expression to shift the values accordingly. In this case, the numbers we were getting (2, 4, 6) were consistently one too high, and so we subtract 1 to shift our expression over.

If you're a fan of math, then this was really just slope-intercept form, but otherwise you can follow this strategy and it will always work. The expression in the rightmost column is what we were looking for, and so we can update the nested loop structure accordingly.

```
for (int i = 1; i <= 6; i++) {
  for (int i = 1; i < expression; i++) {
    System.out.print("/");
  }
  for (int i = 1; i < 2 * i - 1; i++) {
    System.out.print("/");
  }
  for (int i = 1; i < expression; i++) {
    System.out.print("=");
  }
  System.out.println();
}
```

The process above can be repeated for all of the inner for loops. Some final tips:

1. Each call to `System.out.print()` should only print a single character.

2. All of the expressions are linear, so you won't have to do any complicated calculations

