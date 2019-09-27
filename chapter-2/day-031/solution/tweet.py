import tweepy
import time
import json
import pandas as pd
import re
from textblob import TextBlob

    #######________DAY 1_______########

auth = tweepy.OAuthHandler("", 
    "")
auth.set_access_token("", 
    "")

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")


def show_timeline():
    timeline = api.home_timeline()
    for tweet in timeline:
        print(tweet)

def tweet(input):
    api.update_status(input)


def dox_user(username):
    user = api.get_user(username)
    print("User Details:")
    print()
    print(user.name, user.description, user.location)
    print()
    print("Most recent followers")
    for follower in user.followers():
        print(follower.name)


def add_friend(username):
    api.create_friendship(username)

    #######_______Day 2________########

def search_twitter(query):
    tweets = api.search(query)
    for tweet in tweets:
        json_str = tweet._json
        org_data(json_str)  

def org_data(data):
    tweet = data['text']
    user_obj = data['user']
    username = user_obj['screen_name']
    location = user_obj['location']
    date = data['created_at']

    data_dict = {
        'username': username,
        'tweet': tweet,
        'location': location,
        'date': date
    }
    df = pd.DataFrame(list(data_dict.items()))
    print(df)
    
######_______END DAY 2_______#########

def get_tweets(user):
    # We create a tweet list as follows:
    tweets = api.user_timeline(screen_name=user, count=200)
    print("Number of tweets extracted: {}.\n".format(len(tweets)))

    # We print the most recent 5 tweets:
    print("5 recent tweets:\n")
    for tweet in tweets[:5]:
        print(tweet.text)
        print(clean_tweet(tweet.text))
        print(analyze_tweet(tweet.text))
        print()

def clean_tweet(tweet):
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

def analyze_tweet(tweet):
    analysis = TextBlob(clean_tweet(tweet))
    if analysis.sentiment.polarity > 0:
        return 1
    elif analysis.sentiment.polarity == 0:
        return 0
    else:
        return -1

def conclusion(tweet):
    cleaned = clean_tweet(tweet)
    analyzed = analyze_tweet(cleaned)
    if analyzed == 1:
        return f'Tweet: {tweet} was ranked positive'
    elif analyzed == 0:
        return f'Tweet: {tweet} was ranked neutral'
    else:
        return f'Tweet: {tweet} was ranked negative... Watch out stock market!'

if __name__ == '__main__':
    # here we can search for keywords, then analyze the entire tweet to see specifics
    get_tweets("realDonaldTrump")