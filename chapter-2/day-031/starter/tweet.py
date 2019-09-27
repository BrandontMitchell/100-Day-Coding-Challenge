#tweepy right? for the library
import tweepy
import time
import json
import pandas as pd
import re
from textblob import TextBlob

    #######________DAY 1_______########

auth = tweepy.OAuthHandler("CONSUMER_KEY", 
    "CONSUMER_SECRET")
auth.set_access_token("ACCESS_TOKEN", 
    "ACCESS_TOKEN_SECRET")

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")


def show_timeline():
    '''show timeline for your own feed'''

def tweet(input):
    '''create a tweet here with an input'''


def dox_user(username):
    '''dox a specific user (as much as twitter would allow...)
        include: name, username, location, description, and most recent tweets'''


def add_friend(username):
    '''add a friend! (by username)'''

    #######_______Day 2________########

def search_twitter(query):
    '''search twitter based on a string query (i.e. search on search bar)''' 

def org_data(data):
    '''create a data object and organize it with a pandas dataframe!'''
    
######_______END DAY 2_______#########

def get_tweets(user):
    '''get top 5 most recent tweets from a user'''


def clean_tweet(tweet):
    '''here's how we will clean the tweets using regex!'''
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

def analyze_tweet(tweet):
    analysis = TextBlob(clean_tweet(tweet))
    if analysis.sentiment.polarity > 0:
        return 1
    
    #TODO:
        # what other polarities could we have?

def conclusion(tweet):
    '''conclude what you have found with some nice printing and polarity checking!'''

if __name__ == '__main__':
    # here we can search for keywords, then analyze the entire tweet to see specifics
    get_tweets("realDonaldTrump")