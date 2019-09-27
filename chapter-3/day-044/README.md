# Day 044 - Introduction to JavaScript

Now that we've learned how to add **content** and **styles** to a web page, we're going to explore how to add responsive **behavior**. This is where JavaScript comes in. JavaScript gives us the building blocks to dynamically update what you see on a web page in response to clicks, text input, timers, etc.

We will be creating an interactive [nonogram](https://en.wikipedia.org/wiki/Nonogram) game! This game (sometimes called Picross or Griddlers) is a simple puzzle game that is easy to recreate in JavaScript, especially if you already have a good foundation set up in HTML and CSS. The game involves a large grid of squares where each row and column are labelled with a series of numbers kind of like Sudoku. These numbers give you hints on how many squares in that row/column should be filled in. Combining the information you should be able to fill in squares by process of elimination until you end up with a picture in the end. 

## Starter Code

There are a few files in the starter-code folder for this week. `starter.html` and `starter.css` take care of the grid for you. 

Nonogram puzzles usually offer players the ability to cross out squares that they have determined by process of elimination cannot possibly be filled in. This will be accomplished by changing the background image of the squares to `x.png`, a small image of a transparent X. This is the third file in the starter-code folder.

Your job will be to implement a JavaScript file that adds functionality to the clear button, and allows users to click on boxes, cycling their background between white, black, and crossed-out. 

You are encouraged to start working off of the provided `starter.js` file. This includes two helper functions: `$` and `$$` which save you a lot of typing. They will be explained later. 

There are two important pieces of information to note about the `starter.html` file.

1. Each of the squares in the puzzle have been assigned the class name `box`. 

2. The ID of the clear button is `clear`

There are also two important pieces of information to note about the `starter.css` file.

1. The class `filled` gives a black background color.

2. The class `crossed-out` sets `x.png` as the background image.

You will be using JavaScript to toggle these classes back and forth as the user clicks on squares. Other than these pieces of information, you may ignore these two files and focus on writing the JavaScript.

## Getting Started

Before you can get started, we have to introduce some basic JavaScript syntax. Thankfully, you've already had plenty of experience working with both Java and Python so we can introduce the concepts by comparing similar aspects that these three languages have in common.

We will be using JavaScript as a **client-side** scripting language. This means that our code will run after the page has already loaded. Basically, we won't need to be connected to the internet to run client-side code; we can start programming in JavaScript in whatever browser we have on our computer.

Despite the name, JavaScript is not really related to Java, other than the name and some similar aspects of the syntax. JavaScript is an **interpreted** language, as opposed to Java which was a **compiled** language. Basically what this means for us is that JavaScript is going to do the best it can to produce something on the page. While Java wouldn't allow us to run our program at all if it found a compiler error, JavaScript errors are often silent. Variables don't need to be declared, and there are fewer data types that we have to work with. It's more similar to Python in these ways.

Here's how you would link your HTML file to a JavaScript file:

### Syntax

```
<script src="filename"></script>
```

### Example
```
<script src="example.js"></script>
```

This tag should be placed in the HTML page's `<head>` tag. Make sure to do this before you start programming in JavaScript! It can be really frustrating to keep making changes in your JavaScript file and for nothing to happen only to find out that the files were never connected.

Let's learn our first JavaScript command: `alert`.

### Syntax
```
alert("message");
```

### Example
```
alert("Hello! You have succesfully connected your JS file");
```

It's a nice sanity check to put a line of code like this into your JavaScript file before you start coding to make sure that everything is set up correctly. The `alert` command will generate a popup with the text that you place into the quotation marks.

Next, let's learn how to output values to the browser console. To view the console in your brower, open up the dev tools by right clicking and selecting Inspect anywhere on the page.

### Syntax
```
console.log("message");
```

### Example
```
console.log("The answer is: " + 42);
```

This command works exactly the same as the `System.out.println` command in Java. `console.log` is really useful for debugging purposes. You can find out what something's value is quickly and easily, without having to deal with a popup.

Comments in JavaScript are exactly the same Java, so we won't spend time covering those.

Variables and types work similarly to Python. Here's the syntax for it:

### Syntax
```
let name = expression;
```

### Example
```
let level = 23;
let accuracy = 0.9;
let name = "Ludicolo";
```

Variables are declared with the `let` keyword. Notice that variable types are not specified in the declaration statement, but JavaScript does have a loose concept of types. Some examples include `Number`, `Boolean`, `String`, etc. Integers and real numbers are the same type, so there is no concept of an `int` or `double` JavaScript uses the same arithmetic operators and precedence as Java.

JavaScript is a **dynamically-typed** lanugage, meaning that you can change the type a variable refers to throughout execution.

### Example
```
let isValid = true;
isValid = "hello!";
isValid = 1;
```

Java on the other hand was a **statically-typed** language, meaning that when declaring variables, you must specify their type which must always stay the same.

If you want to declare a variable that you do not intend to ever be updated, you can use the `const` keyword. This is similar to a class constant in Java.

### Syntax
```
const NAME = expression;
```

### Expression
```
const GRAVITY_CONSTANT = 9.81;
```

These constant values are statically-typed, and follow the `UPPER_CASING` naming convention.

Strings use many of the same methods as Java:

* `charAt`
* `indexOf`
* `replace`
* `substring`
* `toLowerCase`
* `toUpperCase`

Escape sequences also behave the same as in Java. One subtle difference is that `length` is a property of Strings in JavaScript and not a method. This means that to access the length of a String in JavaScript, there will not be any parantheses.

There is a `Math` object in JavaScript with almost identical methods to the `Math` class in Java. 

For loops work exactly the same as Java. Just remember that the initialization step will use the `let` keyword.

### Example
```
let sum = 0;
for (let i = 0; i < 100; i++) {
  sum = sum + i;
}
```

While loops and if statements follow an identical structure to Java's.

Relational and logical operators are identical to Java. Equality operators have a subtle difference. There are four ways to check equality in JavaScript:

* `==`
* `!=`
* `===`
* `!==`

The last two equality operators behave identically to `==` and `!=` in Java respectively. They perform strict equality tests which check both type and value. The first two equality operators only check value in JavaScript.

Some examples of `true` statements in JavaScript:
`5 < "7"`
`42 == 42.0`
`"5.0" == 5`

In general, the last two equality operators are generally what you want to use.

Boolean works the same as Java. One strange thing is that any value can be used as a Boolean. The list of things that evaluate to `false` is very short:

* `false`
* `0`
* `NaN`
* `""`
* `null`
* `undefined`

Literally everything else evaluates to true.

There is a slight distinction to be made between `null` and `undefined`. The latter refers to something that has been declared but not yet assigned a value. The prior means that something was specifically assigned an empty value.

Arrays in JavaScript work more similarly to `ArrayList` in Java than regular arrays.

### Syntax
```
let name = [];                          // empty array
let names = [value, value, ..., value]; // pre-filled
names[index] = value;                   // store element
```

### Example
```
let types = ["Electric", "Water", "Fire"];
let pokemon = [];        // []
pokemon[0] = "Pikachu";  // ["Pikachu"]
pokemon[1] = "Squirtle"; // ["Pikachu", "Sqiurtle"]
pokemon[3] = "Magikarp"; // ["Pikachu", "Sqiurtle", undefined, "Magikarp"]
pokemon[3] = "Gyarados"; // ["Pikachu", "Sqiurtle", undefined, "Gyarados"]
```

Arrays in JavaScript grow as needed when elements are added, similarly to an `ArrayList`.

JavaScripts' key construct is the **function**, rather than the method. 

### Syntax
```
function name(params) {
	statement;
	statement;
	...
	statement;
}
```

### Example
```
function myFunction() {
	console.log("Hello!");
	alert("Your browser says hi!");
}
```

The example above could be the contents of `example.js` and linked to our HTML page.

First, we can introduce the overall structure of a JavaScript file. We will be working with pure JavaScript for this chapter, which means that at no point will we make use of any additional JavaScript libraries. Here's what it looks like:

```
(function () {
	"use strict";

	// global variables
  let name = value;
  
	window.onload = function () {
		
    // code that is run when the page loads
    
	};

  // methods
  
  function name( ... ) {
  
  }
	
})();
```

Although you could just start writing JavaScript code and have it work mostly fine, we've introduced some structural syntax to help you write well-styled code. This program follows the **module pattern***. It wraps all of the file's code in an **anonymous function** (function without a name) that is declared and immediately called. This doesn't introduce any global symbols, nicely **encapsulating** our code and preventing it from being messed with externally.

Writing `"use strict";` at the very top of your JavaScript file turns on strict syntax checking. It will help you debug your code, especially since JavaScript is notoriously difficult to debug.

`window.onload` is similar to your main method in Java. Any code that you place inside of this function will always execute when the page is finished loading. Normally JavaScript is an **event-driven** programming language, meaning that it responds to events from the user, like a click or scroll. This is one of the exceptions to that.

Let's talk more about the idea of event-driven programming by making a responsive button. Let's say a button exists somewhere in our `<body>` tag like so:

```
<button id="my-btn">Click me!</button>
```

In order to make this button responsive, the first thing we need to do is access the HTML element in our JavaScript code. To access an element, you use `document.getElementById`. This function returns an object for an HTML element with the given `id` in the document. 

### Example
```
let element = document.getElementById("id");
```

Notice that you omit the `#` when giving an id in JavaScript unlike CSS.

Then, you set up a function to handle the click event.

### Example
```
element.onclick = handleClick;
function handleClick() {
  // event handler code;
};
```

The `handleClick` function in the example above is referred to as an **event handler**. When you interact with the element in the specified way (in this case a click), the function will execute. `onclick` is just one of many **event attributes** we'll see.

Let's put this all together:

```
<button id="my-btn">Click me!</button>
```

```
let button = document.getElementById("my-btn");
button.onclick = sayHello;

function sayHello() {
  alert("Hello there! I see you've clicked the button.");
}
```

Now when you click on the button, given that the files are linked correctly, you'll see a popup appear in your browser with the specified message. This example has exposed the underlying structure of HTML pages. This tree-shaped structure built out of all the HTML elements in a page is referred to as the **Document Object Model** or DOM. It's a set of JavaScript objects that represent each element on the page. Each tag in a page corresponds to a JavaScript DOM object.

Here's how to visualize the tree:

```
<html>
  <head>
    <title> ... </title>
  </head>
  <body>
    <h1> ... </h1>
    <div>
      <p> ... </p>
    </div>
  </body>
</html>
```

![DOM Tree](https://github.com/BrandontMitchell/100-Days-CC/blob/master/images/dom.png)

There are three ways to access DOM elements in JavaScript. We've already seen one of them:

1. You can ask for them by `id`: `document.getElementById`

2. You can query for them with CSS style selectors: `document.querySelector`

3. You can query for multiple at once with `document.querySelectorAll`. This will return an array of all elements that match the provided CSS selector.

Since `document.getElementById` and `document.querySelectorAll` are used so much in JavaScript, programmers will oftentimes introduce a helper function with a short name, like `$` to act as an alias. This is what the `starter.js` file has done for you.

Here's an example of how to use `document.querySelectorAll`:

```
let paragraphs = document.querySelectorAll("p");
for (let i = 0; i < paragraphs.length; i++) {
  paragraphs[i].style.color = "red";
}
```

The code above will make all of the text contained in `<p>` tags red. You'll notice you that every DOM object has a `.style` property that you can use to access anything that you would be able to access in CSS. The only difference is the naming convention. If you want to change the `background-color` CSS attribute using the DOM model, then you can access the `.style.backgroundColor` property of the DOM element. This is the reason we stressed camelCasing naming convention during chapter 1. If you want a full list of things you can access, look [here](https://www.w3schools.com/jsref/dom_obj_style.asp).

The DOM object stores several other pieces of information about the HTML element it represents. For starters, it stores the HTML attributes.

### Example
```
<img id="puppy" src="images/puppy.png" alt="A fantastic puppy photo"/>
```

```
let puppyImg = document.getElementById("puppy");
puppyImg.src // images/puppy.png
puppyImg.alt // "A fantastic puppy photo"
```

There are also properties of every DOM object:

* `tagName`
  * an element's HTML tag
* `className`
  * CSS classes of element
* `src`
  * URL target of an image
* `href`
  * URL target of a link
* `innerHTML`
  * stores the contents of the HTML tag as a string

The DOM property that we will primarily be using to complete today's challenge is called `classList`. The `classList` collection has methods `add`, `remove`, `contains`, and `toggle` that you can use to manipulate the CSS classes being applied to a DOM element.

### Example
```
function highlightField() {
  // turn text yellow
  let text = document.getElementById("text");
  if (!text.classList.contains("invalid")) {
    text.classList.add("highlight");
  }
}
```

Here's some tips for a development strategy:

1. Make an alert popup when a user clicks a tile. We just covered a huge amount of information, so if you can get this setup it's a really good starting point. You'll need to set up an event handler when the page loads to attach a function to each time in the grid. Remember that each tile in the grid has the class `box`. 

2. Make a single tile turn black when its clicked. Remember there is an existing class in the `starter.css` file called `filled` that handles styling for you. You should add this class using the `classList` collection when a user clicks on a box.

3. Modify the `onclick` event to toggle the `filled` class. In other words, if the tile is white, it should change to black, an if it is filled, it should change back to white.

4. Add a clear button to the page. It should remove the `filled` class from all the boxes. If you'd like, you can add a [`confirm`](https://www.w3schools.com/jsref/met_win_confirm.asp) event.

5. Modify the `onclick` event to cycle between white, black, and and X background. You can do this by accessing the `style.backgroundImage` of a box.

### Extra-Credit Challenges

1. Add a hover effect to the boxes. Hint: use the `:hover` selector in CSS and modify the `box-shadow` property.

2. Add a submit button to the page that allows the user to check if they correctly solved the puzzle.

3. Add a drag and fill feature.





















