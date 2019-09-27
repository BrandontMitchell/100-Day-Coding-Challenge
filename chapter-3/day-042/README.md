# Day 042 - Layout in CSS

The purpose of this day is to introduce CSS, a language used for styling websites. CSS, along with HTML, is used
to control the appearance and layout of information on a web page. It is preferred to place all of your CSS code
into a separate file with the `.css` extension.

Here's an example of a bad way to produce styling:
```
<p>
  <font face="Arial">Welcome to Greasy Joe's.</font>
  You will <b>never</b>, <i>ever</i>, <u>EVER</u> beat
  <font size="+4" color="red">OUR</font> prices!
</p>
```

Why is this bad? Tags such as `<b>`, `<i>`, and `<u>` are discouraged in strict HTML because for one they lack any semantic meaning. There are alternative tags such as `<bold>` and `<em>` that are more accessible for screen readers. Moreover, it's disorganized and makes changing the style of the webpage difficult.

CSS allows us to easily apply styling to elements in a way that can be changed later. Keeping your HTML (content) separate from
your CSS (presentation) is an important web design principle. If a website contains no inline styling, then it's entire appearance 
can be changed by swapping the CSS file. You can see a good example of this [here](http://www.csszengarden.com/).

## Starter Code

This day includes a single file in the starter-code folder titled `starter.html`. This includes a pure HTML website that you will be styling with CSS.

You will be creating a new file `solution.css` to go in the same directory as `starter.html` to provide styling to the existing website. If you open up the website in your browser, then it should give you pretty thorough instructions on how to style the website. It will be good practice in using the [Chrome Dev Tools](https://developers.google.com/web/tools/chrome-devtools). 
  
## Getting Started
  
You can connect a CSS file to your HTML file by including the following code:

### Syntax

```
<head>
  ...
  <link type="text/css" href="filename" rel="stylesheet" />
  ...
</head>
```

### Example

```
<link type="text/css" href="style.css" rel="stylesheet" />
```

Once it's connected you can start producing styling by adding code to your CSS file. A CSS file consists of one or more rules. Each **rule** uses a **selector** to apply style **properties** to HTML elements that match the selector. Selectors are keywords that are used to reference one or many HTML elements on a page. Properties are things like `font-size`, `color`, and `width`.

### Syntax:
```
selector {
  property: value;
  property: value;
  ...
  property: value;
}
```
### Example:
```
p {
  font-family: sans-serif;
  color: red;
}
```
This rule would make all of the text contained inside of `<p>` tags on the website red, as well as change their font to sans-serif.

### List of Common CSS Properties

* Foreground and background color styles
  * `color`
  * `background-color`
* Font styles
  * `font-family`
  * `font-size`
  * `font-style`
  * `font-weight`
* Text styles
  * `text-align`
  * `text-decoration`
  * `text-indent`
  * `text-shadow`
  * `text-transform`
* Line/word/letter styles
  * `line-height`
  * `word-spacing`
  * `letter-spacing`
  * `list-style-type`
* Background styles
  * `background-image`
  * `background-repeat`
  * `background-position`
  * `background-attachment`
  * `background-size`
* Layout styles
  * `margin`
  * `padding`
  * `border`
  * `text-align`
  * `position`
  * `display`
  
## Grouping Styles

A selector can select multiple elements separated by commas.

### Syntax
  
```
selector1, selector2, selector3 {
  property: value;
  property: value;
  ...
  property: value;
}
```

### Example

```
p, h1, h2 {
  color: green;
}
```

## Conflicting Styles

When two rules set conflicting values for the same property, the latter style takes precedence.

### Example

```
h1, h2 { 
  color: blue; 
  font-style: 
  italic; 
}
h2 { 
  color: red; 
}
```

In this example, all of the `<h2>` elements will appear as red, because that style came later in the CSS file. 

## ID's and Classes

**id** and **classes** give us another way to refer to HTML content in CSS (and later in JavaScript). 

### Example

```
<p id="product-12345" class="product">Puppy calendar</p>
<p id="product-133337" class="product">Cat mug</p>
```
In this example, both paragraphs have the same class (product) but each have their own id.

How do you decide which one to use? Classes are generally preferable because each element can only have a single id. There
is no limit on how many classes and HTML element can have. However, if you truly want to apply unique styling to a single
element, then an id is probably the way to go.

### Main Differences:

* `id`
  * a unique identifier for an element
  * only allowed one id value per page
  * each element can only have one `id`
* `class`
  * non-unique grouping attribute to share with many elements
  * many elements (even different tags) can share the same `class`
  * each element can have many different classes
  
  


