# Day 031 - Using twitter with python

Here we will be exploring the beautiful library `tweepy`! Here we do a bit of sentiment analysis on trump's tweets, to determine how stock market prices will be altered. 

This is one of my favorite libraries because of how many different paths and projects you can continue after learning some of its syntax.

### Setup

* setup is kind of complicated, so please follow carefully, or look into how to setup tweepy python
* First, I recommend creating a project or random account on twitter so this doesn't accidentally mess with your personal account!
* Import the tweepy package, Set the authentication     credentials, Create a new tweepy.API object, Use        the api object to call the Twitter API
1. visit https://developer.twitter.com/ and chose your account
2. agree to all the requirements, and specify why you need an api key/secret etc. 
3. create an application (name, desc, url (if necessary), and why you will use it)
4. create the auth credentials


### Your Task:

1. After you finish reading through this guide, visit the documentation to get an understanding how to use things

2. Install all dependencies:
    ```
    pip install tweepy
    https://pip.pypa.io/en/stable/installing/
    ^ if you do not have pip installed on machine
    ```

3. follow along in the code comments to continue!

We will be using https://www.sports-reference.com/ for sports stats. They allow web scraping and have very easy-to-follow web elements.

Good luck and happy coding!