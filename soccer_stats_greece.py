#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 09:35:47 2020

@author: stavros77
"""
#!/usr/local/bin/python

import pandas as pd
#import numpy as np
#import matplotlib as plt
#import seaborn as sns
name = __name__
print(f'File\'s name is {name}')



files = ['/home/stavros77/G1_2017_18.csv', '/home/stavros77/G1_2018_19.csv','/home/stavros77/G1_2019_20.csv']

while True:
    try:
        season = int(input('Enter a number between 0-2 in order to choose a season:'))
        if 0 <= season < 3:
            break
    except (ValueError, TypeError):
        print("Input isn't a valid entry" )

        
league_stats = pd.read_csv(files[season])
#stats = sns.load_dataset(files[season])
categories = list(league_stats.columns)
print("Group count of Home goals :")
print(league_stats['FTHG'].value_counts())
print("Group count of Away goals :")
print(league_stats['FTAG'].value_counts())
#print(len(categories))

home_season_goals = league_stats['FTHG'].value_counts()
#print(len(league_stats.columns))
print("Wins amd Draws in season :")
print(league_stats['FTR'].value_counts())
#team results and stats
Teams = league_stats.HomeTeam.unique()
total_teams = len(Teams)
print(f'Total teams :{total_teams}')

team_stats = league_stats.groupby(['FTR'])
### print(team_stats[['HS','AS']].value_counts())

while True:
    try:
        val = (int(input(f"enter a value between 1 and {total_teams}.")) -1)
        if 0 <= val < total_teams:
            break
    except (ValueError, TypeError):
        print('try to enter a new valid value!!!')
        
print(Teams[val])
filt = (league_stats['HomeTeam'] == Teams[val]) | (league_stats['AwayTeam'] == Teams[val])

results = league_stats.loc[filt]
print(results[['HomeTeam','FTHG','AwayTeam','FTAG']])
###  league_stats['total_goals'] = league_stats['FTHG'] + league_stats['FTAG']



#league_stats.add(league_stats['total_goals'], inplace=True)
#print(league_stats['total_goals'])
#### league_stats['total_goals'].plot()

#plot goals


#sns.relplot(x='Date',y='FTR'. data=stats)
league_stats.hist(column=['FTHG', 'FTAG'], legend=True)
results[['FTHG','FTAG']].plot(marker='o')
results[['B365>2.5','B365<2.5']].plot()
league_stats.hist(column=['B365>2.5','B365<2.5'], bins=4, legend=True)
#  home_season_goals.hist(subplot=True)


#results['HS'].plot()