# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 11:59:16 2020

@author: MJ
"""

import pandas as pd
import numpy as np

movies = pd.read_csv('../datasets/movielens/movies.csv', sep=',')
print(type(movies))
movies.head()
tags = pd.read_csv('../datasets/movielens/tags.csv', sep=',')
tags.head(10)

ratings = pd.read_csv('../datasets/movielens/ratings.csv', sep=',', parse_dates=['timestamp'])
ratings.head()

# Borraremos la columna timestamp para el análisis inicial
del ratings['timestamp']
del tags['timestamp']


movies[2:20]['title']
movies['title']
movies[:20]['title']
movies[20:]['title']

movies.iloc[2:20]
movies.iloc[2:20]['title']


tag_counts = tags['tag'].value_counts()
tag_counts[:20]

tag_counts[5:15].plot(kind='bar', figsize=(5,5))

 movies["genres"].value_counts()[:20].plot(kind="bar",figsize=(10,5))
 
 ratings.head()
 
 
average_rating = ratings[['movieId','rating']].groupby('movieId').mean()
average_rating.head()

movie_count = ratings[['movieId','rating']].groupby('movieId').count()
movie_count.head()


movie_sum = ratings[['movieId','rating']].groupby('movieId').sum()
movie_sum.head()


ratings.hist(column='rating', figsize=(10,5))

ratings.boxplot(column='rating')

tag_counts[5:15].plot(kind='bar', figsize=(5,5))

 ratings.groupby('movieId').agg(np.mean)
 
 
 movies_ranting=ratings.groupby("movieId").agg({'rating':np.mean, 'movieId': np.size})

 
 
 movie_new = ratings.groupby('movieId').agg({'rating': [np.mean, np.size]})
 
 movie_new = ratings[['movieId', 'rating']].groupby('movieId').agg({'rating':np.mean, 'movieId': np.size})
  # ratings[['movieId', 'rating']].groupby('movieId').agg({'rating':"mean", 'movieId': "count"})
 
 
 movie_new = ratings.groupby('movieId').agg({'rating': {"mitja":np.mean, "lon":np.size}})
 
 movie_new = ratings.groupby(['movieId', 'rating']).agg({'rating': [np.mean, np.size]})
 

 
   
 new=ratings.groupby("rating").agg({'rating':{"mean": np.mean, "std": np.std}, 'movieId': np.size})
 new
 
 new=ratings.groupby("rating").agg({'rating':{"nom_mean": "mean", "nom_std": "std"}, 'movieId': np.size})
 new
 
 new.columns = new.columns.droplevel(0)
 
 
t = movies.merge(tags, on='movieId')
t.head()

avg_ratings= ratings.groupby("movieId", as_index=False).mean()
del avg_ratings['userId']
avg_ratings["rating"].round(2)
 
 avg_ratings.hist('rating')
 avg_ratings.groupby("rating").count().sort_values("movieId",ascending=False).head(20)
 
 #unimos peliculas y la media del rating,
 movies.count
 avg_ratings.count()
 #hay más peliculas que rating, nos quedaos con los que estan aen avg_ratins y movies
 #inner join, intersección
box_office = movies.merge(avg_ratings, on='movieId', how='inner')
box_office.tail()
box_office.count()

is_highly_rated = box_office['rating'] >= 4.0
box_office.count()

box_office[is_highly_rated][-5:]
 
is_comedy = box_office['genres'].str.contains('Comedy')

box_office[is_comedy][:5] 
 
 box_office[is_comedy & is_highly_rated][-5:]
 
 #dividir strings
 
 movie_genres = movies['genres'].str.split('|', expand=True)
 
 #Añadir una columna para indicar si la película es una Comedia
 movie_genres['isComedy'] = movies['genres'].str.contains('Comedy')
 
 
movies['year'] = movies['title'].str.extract('.*\(([0-9]+)\).*', expand=True)
 
average_rating = ratings[['movieId','rating']].groupby('movieId',as_index=False).mean()

joined = movies.merge(average_rating, on='movieId', how='inner')
joined.head()

yearly_average = joined[['year','rating']].groupby('year', as_index=False).mean()
yearly_average[-20:] 
 
yearly_average[-20:].plot(x='year', y='rating', figsize=(10,5), grid=True)

yearly_average[yearly_average['year'].str.contains('2009')]
#yearly_average[yearly_average['year'] =='2009']

 