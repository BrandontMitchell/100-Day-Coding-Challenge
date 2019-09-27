# Day 010 - String Methods

The purpose of these next two days is to finalize your guessing game program, as well as introduce some of the included Java `String` methods that can be really useful. You will be building off of your solution from the previous day by adding functionality for users to play multiple games, as well as view statistics about the games that they've played.

Here's what the sample output looks like:

```
I'm thinking of a number between 1 and 100...
Next guess? 50
Nope. It's higher.
Next guess? 75
Nope. It's higher.
Next guess? 87
Nope. It's lower.
Next guess? 82
Nope. It's higher.
Next guess? 85
Nope. It's lower.
Next guess? 83
Nope. It's higher.
Next guess? 84
You guessed it in 7 tries!
Play again? (y/n) yes
Oops. Please type either 'y' or 'n'
Play again? (y/n) y

I'm thinking of a number between 1 and 100...
Next guess? 50
Nope. It's higher.
Next guess? 75
Nope. It's higher.
Next guess? 87
Nope. It's higher.
Next guess? 93
Nope. It's higher.
Next guess? 96
Nope. It's higher.
Next guess? 98
Nope. It's higher.
Next guess? 100
Nope. It's lower.
Next guess? 99
You guessed it in 8 tries!
Play again? (y/n) no
Oops. Please type either 'y' or 'n'
Play again? (y/n) nope
Oops. Please type either 'y' or 'n'
Play again? (y/n) n

Statistics:
Games       = 2
Guesses     = 15
Best Game   = 7
```

As you can see above, there are three statistics that you will need to keep track of: the total number of games played, the total number of guesses made, and the best game (the game that took the fewest number of guesses).

One of the new things that you'll have to do is continually prompt the user until they type in either 'y' or 'n' exactly. This will require combining a few different concepts, including while loops, relational operators, and String methods (the new concept for today). Since today's solution is a little bit challenging, we will provide two days to complete it.

## Starter Code

This day includes a single file in the starter-code folder titled `Starter.java`. This file is the same file as the `Solution.java` file from the previous day.

This will provide a great starting point for completing today's challenge, especially since the `game` method is already set up to return the number of guesses that the most recently played game took.

## Getting Started

Although not really the centerpiece of today's challenge, the new piece of material for today are the Java `String` methods. If you recall, `String` is the name of the data type in Java that holds text. Here's the syntax for declaring a String:

### Syntax
```
String name = "text";
```

### Example
```
String password = "computersRkool";
```

Once declared, you can use dot notation to access all of the provided `String` methods and get more information about that `String`. Here's an example of what that would look like:

### Syntax
```
String password = "this is a bad password";
int length = password.length();
```

In the previous example, the variable `length` will store the value 22. That's because the length method returns the number of characters in the `String`. This includes whitespace and special characters like `#`, `$`, `&`, etc.

Here's a list of some of the more commonly used `String` methods:

* `contains(str)`
  * returns true if this `String` contains the other's characters inside it
* `endsWith(str)`, `startsWith(str)`
  * returns true if this `String` starts/ends with the other's characters
* `equals(str)`
  * returns true if this `String` is the same as `str`
* `equalsIgnoreCase(str)`
  * returns true if this `String` is the same as `str`, ignoring capitalization
* `indexOf(str)`
  * returns the index in this `String` where given `String` begins (-1 if not found)
* `length()`
  * returns number of characters in this `String`
* `substring(i, j)`
  * returns the characters in this `String` from index `i` (inclusive) to `j` (exclusive)
* `toLowerCase()`, `toUpperCase()` 
  * returns a new `String` with all lowercase or uppercase letters
* `charAt(i)` 
  * returns the character at index `i` as a primitive `char`

Some things to keep in mind:

* Remember that `String` in Java use zero-based indexing. This means that the first character is in the 0th index.
* `String` methods are case-sensitive unless otherwise stated
* Remember that the `toLowerCase` and `toUpperCase` methods return a new version of the `String`. To change a `String` to either uppercase or lowercase, you must use an assignment statement.
  * Ex. `password = password.toLowerCase();`
  
Now we can talk about a useful programming trick that will help you with the assignment.

### Finding the Minimum Value

Consider the task of reading 5 integers typed in by the user, and then reporting the smallest number that was typed in. We would need a variable to keep track of the lowest number that we've seen so far. Each time they type something in, we can see if it's smaller, and then update it accordingly. But when we initialize the variable, what should it's value be? We could pick a really big number, but it's possible that everything the user types in is bigger than that number, and in that case we would incorrectly report the minimum number. Here's how we fix this problem:

```
Scanner console = new Scanner(System.in);
int min = Integer.MAX_VALUE;
for (int i = 1; i <= 5; i++) {
  int answer = console.nextInt();
  if (answer < min) {
    min = answer;
  }
}
System.out.println("The smallest number typed in was " + min);
```

Java provides a class constant for the biggest possible integer. This sounds strange, but it has to do with the way number representation works in computers. Everything is stored in a finite amount of space, so there's actually a limit to how high you can go. It's 2,147,483,647 if you were curious.

The code that makes this algorithm work is the if statement inside of the for loop. It checks each value that the user types in, and if what they typed in was smaller than the smallest number we had seen so far, we update our `min` variable to that new number. This algorithm is especially relevant to how you keep track of the best game.


