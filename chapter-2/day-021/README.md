# Day 021 - Introduction to Web scraping

The purpose of this day is to understand the power of scraping data from websites. There is a wide variety of things you can do with the scraped data, from analysis to automated bots, and so on.

This will be our first python project! I will link some good introduction tutorials if you have no python practice at all. I will also go over some important syntax and examples to help you get ready to tackle this challenge! 

### Variables and Strings

`print("Hello World")` --> print strings directly
```
msg = "Hello World"     # assign the string to variable msg
print(msg)
```
```
first_msg = "Hello"
second_msg = "World"
print(first_msg + ' ' + second_msg)     # concatenate variables together with +

OR

print(f'{first_msg} {second_msg})   # f string syntax
```

### Lists and Dictionaries
Lists:
```food = ['pizza', 'chicken', 'eggs']
print(food[0]) --> prints 'pizza' or first element
print(food[1:]) --> prints ['chicken', 'eggs]
print(food[-1]) --> prints 'eggs' (last element)

empty_list = []
item_one = "item1"
item_two - "item2"
empty_list.append(item_one)     # append items to list
empty_list.append(item_two)
print(empty_list) --> list is now not empty!
```

Dictionaries:
```
alien = {
    'color': 'green',
    'health': 100,
    'swag': 100
}
print("the alien's color is alien['color']) --> prints the *value* from a key reference

dictionaries are made up of a key value pair, in this
case, the alien's color was the key, and to obtain
the value, 'green', we reference 'color'
```

### Conditionals
```
equals --> x == 42
not equal --> x != 42
greater than / equal to --> x > 42 // x >= 42
less than / equal to --> x < 42 // x <= 42

with lists:
'pizza' in food
'hotdogs' not in food
```

### Loops
For loops
``` 
my_list - [1,2,3,4,5,6,7]
for num in my_list:
    print(num)

>> 1234567 (on separate lines)
```

While loops
```
i = 0
while i < 10:
    print(i)
    i += 1

>> 123456789 (on separate lines)
```

Great! Now you have the basic syntax down, and our buddy Stack Overflow will always be there for us to ask questions if you have them. Now we will be going over some basic usage for the libraries we are using: **Beautiful Soup**, **Requests**, and **Pandas**. Don't worry, the focus will be on beautiful soup with a couple lines used from the others. 

Beautiful Soup with requests:
```
from bs4 import BeautifulSoup as bs

page = requests.get('enter_url_here.com')
soup = bs(page.content, 'html.parser')  # we are parsing the html elements within a webpage

# We can find elements by there tag:

soup.find_all('ul') --> will find all unordered lists on the webpage, 
                        and the content that is considered their children
```

One thing we have to rely on while working with bs4 is the devtools in our browser. It allows us to see the underlying skeleton of the webpage, and helps us identify which tags we need to obtain certain data.

Docs for Beautiful Soup are here: https://www.crummy.com/software/BeautifulSoup/bs4/doc/

And requests: https://2.python-requests.org/en/master/

And Pandas (although not needed necessarily for this project): https://pandas.pydata.org/pandas-docs/stable/

### Your Task:

1. After you finish reading through this guide, visit the documentation to get an understanding how to use things

2. Install all dependencies:
    ```
    pip install bs4
    pip install pandas
    https://pip.pypa.io/en/stable/installing/
    ^ if you do not have pip installed on machine
    ```

3. create 3 functions:
* One that gets the roster of a team
* Two that get different types of stats
* Convert to csv file (Extra credit)

We will be using https://www.sports-reference.com/ for sports stats. They allow web scraping and have very easy-to-follow web elements.

Good luck and happy coding!