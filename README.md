# IMBD Ratings Predictor: Project Overview

- Created a tool that predicts movie ratings from the imbd website
- Scraped over 2000 movies from imbd website using Python and Beautiful Soup
- Engineered features from the genres to quatify the value for each genre such as drama, action, thriller, comedy, romance and so forth.
- Optimized Linear, Lasso, Bayesian Ridge and Random Forest Regressor using GridSearchCV to reach the best model.
- A deep dive into data leakage to prevent target from leaking into models I chose for an accurate prediction.
- Evaluated the models using Mean Absolute Error for simplicity.


## References:
**Python Version:** 3.8<br/>
**Packages:** numpy, pandas, seaborn, matplotlib, Beautiful Soup, pickle <br/>
**Scraper Github:**  [Joseph Cowell Project 2](https://github.com/josephpcowell/cowell_proj_2/tree/master/helper_functions)<br/>
**Scraper Article:** https://towardsdatascience.com/scraping-tv-show-epsiode-imdb-ratings-using-python-beautifulsoup-7a9e09c4fbe5<br/>
**Regression Article:** [Are low R-Squared Values always a Problem?](https://statisticsbyjim.com/regression/interpret-r-squared-regression/)<br/>
**Data Leakeage Article** [Data Leakage in Machine Learning](https://towardsdatascience.com/data-leakage-in-machine-learning-6161c167e8ba)<br/>



# Web Scraping

Tweaked the web scraper github repo (above) to scrape 2000 movies from imdb.com. With each movie, we obtained the following:

- movie title
- imdb rating
- imdb raters
- mpaa
- genres
- director
- writer
- stars
- country
- language
- release date
- budget
- opening weekend
- gross usa
- cumulative worldwide
- production companies
- runtime (min)


# Data Cleaning
After scraping the data, I needed to clean it up so that it was usable for our model. I made the following changes and created the following variables:

- Renaming the columns
- Removing movies without production companies
- Creating a column for the release year of each movies
- Dropping movies wihout ratings. Movies without ratings means that it does not have raters. Hence, movies without raters have been removed as well.
- Removed the MPAA columns since there are too many missing values and filling in the MPAA would be inaccurate.
- Impute missing values for {'Budget', 'Openning Weekend', 'Gross USA', 'cumulative worldwide'} with median.
- Made columns for if different genres for each movie where some movies have combinations of genres as given below represented as binary:
  - Comedy
  - Action
  - Thriller
  - Fantasy
  - Drama
  - Western
  - Biography
  - Mystery
  - Musical
  - War
  - Sci-Fi
  - Sport
  - Music
  - Horror
  - Crime
  - Adventure
  - Family
  - Animation
  - History
  - Romance

# Exploratory Data Analysis

![](https://github.com/roywong96/imbd_proj/blob/master/images/actors.png)
![](https://github.com/roywong96/imbd_proj/blob/master/images/genres.png)
![](https://github.com/roywong96/imbd_proj/blob/master/images/genres20years.png)

Full Notebook can be view [here](https://jovian.ai/roywong96/imdb-eda)


# Model Building
First, I transformed the categorical variables into dummy variables. I also split the data into train and tests sets with a test size of 20%.


I tried several different models and evaluated them using Mean Absolute Error. I chose MAE because it is relatively easy to interpret and outliers aren’t particularly bad in for this type of model.


Models I tried using Scikit learn are:

- **Multiple Linear Regression:** Baseline for the model
- **Lasso Regression:** Because of the sparse data from the many categorical variables in genres, I thought a normalized regression like lasso would be effective.
- **Bayesian Ridge:** Chosen with regards to the sparsity of the data and ideal for dealing with data containing multiple outliers.
- **Random Forest Regressor:** With the sparsity of data, I assume that it would be a good fit

Full Notebook for Model Building can be view [here](https://jovian.ai/roywong96/imdb-model-building)

# Model Performance

So far, The Random Forest model far outperformed the other approaches on the test and validation sets.


- **Linear Regression Model:** MAE= 0.558
- **Lasso Regression Model:** MAE= 0.540
- **Bayesian Ridge Regression Model:** MAE= 0.541
- **Random Forest Model:** MAE= 0.505
- **Average Random Foreest and Linear Regression:** MAE= 0.515

# Regression Analysis

Based on the regression model, the R-squared is found to 0.426 which is seemingly low. However, it is not necessarily bad as studies that try to explain human behavior generally have R<sup>2</sup> values less than 50%. People are just harder to predict than things like physical processes. Article related to this explanation can be found in the references above.


# Exploration into Data Leakage

Throughout the modeling, it is found that the model I chose has been performing a little too well when adding in Directors and Writers to the model which gives an R<sup>2</sup> = 0.875.

Hence, after researching several articles regarding data leakage, it is obvious that the target is leaking into the model which destroyed the purpose of predictions.

