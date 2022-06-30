import csv

from cs50 import SQL

open("assignment.db","w").close()

db = SQL("sqlite///assignment.db")

db.execute("CREATE TABLE movies(movie_id INTERGER, movie TEXT, PRIMARY KEY(movie_id)")
db.execute("CREATE TABLE movie_genre(movies_id INTEGER, genre_id INTEGER, PRIMARY KEY(genre_id), FOREIGN KEY(movies_id) REFERENCES movies(id))")
db.execute("CREATE TABLE genre (genre_id INTEGER, genre TEXT, PRIMARY KEY(genre_id), FOREIGN KEY(genre_id) REFERENCES movie_genre(genre_id))")

with open("gross movies.csv", "r") as file:
    reader=csv.DictReader(file)

    for row in reader:
        title=row["Film"].strip().capitalize()
        id=db.execute("INSERT INTO movies(title) VALUES(?)",title)

        for Genre in row["Genre"].split(","):
            genre=Genre.capitalize().strip()


            genre_id=db.execute("INSERT INTO movie_genre(movies_id) VALUES((SELECT id FROM movies WHERE title=?))",title)
            
            db.execute("INSERT INTO genre(genre_id,genre) VALUES ((SELECT genre_id FROM movie_genre WHERE movies_id=?),?)",genre_id,genre)
