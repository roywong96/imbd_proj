#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 13:42:21 2020

@author: roywong
"""

# Libraries for data extraction and visualisation
import pandas as pd
import ast


# Import DataFrame
df_2000 = pd.read_csv("/Users/roywong/Desktop/Work_Stuff/PythonPortfolio/10.web_imdb_data/dataset/movie_2000.csv")


# renaming some columns
df_2000.rename(columns = {'movie title':'Title', 'imdb rating':'Ratings', 
                              'imdb raters':'Raters', 'director':'Directors',
                              'country':'Country', 'language':'Language',
                              'release date':'Date', 'runtime (min)':'Durations',
                              'mpaa':'MPAA', 'writer':'Writers',
                              'stars':'Actors', 'budget':'Budget',
                              'production companies':'Studios',
                              'opening weekend':'Openning Weekend',
                              'gross usa':'Gross USA'}, inplace = True) 


# missing values
df_2000.isnull().sum()


# Check for NaN values
df_2000.loc[df_2000['Directors'].isna()]

# fill missing directors
df_2000.loc[58,'Directors'] = 'Peter Ramsey' 
df_2000.loc[321,'Directors'] = 'Ron Clements'
df_2000.loc[401,'Directors'] = 'Byron Howard'
df_2000.loc[449,'Directors'] = 'Lana Wachowski'
df_2000.loc[463,'Directors'] = 'Frank Miller'
df_2000.loc[479,'Directors'] = 'Jeff Schaffer'
df_2000.loc[748,'Directors'] = 'Pete Docter'
df_2000.loc[860,'Directors'] = 'Brenda Chapman'
df_2000.loc[931,'Directors'] = 'Conrad Vernon'
df_2000.loc[1152,'Directors'] = 'Elizabeth Banks'
df_2000.loc[1312,'Directors'] = 'Pierre Coffin'
df_2000.loc[1606,'Directors'] = 'George Miller'
df_2000.loc[1663,'Directors'] = 'Ouentin Tarantino'
df_2000.loc[1803,'Directors'] = 'Tom McGrath'



# drop movies without the run time
df_2000.dropna(subset=['Durations'], inplace=True)
df_2000.dropna(subset=['Studios'], inplace=True)
# droping 'nan' dates 
df_2000.dropna(subset=['Date'], inplace=True)
# Drop movies without a rating
df_2000.dropna(subset=['Raters'], inplace=True)


# impute missing values for the 'Budget', 'Openning Weekend', 'Gross USA', 
# and 'cumulative worldwide'.
df_2000['Budget'] = df_2000['Budget'].fillna(df_2000['Budget'].median())
df_2000['Openning Weekend'] = df_2000['Openning Weekend'].fillna(df_2000['Openning Weekend'].median())
df_2000[ 'Gross USA'] = df_2000[ 'Gross USA'].fillna(df_2000[ 'Gross USA'].median())
df_2000['cumulative worldwide'] = df_2000['cumulative worldwide'].fillna(df_2000['cumulative worldwide'].median())


#genre parsing
df_2000.genres = df_2000.genres.apply(lambda x : ast.literal_eval(x))
#stars parsing
df_2000.Actors = df_2000.Actors.apply(lambda x : ast.literal_eval(x))
#production company parsing
df_2000.Studios = df_2000.Studios.apply(lambda x : ast.literal_eval(x))

#df_2000.to_csv('movies_genres_unchanged.csv', index=False)


'''
All Genres Has Turned into New features for Movies
'''

# Getting distinct genre types for generating columns of genre type.
genre_columns = list(set([j for i in df_2000['genres'].tolist() for j in i]))


# Iterating over every list to create and fill values into columns.
for j in genre_columns:
    df_2000[j] = 0
for i in range(df_2000.shape[0]):
    for j in genre_columns:
        if(j in df_2000['genres'].iloc[i]):
            df_2000.loc[i,j] = 1


# remove mpaa
df_2000.drop('MPAA', inplace=True, axis=1)


# changing the datetime format
df_2000['Date'] = pd.to_datetime(df_2000['Date'])

# extracting the year 
df_2000['Year'] = pd.DatetimeIndex(df_2000['Date']).year
df_2000['Month'] = pd.DatetimeIndex(df_2000['Date']).month


# year since release
from datetime import datetime
date = pd.to_datetime(datetime.now().date())
df_2000['Years_Since_Release'] = df_2000['Date'].apply(lambda x: (((date-pd.to_datetime(x))).days/365.25))



# rearrange by year
df_2000.sort_values(by=['Year'], ascending=False)

      
df_2000.dropna(subset=['genres'], inplace=True)

# drop the genres column
df_2000.drop('genres', inplace=True, axis=1)


df_2000.Durations = df_2000.Durations.astype(int)
df_2000.Year = df_2000.Year.astype(int)
df_2000.Comedy = df_2000.Comedy.astype(int)
df_2000.Action = df_2000.Action.astype(int)
df_2000.Thriller = df_2000.Thriller.astype(int)
df_2000.Fantasy = df_2000.Fantasy.astype(int)
df_2000.Drama = df_2000.Drama.astype(int)
df_2000.Western = df_2000.Western.astype(int)
df_2000.Biography = df_2000.Biography.astype(int)
df_2000.Mystery = df_2000.Mystery.astype(int)
df_2000.Musical = df_2000.Musical.astype(int)
df_2000.War = df_2000.War.astype(int)
df_2000['Sci-Fi'] = df_2000['Sci-Fi'].astype(int)
df_2000.Sport = df_2000.Sport.astype(int)
df_2000.Music = df_2000.Music.astype(int)
df_2000.Horror = df_2000.Horror.astype(int)
df_2000.Crime = df_2000.Crime.astype(int)
df_2000.Adventure = df_2000.Adventure.astype(int)
df_2000.Family = df_2000.Family.astype(int)
df_2000.Animation = df_2000.Animation.astype(int)
df_2000.History = df_2000.History.astype(int)
df_2000.Romance = df_2000.Romance.astype(int)


df_2000.Year.dtypes



# save the dataframe
df_2000.to_csv('eda_data.csv', index=False)

