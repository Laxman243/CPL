import pandas as pd
import csv,io
from scipy import sparse


ratings = pd.read_csv("C:/Users/vshuk/Desktop/CPL/DjangoProject/mac/dataset/ratings.csv")
movies = pd.read_csv('C:/Users/vshuk/Desktop/CPL/DjangoProject/mac/dataset/movies.csv')
ratings = pd.merge(movies,ratings).drop(['genres','timestamp'],axis=1)
# print(ratings.shape)
ratings.head()
# print(movies)
# print(ratings)

# ratings
userRatings = ratings.pivot_table(index=['userId'],columns=['title'],values='rating')
userRatings.head()
# print("Before: ",userRatings.shape)
userRatings = userRatings.dropna(thresh=10, axis=1).fillna(0,axis=1)
#userRatings.fillna(0, inplace=True)
# print("After: ",userRatings.shape)


corrMatrix = userRatings.corr(method='pearson')
corrMatrix.head(100)

def get_similar(movie_name,rating):
    similar_ratings = corrMatrix[movie_name]*(rating-2.5)
    similar_ratings = similar_ratings.sort_values(ascending=False)
    #print(type(similar_ratings))
    return similar_ratings


romantic_lover = [("(500) Days of Summer (2009)",5),("Alice in Wonderland (2010)",3),("Aliens (1986)",1),
                  ("2001: A Space Odyssey (1968)",2)]
similar_movies = pd.DataFrame()
for movie,rating in romantic_lover:
    similar_movies = similar_movies.append(get_similar(movie,rating),ignore_index = True)

similar_movies.head(10)
# print("laxman")
# df = get_similar("Toy Story (1995)",5)
# print(df)

