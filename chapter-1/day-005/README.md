# Day 005 - Parameters

The purpose of this day is to introduce a huge concept in programming: parameters. 

For this challenge, you will be working with a helper program called `DrawingPanel` that was created by my professor at the University of Washington purely for the purpose of introducing parameters to students. It is a simplified version of the existing graphics Java libraries. Basically it will allow us to draw [mspaint](https://en.wikipedia.org/wiki/Microsoft_Paint) looking drawings.

You will be creating the image shown below:

![Image](https://github.com/BrandontMitchell/100-Days-CC/blob/master/images/vans.png)

## Starter Code

This day includes a two files in the starter-code folder. One is `DrawingPanel.java`, which is necessary for your program to work correctly. It should be downloaded along with `Starter.java` and placed in the exact same directory. You don't have to open the `DrawingPanel.java` file or understand it's contents whatsoever. That's one of the nice things about programming: you don't have to know how something works in order to use it effectively. Think about it like an average person listening to music on their radio. They just have to know how to operate the buttons, not wire it up themselves.

You'll notice that there will an unfamiliar line of code near the top of Starter.java that look like this:

```
import java.awt.*;
```
This is called an **import statement**, and it's necessary for DrawingPanel to work correctly. Your program won't compile without this line, because it tells Java to go out and get the required libraries before executing your program. It's not super important to understand why/how this works.

All of the code will go into the `drawCar` method.
  
## Getting Started

One other thing you probably noticed about `Starter.java` is that there is now code that appears inside of the parentheses of method calls that have previously been blank. Basically all of the methods that we've written so far have not used parameters, and so we left the parentheses blank by default. 

One place that we've actually already seen this before is the `System.out.println()` command. This is an example of a well parameterized method. What that means is it can take in basically whatever you put into the parentheses as a parameter, and then output that thing to the console. The alternative to having parameters would be to have a different method to print each character. You'd have a method called `System.out.printlnA()` and `System.out.printlnB()` and so on which would end up being a logistical nightmare. **Parameters** are the name for the things that go into the parantheses of method calls, and make our methods more flexible. Here's what the syntax looks like:

### Syntax
```
public static void main(String[] args) {
  name(expression);
}

public static void name(type name) {
  statement(s);
}
```

### Example
```
public static void main(String[] args) {
  sayPassword(42);
  sayPassword(12345);
}

public static void sayPassword(int code) {
  System.out.println("The password is: " + code);
}
```

### Output
```
The password is: 42
The password is: 12345
```

Parameters allow us to share variables between our methods. This allows us to get around the issue of scoping. **Scoping** is the concept that variables only exist within the closest set of curly braces that surround them.

### Incorrect Example

```
public static void main(String[] args) {
  int x = 45;
  sayPassword();
}

public static void sayPassword() {
  System.out.println("The password is: " + x);
}
```

This code will through a compiler error, because the variable `x` only exists inside of the main method. If I want to use it's value elsewhere in my program, I have to pass it as a parameter.

### Correct Example
```
public static void main(String[] args) {
  int x = 45;
  sayPassword(x);
}

public static void sayPassword(int code) {
  System.out.println("The password is: " + code);
}
```

The value of the expression passed in must be the same as the data type of the parameter specified in the method header. Notice how they don't have to have the same name as each other however. Methods can have as many parameters as you want, but each of them should have a distinct purpose.

The two method calls to `drawCar` have three parameters. One is the `Graphics` object, and the other two represent the x and y coordinates of where we want our car to appear on the canvas. The reason we pass the `Graphics` object as a parameter is so that we're not wasteful; this way we only need one brush that each of our methods can share. Although we don't know much about objects at this point, one thing to remember is that they're expensive in terms of space and memory. We shouldn't make more objects than we have to.

The reason our `drawCar` method accepts a parameter is similar to the reason that we don't have a separate `System.out.println()` method for each character. If I wanted to draw another car somewhere else on my canvas, then I would have to write an entirely new method that would look almost exactly the same. Why not have one method that's flexible enough to do the work of both?

The first two lines of code in main are what is necessary to get `DrawingPanel` up and running. The first line creates a new `DrawingPanel` object. You'll notice that we pass `DrawingPanel` two parameters when we first construct it. These two numbers represent the desired width and height of our canvas in pixels. Feel free to mess around with these numbers. Objects in Java are difficult to fully understand at this point in your programming career, but for now you can think of them as available tools that we have to work with that make our lives easier. In the case of `DrawingPanel`, it takes care of the process of opening a new window when you run your program that will act like a canvas that we can draw on. 

The subsequent line of code creates a new `Graphics` object. This is like the pen/brush that we will be using to draw on our `DrawingPanel`. One of the nice things about the `Graphics` and `DrawingPanel` objects is that they will greatly simplify the amount of work that we have to do to actually draw things. It takes care of the difficult and uninteresting stuff for us. The `Graphics` object (our brush) will act as a middleman that we can talk to in a way that's intuitive and easy to understand.

Here's some of the useful methods of the `Graphics` object that you can use to complete the task:

* `panel.setBackground(color);` 
  * sets the background color (changing canvas color)
* `g.setColor(color);` 
  * sets the pen color (like dipping a brush in paint)
* `g.drawLine(x1, y1, x2, y2);`
  * draws a line from point (x1, y1) to (x2, y2)
* `g.drawRect(x, y, width, height);`
  * draws outline of rectangle with top left corner at (x, y) and given width and height
* `g.drawOval(x, y, width, height);`
  * draws outline of largest oval to fit rectangle with top left corner at (x, y) and given width and height
* `g.fillRect(x, y, width, height);` 
  * `drawRect`, but fills in rectangle with current color
* `g.fillOval(x, y, width, height);` 
  * `drawOval`, but fills in oval with current color
* `g.drawString(text, x, y);` 
  * draws given text with its lower-left corner at (x, y)
* `g.setFont(font);` 
  * sets font for drawing strings
  
### Example
  
```
DrawingPanel panel = new DrawingPanel(400, 300);
Graphics g = panel.getGraphics();
g.drawRect(10, 30, 80, 100);
```

Here's a list of colors that you can use:

* `Color.BLACK `
* `Color.BLUE` 
* `Color.CYAN`
* `Color.DARK_GRAY` 
* `Color.GRAY`
* `Color.GREEN` 
* `Color.LIGHT_GRAY` 
* `Color.MAGENTA` 
* `Color.ORANGE` 
* `Color.PINK`
* `Color.RED`
* `Color.WHITE`
* `Color.YELLOW`

### Example
```
panel.setBackground(Color.YELLOW);
g.setFont(new Font("Arial", Font.BOLD, 16));
```

One weird thing about `DrawingPanel` that may seem weird is that the origin of the coordinate system is located at the top-left of the canvas. This is a strange but standard coding convention for graphics.

Here's a more detailed image of what you'll be recreating:

![Image](https://github.com/BrandontMitchell/100-Days-CC/blob/master/images/van-dimensions.jpg)
