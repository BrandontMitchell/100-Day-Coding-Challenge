# Day 012 - File Processing

The purpose of this day is to combine some of the tools that we've learned already to learn **file processing**. File processing can be incredibly useful especially when dealing with large files. There's a lot of new syntax for processing files, especially since we'll be generating our own files as well, but you'll find that it opens up many new problems we can solve.

For this challenge, you will be re-formatting the text in an input file. However, you will not be modifying the existing files (this is a much trickier task to do in Java). Instead, we'll be creating a new file.

## Starter Code

This day includes a single Java file in the starter-code folder titled `Starter.java`. This includes a lot of helpful lines of code that take care of connecting to the input file and setting up a way for us to write to an output file. There will be two methods that you'll be completing.

The first method is called `collapseSpaces`. The initial input file `messedup.txt` has a bunch of unnecessary whitespace between the words. `collapseSpaces` will be converting this file into a file called `lincoln.txt` that contains all the same information, just with a single space between each word.

The second method is called `leetSpeak`. This is an outdated meme that involves typing in a weird digitized way, but that's not really important to understand. It's basically just an informal language where a bunch of letters are replaced by numbers. This method should convert the newly formatted `lincoln.txt` file into a new file called `leet.txt`.

Here's what the content of the three files will look like once you complete the task succesfully:

### messedup.txt
```
four 		 score 	 	 and
  seven 	 	 years  	ago 			 our

fathers   brought 		 forth 		 	on this  	 	 continent
	 a 	 	 new  	 nation
```

### lincoln.txt
```
four score and 
seven years ago our 

fathers brought forth on this continent 
a new nation 
```

### leet.txt
```
(f0ur) (sc0r3) (4nd) 
(s3v3n) (y34rZ) (4g0) (0ur) 

(f47h3rZ) (br0ugh7) (f0r7h) (0n) (7hiZ) (c0n7in3n7) 
(4) (n3w) (n47i0n) 
```

One thing you might have noticed about the `Starter.java` file is that each of the methods have some additional text in their method header that says `throws FileNotFoundException`. This is a strange Java rule that they implemented to basically make programmers more careful. It's like signing a contract that says "I acknowledge that I might run into some really bad errors by using files but I'm still gonna do it anyways". 
  
## Getting Started

We have actually already learned almost all of the concepts needed to execute file processing Java, it's just a matter of learning the pattern and putting together the different pieces. We'll be using the Java `Scanner` object to read through input files token by token. Previously we saw Scanner being used to read in user input from the console, but the `Scanner` is versatile enough that it can be used on multiple different input sources. Let's first look at the syntax for how to connect `Scanner` to a file:

### Example
```
Scanner name = new Scanner(new File("name.txt"));
```

### Example
```
Scanner input = new Scanner(new File("input.txt"));
```

This part of the code has been taking care of for you, so you don't have to worry about it too much. The important part to understand is how the `Scanner` views the file. I'd encourage you to visualize the `Scanner` as a long two dimensional conveyor belt. The `Scanner` has no concept of line breaks; it's going to read through the file token by token. Let's look at an example to understand what constitutes a token:

Consider a file `numbers.txt` that contains this text:

```
308.2
    14.9 7.4 2.8
3.9 4.7     -15.4
    2.8
```

A Scanner views all input as a stream of characters. It would see `numbers.txt` like this:

```
308.2\n   14.9 7.4  2.8\n\n3.9 4.7    -15.4\n   2.8\n
^
```

The `\n` is the Windows representation of a **newline character**. This is what signifies the line breaks in the input file. In the example above, `numbers.txt` contains 8 tokens. A **token** is defined as a unit of user input, separated by whitespace. **Whitespace** includes any number of spaces, tabs, and line breaks.

Notice the arrow pointing at the very beginning of the file. This represents the **input cursor**, or the current position of the Scanner. If you don't recall, here are the `Scanner` methods:

* `nextInt()` 
    * reads an `int` from the input file and returns it
* `nextDouble()` 
    * reads a `double` from the input file
* `next()` 
    * reads a one-word `String` from the input file
* `nextLine()` 
    * reads a one-line `String` from the input file
    
Here's what happens to the input cursor when we use the `Scanner` methods on an input file:

`double x = input.nextDouble(); // 308.2`
```
308.2\n   14.9 7.4  2.8\n\n3.9 4.7    -15.4\n   2.8\n
     ^
```

`String s = input.next(); // "14.9"`
```
308.2\n   14.9 7.4  2.8\n\n3.9 4.7    -15.4\n   2.8\n
              ^
```

Notice that we have some liberty in how we choose to interpret tokens in the input file. In general, everything can be interpreted as a `String`, but text can not be interpreted as numbers. An important distinction to make is that `input.nextInt()` attempts to read the very next token as an `int`. It doesn't look ahead in the file for the next `int` it can find. This idea also applies to all of the other `Scanner` methods. 

This can lead to some issues, so make sure you're using the correct method based on what's next in the input file. If we don't know what the input file looks like ahead of time, the `Scanner` object provides some methods to peek ahead in the input file so we don't end up running into this problem.

* `hasNextInt()` 
    * returns true if there is a next token and it can be read as an `int`
* `hasNextDouble()` 
    * returns true if there is a next token and it can be read as a `double`
* `hasNext()` 
    * returns true if there are any more tokens of input to read
* `hasNextLine()` 
    * returns true if there are any more lines of input to be read
    
These methods will come in handy for us to make sure that we don't read too far into the file and run into problems. You can infer that the task of reading an input file of uknown size requires a while loop because we don't know how many iterations there will be ahead of time. These methods will serve as the test for our while loops, and allow us to safely read through the entirety of files without causing any errors.

Here's a template for using a while loop to perform line-based file processing:

```
Scanner input = new Scanner(new File("messedup.txt"));          
while (input.hasNextLine()) {
	String line = input.nextLine();
	Scanner words = new Scanner(line);
	while (words.hasNext()) {
		String token = words.next();
		
		// do something with token
		
	}
	output.println();
}
```
You'll notice that in the above example a `Scanner` can also be attached to a `String`. This isn't a huge leap to make from hooking up a `Scanner` to an input file. This template is a lot of code, but the nice thing is that the only unique part you have to generate each time is the commented section, and oftentimes the code in there is only a few lines.

The last thing should be aware of is the `PrintStream` object. Although this part is taken care of for you, here's the syntax for declaring a new `PrintStream` object:

### Syntax
```
PrintStream name = new PrintStream(new File("name.txt"));
```

### Example
```
PrintStream output = new PrintStream(new File("output.txt"));
```

This line of code will do two things: create a new file in the directory of the running program of the name that you put into quotes, and then allow you to write to that file. The `PrintStream` object can be used exactly like `System.out` since it has all the same methods. That means `output.println()` will work, as well as `output.print()`. Note that it is output in this example because that was the name we chose for our `PrintStream` object in the example. 
