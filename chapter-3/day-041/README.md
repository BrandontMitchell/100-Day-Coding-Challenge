# Day 041 - Introduction to HTML

The purpose of this day is to introduce one of the most approachable languages: HTML. HTML is what web developers
use to generate content on websites. This includes words, images, videos, tables, links, and more. Later on,
the structure of your HTML file will be very important when writing other files, and so it's an important
foundational starting point.

For this challenge, you will be creating your first pure HTML web page! This day is unique in that there is no 
correct solution. It's  more of an opportunity to explore [different HTML tags](https://www.w3schools.com/tags/). 

Side-Note: It may seem harsh, but providing links for you to do your own research will become a theme throughout this chapter. New concepts with HTML, CSS, and JavaScript will come in batches with hundreds of tags, elements, and features you can use. Even experienced web programmers Google stuff every day that they forget how to use. If you're ever unsure of something, or want additional information, visit w3schools(https://www.w3schools.com/). It's an excellent website with interactive visual examples. If you want extra clarification on a concept, then Google the name of that concept and w3schools, and click on the most relevant page. We will try to use vocabulary words that coincide with their website.

The `solution.html` file will act as both a cheat-sheet to be referred back to throughout the first 10 days, as well 
as a way to verify that you used tags correctly.

## Starter Code

This day includes a single file in the starter-code folder titled `starter.html`. This includes the
boilerplate structure of an HTML file.

All of the code that you write will go inside of the existing `<body>` tags.
  
## Getting Started

Before going more in-depth into HTML syntax, the first thing you'll need to do is download a text-editor to write your HTML code in. There are many different types of text-editors, and people have their own preference about which one they like to use. Here's our recommendation on which text editor to use if you don't have one downloaded already:

* Windows
  * [Atom](https://atom.io/)
* macOS
  * [Sublime](https://www.sublimetext.com/)
  
Both of these are entirely free, aesthetically pleasant, and simple to use.

In order to complete the challenge (and all future challenges):

1. Create a new folder somewhere on your computer to hold the starter code.

2. Download all of the files located in the starter-code folder into the folder you just created.

3. Open the text-editor of your choice, and then click File, Open Folder, and navigate to the folder you just created.

4. The folder structure will appear on the left-hand side of the text-editor, and from there you can open and edit files.

5. Once you've made your changes, make sure to save the changes, and then navigate to the folder you're working in with Finder/Windows Explorer, and double click on the HTML file to open it in your preferred web browser. Google Chrome has really good developer features, and so it's recommended to use for this chapter.

6. Oftentimes the best way to code websites is to simultaneously have your website open in Chrome and your code pulled up so that you can constantly make small changes and switch back and forth to see the result.

HTML works by surrounding text content with opening and closing **tags**. Each tag's name is called an **element**. Whitespace is largely ignored in HTML.

### Syntax

```
<element> content </element>
```

### Example

```
<p> This is a paragraph. </p>
```



The `<head>` tag describes the page and the `<body>` tag contains
the page's content.

An HTML page is saved into a file ending with the extension `.html.` The `<!DOCTYPE html>` tag tells the browser
to interpret the page's code as HTML.

### HTML Tags

There are many different types of HTML tags used to structure web pages (we can't possibly cover all of them).
But you can find a comprehensive list [here](https://www.w3schools.com/tags/).

### Extra Information

Tags must be correctly nested, meaning that a closing tag must match the most recently opened tag.

```
<p>
  HTML is <em>really,
  <strong>REALLY</em> lots of</strong> fun!
</p>
```

Some tags can contain additional information called attributes.

### Syntax:
```
<element attribute="value" attribute="value"> content </element>
```
### Example:
```
<a href="page2.html">Next page</a>
```

Some tags don't contain content and can be opened and closed in one tag.

### Syntax:
```
<element attribute="value" attribute="value" />
```
### Example:
```
<br />, <hr />, <br>, <hr>
```
### Example:
```
<img src="bunny.jpg" alt="pic from Easter" />
```

Block elements (paragraphs, lists, table cells) contain an entire large region of content.
The browser places a margin of whitespace between block elements for separation

Inline elements (bold text, code fragments, images) can appear on the same line.
They must be nested inside a block element.

There's much more to know about HTML that isn't covered here, but it's much easier to learn by experimenting than by having it explained to you!
