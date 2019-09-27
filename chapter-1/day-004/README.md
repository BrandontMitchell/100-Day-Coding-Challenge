# Day 004 - Class Constants

The purpose of this day is to introduce one new concept, while making our solution from day 3 way cooler. 

For this challenge, you will be modifying your solution from the previous day to make it scalable. By changing a single number in our program, we'll be able to see our ASCII art shrink and grow proportionally.

## Starter Code

This day includes a single file in the starter-code folder titled `Starter.java`. This is the same file as `Solution.java` from the previous day. It's highly encouraged that you work off of this solution, or modify your existing solution to resemble this file. This will be a good sanity check in terms of completing today's challenge. A **Sanity check** in programming refers to eliminating sources of error. If there was something wrong with your solution from the previous day, you want to fix that before building on it.
  
## Getting Started

The way we'll be scaling our ASCII art is through the use of a **class constant**. Class constants in Java are special types of variables that can be used throughout our program and usually represent some special value. They are especially useful for two reasons: readability, and portability.
 
You probably noticed that the value 6 appeared several times throughout the solution to the previous day. That's because that number represents the size of our ASCII art drawing. For someone reading our program, it would be helpful to know this, instead of seeing the number 6 everywhere.

### Syntax

```
public class MyProgram {
  
  public static final int SIZE = 6;
  
  public static void main(String[] args) {
  
  }
  
}
```

The program above has a single class constant that holds the value 6. The keyword `final` indicates that the variable `SIZE` will always hold the value it was initially assigned. For the entire lifetime of the program, (from run to finish) we will be able to use `SIZE` as an alias for the number 6.

### Example
```
public class MyProgram {
  
  public static final int SIZE = 6;
  
  public static void main(String[] args) {
    for (int i = 1; i <= SIZE; i++) {
      System.out.print("%");
    }
    for (int i = 1; i <= 6; i++) {
      System.out.print("%");
    }
  }
  
}
```

In the example above, the two for loops will behave identical to one another. Now that we know how to introduce a class constant to our program, it's time to actually incorporate it into our code. First, we'll need to look at a few different scaled versions of the original ASCII art.

### SIZE = 4

```
                 /====
                ///====
               /////====
              ///////====
             ////#////====
            ////###////====
           ////#####////====
          ////###### ////====
         ////######   ////====
        ////######     ////====
       ////######       ////====
      ////######         ////====
     ////######           ////====
    ////######=====================
   ////######=======================
  ////######=========================
 ////################################
  //################################
```

### SIZE = 6 (DEFAULT)

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

### SIZE = 12

```
                         /============
                        ///============
                       /////============
                      ///////============
                     /////////============
                    ///////////============
                   /////////////============
                  ///////////////============
                 /////////////////============
                ///////////////////============
               /////////////////////============
              ///////////////////////============
             ////////////#////////////============
            ////////////###////////////============
           ////////////#####////////////============
          ////////////###### ////////////============
         ////////////######   ////////////============
        ////////////######     ////////////============
       ////////////######       ////////////============
      ////////////######         ////////////============
     ////////////######           ////////////============
    ////////////######=====================================
   ////////////######=======================================
  ////////////######=========================================
 ////////////################################################
  //////////################################################
   ////////################################################
    //////################################################
     ////################################################
      //################################################
```

Our job is to figure out how the expressions must change according to the `SIZE`, if at all. In other words, you can say that our original expressions made the assumption that the `SIZE` was 6, and so we need to generalize the expressions to work for all values of `SIZE`. The easiest way to do this is to compare how the expressions change between different values of `SIZE`. 

For example, let's look at the number of spaces in section 1:

### SIZE = 4

| i (line number)  | number of characters  | -1 * i  | -1 * i + 18 |
| ---------------- | --------------------- | ------- | ----------- |
| 1                | 17                    | -1      | 17          |
| 2                | 16                    | -2      | 16          |
| 3                | 15                    | -3      | 15          |

### SIZE = 6

| i (line number)  | number of characters  | -1 * i  | -1 * i + 20 |
| ---------------- | --------------------- | ------- | ----------- |
| 1                | 19                    | -1      | 19          |
| 2                | 18                    | -2      | 18          |
| 3                | 17                    | -3      | 17          |

### SIZE = 12

| i (line number)  | number of characters  | -1 * i  | -1 * i + 26 |
| ---------------- | --------------------- | ------- | ----------- |
| 1                | 25                    | -1      | 25          |
| 2                | 24                    | -2      | 24          |
| 3                | 23                    | -3      | 23          |

The only thing that changed between the three expressions in the fourth column is the constant; it changed from 18 to 20 to 26. In case the relationship isn't clear yet, let's make a table that compares the relationship between the `SIZE` and the constant in the expression.

| SIZE   | shift  | SIZE + 14  |
| ------ | ------ | ---------- |
| 4      | 18     | 18         |
| 6      | 20     | 20         |
| 12     | 26     | 26         |

We've found the generalized expression, so now we can replace our old one, and now continue the process for the rest of expressions. Note that some of the expressions may not have to change at all. 
