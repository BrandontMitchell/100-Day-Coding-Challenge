# Day 009 - While Loops

The purpose of this day is to introduce yet another control structure in Java: the **while loop**. We will be doing this by creating a classic programming game: the number guessing game.

Here's a sample output log of what your program should produce when you're finished:
```
I'm thinking of a number between 1 and 100...
Next guess? 50
Nope. It's lower.
Next guess? 25
Nope. It's lower.
Next guess? 12
Nope. It's lower.
Next guess? 6
Nope. It's lower.
Next guess? 3
Nope. It's higher.
Next guess? 5
It took you 6 guess(es)
```

To make the game more interesting, we'll also be introducing random number generation. That way the correct answer changes with each execution of the program.

## Starter Code

The starter-code folder for this week includes a single file called `Starter.java`. This outlines a good structure that you are encouraged to follow. Your job is implement the `game` method. This method is in charge of producing all of the output associated with a single game. It should also return the number of guesses that the user took to correctly guess the number.
  
## Getting Started

There are two new concepts for today's challenge: **pseudorandom** number generation, and while loops. Let's first talk about random number generation, since it's relatively straightforward to use. To get a number in an inclusive range:

### Syntax
```
Random name = new Random();
name.nextInt(range) + min   // range = (max - min + 1)
```

### Example
```
Random randy = new Random();
int n = randy.nextInt(7) + 4;
```

In the example above, `n` will store a random integer between 4 and 10 inclusive. `Random` is another Java object that we have access to that takes care of the work of generating random numbers. The reason they're called pseudorandom numbers is because it's impossible for computers to be truly random, but it's good enough for any normal usage.

Next, we can discuss while loop syntax.

### Syntax
```
while (test) {
  statements(s);
}
```

### Example
```
int num = 1;                    // initialization
while (num <= 200) {            // test
  System.out.print(num + " ");
  num = num * 2;                // update
}
// output: 1 2 4 8 15 32 64 128
```

Notice that while loops have all of the same pieces as for loops. In fact, any loop that can be written as a for loop can also be written as an equivalent while loop. However, stylistic coding standards would assert that there's a time and place for both.

While loops are used when the number of times its body repeats is not known in advance. An excellent example of this is the guessing game. We have no idea how long we are going to have to prompt the user. The program could potentially run forever if they never guess the correct solution. Earlier, we used for loops when there was a task we wanted to execute a known number of times.

