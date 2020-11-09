# The 500 Greatest Albums of All Time 
## An exercise of analysis of the database with extra information gathered using the Spotify and Wikipedia APIs

In an special issue of the American magazine Rolling Stone in 2003, it was presented a list with the top 500 albums of all time. This selection was made with the vote of rock stats, musical critics, and personalities from the industry. 

https://www.rollingstone.com/music/music-lists/500-greatest-albums-of-all-time-156826/

This forms a music database of albums of great quality. In this exercise of data visualization, I analzyed whether there are intrinsic features that make an album great. I decided to ckeck several musical features and checked wether in this list there is a trend in these features. This information is gathered using the Spotify API. Each track in each album have some metrics about danceability, energy, loudness, speechiness, acousticness, instrumentalness, liveness, valence and tempo, so I can check possible relations. 

In addition, I analyzed whether the top albums show different Wikipedia read metric according to its position. This can allow we to investidate if the knowledge interest based on the Wikipedia page view is correlated with the list position. I gathered this information using the Wikipedia API. 

## Data cleaning and improving the database

I obtained a CSV with the top 500 albums in the Kaggle website, through the following link:

https://www.kaggle.com/notgibs/500-greatest-albums-of-all-time-rolling-stone?select=albumlist.csv

I conducted some simple cleaning of this dataset to remove some bad characters, to divide different genre and subgenre into lists and remove all albums that aren't present in the Spotify catalogue.
