# Day 006 - Animation

The purpose of this day is to build on the concepts from yesterday and take advantage of some of the cool features included in `DrawingPanel`.

For this challenge, you will be creating a simple animation with `DrawingPanel`. This day is unique in that there is no 
correct solution. It's more of an opportunity to be creative and make your own animation. It's exactly like last week, only there is no guided drawing you are trying to reproduce. You get to make whatever you want!

## Starter Code

This day includes two files in the starter-code folder. One is `DrawingPanel.java` and the other is `Starter.java`. Just like last week, you will download both of these files and place them inside of the same directory in order for it to work.

All of the code that you write will go inside of the provided draw method. Feel free to play around with using different values for the for loop in main.
  
## Getting Started

The way this program works is similar to a flipbook. In the main method, there is a for loop set up to run 50 times. On each iteration of the for loop, the program pauses for 10 milliseconds with `panel.sleep(10)`, clears the entire canvas with `panel.clear()`, and then draws something. Since the draw method is conveniently parameterized for us, we can pass in an expression for the value of the x coordinate parameter instead of a constant number. This causes each subsequent drawing to appear 5 pixels to the right of the previous one. Since the program runs quickly enough, the result is a mediocre flip-book type animation.

When implementing your draw method, try to incorporate the size parameter if possible. The only paramaters strictly necessary for this to work are the x coordinate and the `Graphics` object, but the other two parameters help your animation become more flexible if you want to change it later. It's also good practice in writing generalized code. You can go about doing this by first writing code to make it work, and then figuring out how you want your drawing to scale. If it's too difficult, you can omit this part entirely.

The sample solution uses the `drawCar` method from the previous day if you'd like an example to work off of.
