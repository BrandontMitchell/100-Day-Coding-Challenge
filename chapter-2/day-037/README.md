# Day 037 - Creating a voice assistant with python

The purpose of this day is to explore another cool library `pyttsx3` as in python text to speech version 3, built with many, many cool features!

### Overview:

1. `pyttsx3` has many things available, but we only have one day, so this will be limited. Feel free to explore their docs! (https://pyttsx3.readthedocs.io/en/latest/)
2. We will be creating a 'voice' assistant, but in reality we are just typing what the bot will say. We will separate these into separate functions.



### Guide:

1. To get the voice to responsd, we must first create an engine: `engine=pyttsx3.init()`, which initializes our engine so it can interpret and speak
2. We use `say` and `.runAndWait()` to interpret, and then run that say function. We can pass variables into the `say()` as well. The runandwait is required after every `say` to actually execute that speech. All we need to say to the engine is:
* `engine.say(TEXT_IN_HERE)`
* `engine.runAndWait()`
3. We will be using past lessons to create these functions, so have that code ready!


### Your Task:

1. After you finish reading through this guide, visit the documentation to get an understanding how to use things

2. Install all dependencies:
    ```
    pip install pyttsx3
    pip install yahoo_fin
    https://pip.pypa.io/en/stable/installing/
    ^ if you do not have pip installed on machine
    ```

3. Create some functions
* BTC price (api call to some public service)
* Weather (another api to openweathermaps)
* Stock index for a specific (or variable) stock
* Change voice (rate, volumne, and voice type)


Good luck and happy coding!]