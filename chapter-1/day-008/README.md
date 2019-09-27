# Day 008 - Conditional Execution

The purpose of this day is to introduce another important programming concept: the **if statement**. The if statement is used to execute a block of statements only if a test is true.

For this challenge, you will be building off of your solution from the previous day to create a budgeting program. It will calculate your montly deposits and withdrawals and give you a spending report. Here's a sample log of execution:

```
Please enter your deposits and withdrawals
to calculate your net monthly income.

How many deposits? 3
    Next deposit amount? $123.24
    Next deposit amount? $100.30
    Next deposit amount? $23.78

How many withdrawals? 4
    Next withdrawal amount? $53.75
    Next withdrawal amount? $24.99
    Next withdrawal amount? $12.34
    Next withdrawal amount? $16.46

Total deposits    = $247.32
Total withdrawals = $107.54

You deposited $139.78 more than you withdrew this month.
You deposited a decent amount of money this month.
```

Several parts of the code depend on user input, most of which are tied to the calculations and user input. The last two lines of code should accurately reflect the results of the calcuations.

The second to last line will either print:
```
You deposited $X more than you withdrew this month.
```
OR
```
You withdrew $X more than you deposited this month.
```

The very last line depends on the magnitude of the difference between their deposits and withdrawals.

If they withdrew at least $500 more than they deposited you should print:
```
You withdrew a lot of money this month!");
```
Otherwise, if they withdrew more than they deposited you should print:
```
You withdrew a decent amount of money this month.");
```
Otherwise, if they deposited less than $500 more than they withdrew you should print:
```
You deposited a decent amount of money this month.");
```
Otherwise, if they deposited more than 500 than they withdrew you should print:
```
You deposited a lot of money this month!");
```

## Starter Code

This day includes a single file in the starter-code folder titled `Starter.java`. This file is the same as the solution from the previous day. It gives a great starting point for the code that you will have to write today.
  
## Getting Started

There are two new concepts today: **conditional execution** and **boolean** expressions. We've already seen examples of boolean expressions, so  let's first take a look at the syntax for conditional execution.

### Syntax
```
if (test) {
  statement(s);
} else {
  statement(s);
}
```

### Example
```
Scanner console = new Scanner(System.in);
double gpa = console.nextDouble();
if (gpa >= 3.0) {
  System.out.println("Good job! Here's a cookie.");
} else {
  System.out.println("No cookie for you!");
}
```

The if statement is one of the more intuitive coding concepts to understand. If the test is true, then the statements in the if branch will be executed, otherwise the statements in the else branch will be executed. Let's take a closer look at the **relational operators** that make up boolean expressions.

### Relational Operators

| Operator  | Meaning                   | Example     | Value |
| --------- | ------------------------- | ----------- | ----- |
| ==        | equals                    | 1 + 1 == 2  | true  |
| ==        | does not equal            | 3.2 != 2.5  | true  |
| <         | less than                 | 10 < 5      | false |
| >         | greater than              | 10 > 5      | true  |
| <=        | less than or equal to     | 126 <= 100  | false |
| >=        | greater than or equal to  | 5.0 >= 5.0  | true  |

These are also relatively intuitive to understand. We've seen these appear already in our for loop test conditions. There are a few variations on the conditional structure that you can use.

## Conditional Structures

### Exactly 1 Path
```
if (test) {
  statement(s);
} else if (test) {
  statement(s);
} else {
  statement(s);
}
```

### 0 or 1 Path
```
if (test) {
  statement(s);
} else if (test) {
  statement(s);
} else if (test) {
  statement(s);
}
```

### 0, 1, or Many Paths
```
if (test) {
  statement(s);
} 
if (test) {
  statement(s);
} 
if (test) {
  statement(s);
}
```

One if the trickiest parts about using if statements is figuring out which of the conditional structures you should use. As a general tip, there is a correct structure for every task.


