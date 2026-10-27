import csv

from fastapi import FastAPI

app = FastAPI()

#ZAD 2 i 3 (modele danych)
class Movie:
    def __init__(self, movie_id: str, title: str, genres: str):
        self.id = movie_id
        self.title = title
        self.genres = genres

class Link:
    def __init__(self, movie_id: str, imdbId: str, tmdbId: str):
        self.id = movie_id
        self.imdbId = imdbId
        self.tmdbId = tmdbId

class Rating:
    def __init__(self, user_id: str, movie_id: str, rating: str, timestamp: str):
        self.userId = user_id
        self.id = movie_id
        self.rating = rating
        self.timestamp = timestamp

class Tag:
    def __init__(self, user_id: str, movie_id: str, tag: str, timestamp: str):
        self.userId = user_id
        self.movieId = movie_id
        self.tag = tag
        self.timestamp = timestamp

#ZAD 1 (zwracanie hello world)
@app.get("/")
def read_root():
    return {"Hello": "World"}

#ZAD 2 (endpoint /movies)

@app.get("/movies")
def get_movies():
    movies_list = []
    with open("movies.csv", mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            movie_id = row.get("movieId")

            movie = Movie(
                movie_id = movie_id,
                title=row["title"],
                genres=row["genres"]
            )

            movies_list.append(movie.__dict__)
    return movies_list

#ZADANIE 4
@app.get("/links")
def get_links():
    links_list = []
    with open("links.csv", mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            link = Link(
                movie_id = row.get("movieId", ""),
                imdb_id = row.get("imdbId", ""),
                tmdb_id = row.get("tmdbId", "")
            )

            links_list.append(link.__dict__)
    return links_list