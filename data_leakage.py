#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 19:10:26 2020

@author: roywong
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression

df = pd.read_csv('/Users/roywong/Desktop/Work_Stuff/PythonPortfolio/10.web_imdb_data/eda_data.csv')

df.isnull().sum()

# choose relevant  columns
df.columns


df_model = df[['Ratings', 'Raters', 'Directors',
           'Country', 'Language', 'Budget', 'Openning Weekend',
           'Gross USA', 'Durations', 'Romance',
           'Horror', 'Music', 'Fantasy', 'Mystery', 'Sci-Fi', 'Biography',
           'Family', 'Drama', 'Sport', 'History', 'Thriller', 'Animation',
           'Adventure', 'Crime', 'Musical', 'Western', 'War', 'Action', 'Comedy',
           'Year', 'Month']]


# get dummy variables
df_dum = pd.get_dummies(df_model)

# train test split
from sklearn.model_selection import train_test_split

X = df_dum.drop('Ratings', axis = 1)
y = df_dum.Ratings.values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)



# multiple linear regression
import statsmodels.api as sm

X_sm = X = sm.add_constant(X)
model = sm.OLS(y, X_sm)
model.fit().summary()


# linear Regression
from sklearn.linear_model import LinearRegression, Lasso, Ridge, RidgeCV
from sklearn.model_selection import cross_val_score

lm = LinearRegression()
reg = lm.fit(X_train, y_train)
reg.score(X_train, y_train)


# results
## 0.8751018683244058
### result of the target was leaking into the model