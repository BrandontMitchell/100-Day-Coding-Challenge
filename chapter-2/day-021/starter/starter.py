from bs4 import BeautifulSoup as bs 
import requests 
import pandas as pd 


def get_roster(team):
    '''
        generate a 40 man roster with the following features:
        player name, uniform #, Position, age, bats, throws, 
        height, weight, date of birth, and first year played
    '''
    pass


def get_batting_stats(team):
    '''
        generates team batting stats over last 40 or so
        years. features to add are Wins (W), Losses (L), 
        Runs (R), Hits (H), Doubles (2B), Triples (3B), Homeruns (HR),
        Runs batted in (RBI), Strike outs (SO), Walks (BB), 
        batting average, on base percentage, slugging percentage
    '''
    pass


def get_pitching_stats(team):
    '''
        generates team pitching stats over last 40 or so
        years. features to include are wins (W), losses (L), 
        runs allowed per game, earned run avg, games (G), complete games (CG),
        Innings pitched (IP), whip, and fielding percentage 
    '''
    pass
