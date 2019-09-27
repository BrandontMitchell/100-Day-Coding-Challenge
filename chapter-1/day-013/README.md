# Day 013 - File Processing Cont'd

The purpose of this day is to build off of the tools that you learned in the previous day to do something a little bit more interesting than re-formatting an input file.

For this challenge, you will be creating a game of MadLibs! If you haven't heard of this game, it involves one person asking for a series of words (like a noun or color) that will be used to substitute into a template story without context. After the person is done asking for words, the story can be read back and it'll oftentimes be funny and make little to no-sense.

Let's say the template file looked like this:
```
One of the most <adjective> characters in fiction is named
"Tarzan of the <plural-noun> ." Tarzan was raised by a/an
<noun> and lives in the <adjective> jungle in the
heart of darkest <place> . He spends most of his time
eating <plural-noun> and swinging from tree to <noun> .
Whenever he gets angry, he beats on his chest and says,
" <funny-noise> !" This is his war cry. Tarzan always dresses in
<adjective> shorts made from the skin of a/an <noun>
and his best friend is a/an <adjective> chimpanzee named
Cheetah. He is supposed to be able to speak to elephants and
<plural-noun> . In the movies, Tarzan is played by <person's-name> .
```

Then here's what the sample output of your program should look like:

```
Please type a(n) adjective: silly
Please type a(n) plural noun: dogs
Please type a(n) noun: computer
Please type a(n) adjective: ugly
Please type a(n) place: Canada
Please type a(n) plural noun: horses
Please type a(n) noun: bobblehead
Please type a(n) funny noise: BANG
Please type a(n) adjective: fuzzy
Please type a(n) noun: keyboard
Please type a(n) adjective: smelly
Please type a(n) plural noun: cars
Please type a(n) person's name: Brandon

Your mad-lib has been created!
Check the directory this program is located in
for a file named output.txt
```

More importantly, your program should generate a new output file that looks like this:

```
One of the most silly characters in fiction is named 
"Tarzan of the dogs ." Tarzan was raised by a/an 
computer and lives in the ugly jungle in the 
heart of darkest Canada . He spends most of his time 
eating horses and swinging from tree to bobblehead . 
Whenever he gets angry, he beats on his chest and says, 
" BANG !" This is his war cry. Tarzan always dresses in 
fuzzy shorts made from the skin of a/an keyboard 
and his best friend is a/an smelly chimpanzee named 
Cheetah. He is supposed to be able to speak to elephants and 
cars . In the movies, Tarzan is played by Brandon . 
```

Keep in mind that the original file is unmodified. The new file should be formatted exactly the same, only with the placeholders replaced by the user input.

You'll be making two files: `madlib.txt` and `Solution.java`. The prior will resemble the template file in the example above, and the latter will contain your solution program. Since today's solution is a little bit challenging, we will provide two days to complete it.

## Starter Code

This day includes a single file in the starter-code folder titled `Starter.java`. It takes care of the process of creating a `Scanner` for reading user input, a `Scanner` connected to an input file, and a `PrintStream` object for writing to an output file. Your job will be to implement the `create` method. This does the work of reading through the template file token by token and prompting the user to type things in.
  
## Getting Started

There is no new information required for today, but here are a few tips in terms of development strategy.

* Start off by writing your `madlib.txt` file. This can be fun, and it's not too tricky. Try to leave spaces for a variety of different words that the user can type in. Placeholders should start with a `<`, end with a `>` and if it is multiple words the words should be separated by dashes.

* Look back at the line-based file processing template from the previous day if you're stuck on how to approach the problem. If you follow the template, there's very little code that you actually have to write to make it work.

The program works by processing the input file token by token. There are two cases:

1. The current token is not a placeholder. In this case, you should just print it to the output file along with a trailing space.

2. The current token is a placeholder. In this case, you should use `String` methods to format the placeholder text, and then prompt the user to type in whatever the placeholder was. Then, you should print what the user typed in to the output file.
