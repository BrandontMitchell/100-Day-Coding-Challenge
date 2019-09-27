# Day 028 - Introduction to GUIs

The purpose of this day is to understand and appreciate the simple, yet challenging projects that involve Graphical User Interfaces (GUIs). In this section, we will create two applications:  A basic arithmatic calculator, and a weather app that calls an api (openweather). These sound easy, but the fun is in creating something aesthetic *and* functional. 

### Tkinter Walk Through

Let's get an idea on how tkinter works. 
First we import that library at the top, this has already been done in the starter code. Next, we initialize a **root** widget `.Tk()`, so that we can have access to all widgets. There can only be one *root* or *master* widget in our file/project. Next we create a `Label`, referencing our *master* with the text "Hello World!". After we construct this, we call `.pack()` which will fit the label to the size of the window. Then finally, we run our `mainloop()`. 
```
from tkinter import *   #import tkinter module


master = tkinter.Tk()
msg = tkinter.Label(master, text="Hello World!")
msg.pack()
master.mainloop()
```

## Common Tkinter Widgets 

### For calculator:
`Button` and `Text` is all we will be using. Let me give you an example of this:

```
def createButton(self):
    self.btn = Button(master, text="This is a button", width=5, height=5, bg='black', fg='white', command=print("Button Clicked"))
```

`bg` = background color
`fg` = foreground color
`command` = What will the button do on click?


Here is a rough draw.io mockup of the app
![](calc.png)

### TODO:
1. Create the layout with numbers and a text field for user input
2. Add functionality for each button press, you may find this becomes repetitive (maybe extra credit is to refactor this nicely!)
3. Update the text after each button press
4. Evaluate the text box on click of the `=`
5. I am only asking for you to include +, -, /, and * in this app! 
6. EXTRA CREDIT: add colors, add more operations (%, log, square root, etc.)



### For Weather App:
This one is a little bit more challenging! Here we utilize the `requests` library and make some api calls to https://openweathermap.org/api

In the starter code, you will see a couple imports:
`requests` --> to call our api
`tkinter` --> to build GUI
`json` --> to prettify our data
`datetime` --> to prettify utc to local time

There are a lot of similar features here from the calculator app. It will roughly look like this: consisting of 2 input fields, one for city and state --> (ex: Seattle,WA), and one for zip --> (ex: 98020). After the button click with one of those inputs filled, the bottom part of the GUI will update with the respective data necessary: 

![](weather.png)
### TODO:
1. Create an API key from https://openweathermap.org/api
2. Play around with `requests`, the only time we use this here is placed in the starter file. This API returns a json of all our necessary information for this project. 
3. Create the UI, with two inputs, two buttons, and a bottom text field to be filled up with data
4. Add functionality to buttons, by sending a request to the API after each click
5. Update the UI to respond to the request
6. EXTRA CREDIT: Add more data, add an icon based on weather conditions (i.e. sun if its hot out)