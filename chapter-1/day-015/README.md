# Day 015 - Arrays

The purpose of this day is to introduce one of the most fundamental programming concepts: arrays. This concept is definitely not unique to Java; it exists in almost every programming language.

For this challenge, you will be finding out a little bit more about why the main method header is written the way it is. Although the solution will require very little code, today's challenge will be a good introduction to a lot of important concepts, including the command line. You will be writing a Java program that reverses the order of its command line arguments. If that sentence didn't make any sense, then keep on reading down below.

## Starter Code

This day includes a single file in the starter-code folder titled `Starter.java`. This includes the
boilerplate structure of a Java program.

All of the code that you write will go inside of the main method.
  
## Getting Started

Before going more in-depth into HTML syntax, the first thing we'll need to do is acquaint ourselves with the **command line**. The command line is a different means of interacting with your computer than the screen and mouse. It involves typing in successive lines of text that act as commands to accomplish different things. Some examples might involve navigating the file structure in your computer, opening a file, creating a file, etc. The average computer user will never use a **command line interace** (CLI) because we have widely transitioned to **graphical user interfaces** (GUI). GUIs are the menu-driven interactions of clicking and dragging things on a screen that you're used to with computers.

However, if you're a programmer, then you might find that the CLI can be much more effective in many different tasks. For example, most users prefer to use the command line to interact with GitHub (this website) when they are uploading and downloading files. They can be faster, programmable, customizable, repeatable, and allow you to work remotely. Another advantage of the command line is for internet tutorials. It can be much easier to copy and paste a command than it is to follow an entire tutorial. It bypasses a lot of differences that people might have from machine to machine.

A **shell** is the name of the interactive program that allows you to run commands. For our purposes it's synonymous with the command line; we're going to type commands into the shell, and the shell is going to run the commands. There are many different types of shells, but we will be using **bash** because it is the most commonly used one.

If you're using Linux, then bash is the default shell already installed on your system. If you're using macOS, then the terminal will do just fine. You can find it by searching your list of programs. If you're using Windows, then [here](https://www.windowscentral.com/how-install-bash-shell-command-line-windows-10) is a quick tutorial on how to install bash.

Once you have bash (or terminal) installed, you can open it up and you'll see something that looks like this:

```
username@My-PC:/mnt/c/Users/Josh/Desktop$ 
```

Your cursor should be blinking after the dollar sign. It may seem crazy, but before GUIs were invented, this is what using a computer was like. Right now the series of forward slashes is indicating my working directory. If you were using Finder or Windows Explorer, then it would be the folder that you're currently in. You can verify this by typing `pwd` into the command line and pressing enter. This stands for "print working directory".

The immediate thing you normally do after opening a new shell or folder is look around to see where you are. The way you accomplish this is with the `ls` command. If you type `ls` into the shell and press enter it will list out all of the files and folders in your current directory. 

To navigate through your computer's file structure, you can use the `cd` command. This stands for "change directory". `ls` and `cd` are normally used in conjunction because you first need to check which folders are available to navigate to, before you decide where you want to navigate to next. Now that you've executed the `ls` command, you can navigate to a folder by typing `cd name` where name is the name of the folder. When you executed the `ls` command, you can tell which files are folders by looking for the ones with no file extension.

The `cd` command is the first example of a bash command that uses an **argument**. Arguments are parameters for the command; they give it more information that's necessary to complete it's task. Arguments are the next token that you include after the command before you press enter. In our case, the file name was our sole argument.

Use `ls` and `cd` to navigate to a place on your computer that you'll later be able to find. 

Next, we're going to create a file. In your shell, type: `touch Solution.java`. `touch` is the command used to create files. If you immediately execute an `ls` command afterwards, you'll notice that a file named `Solution.java` will have appeared in your working directory. 

To open the file and see it's contents, we'll need to use a text-editor just like jGRASP. It would be very difficult to operate a program like jGRASP within the shell, so bash has some simplified built-in text editors. We'll be using nano as our text editor. Although we'll include most of the relevant commands, [here](https://wiki.gentoo.org/wiki/Nano/Basics_Guide) is a quick tutorial on some basic nano commands if you're curious or get stuck. If you've ever used notepad on Windows or Mac this will be pretty similar. 

To open your file with nano, type: `nano Solution.java`. You can do the same with most types of files. The screen will change to a mostly blank window with some commands at the bottom. Type out a simple Java program with a `System.out.println()` statement in the main method and when you're done, press Ctrl+O to save the changes you've made, and Ctrl+X to exit nano. This will bring you back to the command line.

To compile your program, type `javac Solution.java`. The `javac` command accepts a single argument which is the name of the file you are trying to compile. If there were any compiler errors, they will be printed in the command line. If the command was successful, you can execute the `ls` command to verify that a file named `Solution.class` has appeared in your working directory.

Now, we can run the program. To run your program, use the `java` command. This accepts a single argument which is the name of the file you are trying to run excluding the extension. For example, `java Solution` will run your `Solution.java` file. If you did everything correctly, your output should be printed to the console. Now you should have all of the tools you need to write and run Java programs in the command line.

The next thing we need to do is talk about arrays:

**Arrays** are objects that store many values of the same type. If you think of a variable as a box storing a piece of information, then an array is like a series of lockers or a cubby system. We use specific terminology when talking about arrays. An **element** is a single value in an array. An **index** is a 0-based integer used to locate/access an element from an array. If you recall, `String` also uses 0-based indexing.

Here's the syntax for making a new array:

### Syntax

```
type[] name = new type[length];
name[index] = value;
```

### Example

```
int[] data = new int[10]
data[3] = 7;
```

The example above will generate an array that can be visualized like this:

| 0  |  0 |  0 | 7  | 0  |  0 | 0  |  0 |  0 | 0  |
|----|----|----|----|----|----|----|----|----|----|

Notice that the fourth element was assigned to the value 7, because of zero-based indexing. Arrays are what is reffered to as a zero-initialized. This means that when you ask for an integer array of size 10, you will get 10 empty boxes with 0 in them.

You've actually seen an array this entire time without realizing it. When you typed:

```
public static void main(String[] args) {

}
```

you were creating a main method with a single parameter, and that parameter was an array of `String`. More specifically, it's an array of `String` that holds all of the command line arguments that were passed in when someone ran our program. So, if someone in the command line had executed the command:

```
java Solution hello my name is
```

Then the String array `args` would look like this:

| hello  |  my |  name | is  |
|--------|-----|-------|-----|

Your job will be to write a program that prints out all of it's command line arguments in reverse order. So if the call had been:

```
java Solution hello my name is
```

Then your program should produce the output:
```
olleh
ym
eman
si
```

It is really common to use for loops to access array elements. Here's the general structure for that:

```
for (int i = 0; i < name.length; i++) {
  // do something with name[i]
}
```

You can use an array's `length` field to find out how many elements it stores.

Similarly, you can use for loops to access characters in a `String`. Now that you know about the concept of arrays, you know that a `String` is really just an array of characters.

```
for (int i = 0; i < name.length(); i++) {
  // do something with name.charAt(i)
}
```

You will need to use both of these patterns to complete today's challenge.







