# Day 047 - GET and POST

The purpose of this day is to understand more about how APIs work by implementing our own. Unfortunately, we will be using PHP because relative to other server-side languages, it is probably the easiest to get up and running. PHP, while still a widely-used programming language, has been in decline for many years now. Flask with Python, Node.js, and others are slowly eclipsing PHP. However many public APIs are still written in PHP, and so it will be a smooth transition for these challenges in terms of continuity.

You will be creating two PHP programs.

The first, `calculator.php`, will take in three parameters: two numbers and an operation to perform. Based on the operation, it will either provide the sum, difference, product, or quotient of the two numbers.

The second, `password.php`, will take in two parameters: a username and password. It will return a JSON object with two fields containing information about the validity of the username and password respectively.

## Starter Code

This day has two folders within the starter-code folder, one for each PHP program you will be writing. 

The calculator folder contains a single file titled `starter.php` that contains the boilerplate structure of a PHP file. It also includes some code to make sure that all of the parameters have correctly been passed in. This code will be discussed later.

The password folder contains three files, `starter.html`, `starter.js`, and `starter.php`. You can safely ignore both the `starter.html` file as well as the `starter.js` file. The `starter.php` file is similar to the other `starter.php` file in the calculator folder. It contains the boilerplate structure of a PHP file and includes some code to make sure that all of the parameters have correctly been passed in.

The two lines of code:
```
ini_set('display_errors', 'On');
error_reporting(E_ALL);
```

help you to see errors, because PHP can be really tough to debug otherwise.
  
## Getting Started
  
PHP is a **server-side** programming language like we mentioned before. **Web servers** contain software that runs these programs and sends back their output. Each language has its own pros and cons, and we will be using PHP.

We have been used to dealing with **static content**. This is what normally happens when you navigate to a web page. The server directly sends the `.html` file that you asked for and displays it in your browser.

When a web browswer requests a `.php` file, the server will first read the file, run any script code inside of it, and the return the output of the file. This is referred to as **dynamic content**.

Here's what a PHP file skeleton looks like:

### Syntax 
```
<?php
  //PHP code goes here
?>
```

The way that you produce console output is with the `print` or `echo` commands. They both have the same functionality.

### Syntax
```
print "text";
echo "text"; 
```

### Example
```
print "Hello, World!\n";
print "Escape \"chars\" are the SAME as in Java!\n";
print "you can have
line breaks in a string.";
```

Arithmetic operators are the same as Java and JavaScript. The only difference is that it uses a special operator for String concatenation: `.`. Here's what that looks like:

### Example
```
5 + "2 turtle doves" // 7
5 . "2 turtle doves" // 52 turtle doves
```

Variable syntax is a little bit new, but more similar to JavaScript than Java.

### Syntax
```
$name = expression;
```

### Example
```
$user_name = "Koding4Lyfe";
$age = 25;
$age_in_dog_years = $age / 7;
$this_class_rocks = TRUE;
```

One important note to make is that variable names always begin with `$` on both declaration and usage. PHP is awful that way.

Similar to JavaScript, types are implicitly declared by assignment. There is still the concept of all the same basic types as Java in PHP. There is a new concept we didn't explicitly cover before called casting. **Type-casting** refers to the process of converting between types in a single instance within an expression.

### Syntax
```
$name = (type) expression;
```

### Example
```
$age = (int) "21";
```

This is especially relevant for the calculator program because we'll have to convert from strings to numbers.

You won't need them for today but [here](https://www.w3schools.com/php/php_ref_string.asp) are the string functions in PHP since they have their own names.

Boolean operators work the same way as Java and JavaScript but in the case that it comes up, PHP uses all uppercase to represent it's two boolean values: `TRUE` and `FALSE`. This also applies to `NULL`. 

There is a function used in the `starter.php` file called `isset` this takes a variable as a parameter and returns true if that variable was assigned a value and is not `NULL`.

### Example
```
if (isset($var1)) {
  print ("This line isn't going to be printed");
}
$var2 = 12;
if (isset($var2)) {
  print ("This line WILL be printed");
}
```

We use this to ensure that the parameters to our PHP program are properly set so we don't run into any errors.

For loops work exactly the same as Java and JavaScript, but look weird because of the dollar signs:

### Syntax
```
for ($i = 0; $i < 10; $i++) {
  print "$i squared is " . $i * $i . "\n";
}
```

If/else statements and while loops work the same as Java and JavaScript. Comments work the same as Java, but the `#` character is also allowed to indicate a single line comment.

Arrays work in their own strange way in PHP, but it's more or less what we're used to.

### Syntax
```
$name = array(); # create
$name = array(value0, value1, ..., valueN);
$name[index] # get element value
$name[index] = value; # set element value
$name[] = value; # append PHP
```

### Example
```
$a = array(); # empty array (length 0)
$a[0] = 23; # stores 23 at index 0 (length 1)
$a2 = array("some", "strings", "in", "an", "array");
$a2[] = "Ooh!"; # add string to end (at index 5) 
```

One interesting thing is that the element type is not specified, so you can mix types in an array. PHP also has this thing called an **associative array** which maps keys to values that you assign to them. A good analogy is a dictionary; the key is the word and the value is the definition.

### Example
```
$age = array("Spot"=>16, "Whitney"=>16, "Jack"=>12); # create
$age["Mowgli"] = 1;
```

Arrays in PHP unfortunately have their own set of methods associated with them, so although we won't be using them for today, you can view them [here](https://www.w3schools.com/php/php_ref_array.asp).

PHP has functions instead of methods that work exactly like JavaScript functions.

The only thing we need to learn now is how to send parameters in an AJAX fetch. We've actually seen an example of this with the trivia function from the previous day's challenge. There are two ways to do it, and it depends on the type of request that you want.

For GET requests, you add them to the end of the url:

### Syntax
```
url.php?param1=value1&param2=value2
```

**GET** requests work by passing parameters through the url. The entire php file at that point works like one big function to return information back to you based on the parameters that you passed in. In the previous week, we used the url `https://opentdb.com/api.php?amount=1` because the parameter `amount` indicated to the database how many trivia questions we wanted to get back. GET requests are preferable for things like public APIs where the information is not private because they're transparent and easy to use. You can also physically navigate to the URL and see the data being returned to you which is a nice feature. This is the type of request that we'll be using for `calculator.php`.

**POST** requests require you to do some more complex things in JavaScript. First, you create a `FormData` object and then append key value pairs containing the parameters that you want to send in. You won't have to worry about this because the JavaScript file takes care of it for you, but if you're curious then you can take a look at the `starter.js` file. POST requests are useful for transferring secure data. This is the way that logging in to a website will often work, because POST requests offer functionality to securely encrypt your data before sending it to the server. This way your password won't be showing up as plain text in the url of an API call. This is the type of request that you'll be using for `password.php`.

The only part of this parameter sending process that we need to understand for our purposes is that PHP automatically stores any GET and POST parameters into built in associative arrays called `$_GET` and `$_POST`. If you want to access the POST parameter `age` then you reference it in PHP as `$_POST["age"]`.

For the `calculator.php` file, it'll be sufficient to `print` or `echo` out the result of the operation as plain text. This doesn't require any extra work. However, for the `password.php` file, you'll need to return JSON formatted data. Here's how to do that:

### Syntax
```
$name = new \stdClass();
$name->key = $variable;
$name->key = "value";

header('Content-type: application/json');
print json_encode($name);
```

This involves creating what is basically a PHP object. We won't go into too much detail on this.

### Example
```
$response = new \stdClass();
$response->usernameerror = $username_error;
$response->passworderror = $password_error;

header('Content-type: application/json');
print json_encode($response);
```

The trickiest part will be testing your PHP code from here on out. Here's two ways you can do it, in order of best to worst options.

1. Download [wamp](http://www.wampserver.com/en/download-wampserver-64bits/#) so that you can run a local server and test your PHP code. Basically you'll install this program, put all your files in a specific folder, turn on the server, and then it will be as if you're working online.

2. Use [this](http://phptester.net/) online sandbox to run your PHP code. It doesn't allow you to pass in parameters however, so you'll have to hard-code the values in.
