# Day 049 - Web Services

For today's challenge, you will be getting more practice with PHP by using it to write our own trivia web service. Your file, `solution.php` will navigate a local file system of directories to service JavaScript requests with formatted data. Basically, you'll be implementing an API!

Since we're nearing the end, today's challenge will be one of the most challenging you've had so far. Don't be discouraged, remember what you've learned, and good luck!

## Starter Code

This day includes several files in the starter-code folder. You can safely ignore the contents of `starter.css`, `starter.html`, and `starter.js`. Make sure that you download and unzip the `starter.zip` folder in the same directory as all the other files. Look inside of the `starter` folder after unzipping it to familiarize yourself with its contents.
  
## Getting Started

One of the things that PHP is actually good at is dealing with files. Here's an overview of some useful PHP file functions:

* [`glob`](https://www.w3schools.com/php/func_filesystem_glob.asp)
  * returns an array of all file names that match a given pattern. `glob` can match a wildcard path with the `*` character.

* [`scandir`](https://www.w3schools.com/php/func_directory_scandir.asp)
  * returns an array of all file names in a given directory

* [`file_get_contents`](https://www.w3schools.com/php/func_filesystem_file_get_contents.asp)
  * returns entire contents of a file as a single string

### Part 1: Setting up the PHP file
  
1. Create a file called `trivia.php`. Don't forget to include `error_reporting(E_ALL)` at the top.

2. Download all of the necessary starter-code and place it in the same directory as your php file. Note that you will have to unzip the `starter.zip` folder.

3. Write PHP code to print out the contents of a random file in the trivia folder. You will find the `glob`, `scandir`, `array_rand`, and `file_get_contents` functions to be especially helpful for this part.

4. Test your service by refreshing the page several times and making sure you are getting random questions and answers.

### Part 2: Adding Parameters

Modify your `trivia.php` file to take a parameter called `mode`. When the user passes in a `mode` value of `categories`, your service should output a list of all the subdirectory names in the unzipped `trivia/` folder. If it is passed a value of `category` for `mode` then your web service should behave as it did before.

### Part 3: Outputting JSON

When passed the `mode` value of `category`, alter your web service to output the question and answer in the JSON format displayed below:

```
{
  "question" : "What Pokemon comes first in the Pokedex?",
  "answer" : "Bulbasaur"
}
```

When sent the `mode` value of `categories` update your file to output JSON data in the format below: 

```
{
  "categories" : [
    { "biology" : 12},
    { "computerScience" : 10},
    { "internet" : 10},
    { "pokemon" : 12}
  ]
}
```

`biology`, `computerScience`, etc. are the names of the folders in the `trivia` directory. The numbers are the counts of files in each folder.

