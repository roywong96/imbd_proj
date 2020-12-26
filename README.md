# imbd_proj
IMDB ratings project 


## References:

Tools used for scraping with the help of Beautiful Soup from [Joseph Cowell Project 2](https://github.com/josephpcowell/cowell_proj_2/tree/master/helper_functions)<br/>
**Python Version:** 3.8<br/>
**Scraper Article:** https://towardsdatascience.com/scraping-tv-show-epsiode-imdb-ratings-using-python-beautifulsoup-7a9e09c4fbe5<br/>



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
