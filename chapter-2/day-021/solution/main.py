# day 11  --> Automation with bs4 and csv

from bs4 import BeautifulSoup as bs 
import requests
import pandas as pd

# Scrape webpage for sports stats
    # Gather all players names for a specific team
    # Gather all stats for each player
    # export all data to csv file
    # prettify the csv file




def get_roster(team):
    '''gets a 40 man roster on input of specific team'''
    base_URL = 'https://www.baseball-reference.com/teams/'
    end_URL = '/2019-roster.shtml'
    page = requests.get(base_URL + team + end_URL)
    soup = bs(page.content, 'html.parser')

    roster = soup.find({'tbody'})
    roster = roster.find_all('tr')
    summary = {'player', 'uniform_number', 'POS', 'age', 'bats', 'throws', 'height', 'weight', 'date_of_birth', 'first_year'}
    summary_dict = {}
    df = pd.DataFrame()

    for player in roster:
        if player.find('th', {'scope': 'row'}) != None:
            for feature in summary:
                f = player.find('td', {'data-stat': feature}).get_text()
                summary_dict[feature] = [f]
            sd = pd.DataFrame.from_dict(summary_dict)
            df = df.append(sd)
        df.to_csv(f'{team}-40-man.csv', encoding='utf-8', index=False)
            

def get_batting_stats(team):
    '''gets year by year stats'''
    base_URL = 'https://www.baseball-reference.com/teams/'
    end_URL = '/batteam.shtml'
    page = requests.get(base_URL + team + end_URL)
    soup = bs(page.content, 'html.parser')

    years = soup.find({'tbody'})
    years = years.find_all('tr')
    summary = {'W', 'L', 'G', 'R', 'H', '2B', '3B', 'HR', 'RBI', 'SO', 'BB', 'batting_avg', 'onbase_perc', 'slugging_perc'}
    summary_dict = {}
    df = pd.DataFrame()

    for year in years:
        if year.find('th', {'scope': 'row'}) != None:
            
            for feature in summary: 
                print(feature)
                f = year.find('td', {'data-stat': feature}).get_text()
                print(feature, f)
                summary_dict[feature] = [f]
            sd = pd.DataFrame.from_dict(summary_dict)
            df = df.append(sd)
        df.to_csv(f'{team}-batting-stats.csv', encoding='utf-8', index=True)


def get_pitching_stats(team):
    '''gets year by year pitching stats'''
    base_URL = 'https://www.baseball-reference.com/teams/'
    end_URL = '/pitchteam.shtml'
    page = requests.get(base_URL + team + end_URL)
    soup = bs(page.content, 'html.parser')

    years = soup.find({'tbody'})
    years = years.find_all('tr')
    summary = {'W', 'L', 'runs_allowed_per_game', 'earned_run_avg', 'G', 'CG', 'IP', 'HR_p', 'BB_p', 'SO_p', 'fielding_perc', 'whip'}
    summary_dict = {}
    df = pd.DataFrame()

    for year in years:
        if year.find('th', {'scope': 'row'}) != None:
            
            for feature in summary: 
                print(feature)
                f = year.find('td', {'data-stat': feature}).get_text()
                print(feature, f)
                summary_dict[feature] = [f]
            sd = pd.DataFrame.from_dict(summary_dict)
            df = df.append(sd)
        df.to_csv(f'{team}-pitching-stats.csv', encoding='utf-8', index=True)

if __name__ == '__main__':
    team = input("What team do you want to analyze? ")
    get_roster(str(team))
    get_batting_stats(str(team))
    get_pitching_stats(str(team))