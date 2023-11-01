from flask_sqlalchemy import SQLAlchemy
from src.models import db, Movie


class MovieRepository:

    def get_all_movies(self):
        # TODO get all movies from the DB
        movie = Movie.query.all()
        # db.session.query(Movie).all()
        return movie

    def get_movie_by_id(self, movie_id):
        # TODO get a single movie from the DB using the ID
        movie = Movie.query.get(movie_id)
        return movie

    def create_movie(self, title, director, rating):
        # TODO create a new movie in the DB
        new_movie = Movie(title=title, director=director, rating=rating)
        db.session.add(new_movie)  # Add the new movie to the session
        db.session.commit()
        return new_movie

    def search_movies(self, title):
        # TODO get all movies matching case insensitive substring (SQL LIKE, use google for how to do with SQLAlchemy)
        movies = Movie.query.filter(Movie.title.ilike(f"%{title}%")).all()  # Use SQLAlchemy's ilike for case-insensitive search
        return movies


# Singleton to be used in other modules
movie_repository_singleton = MovieRepository()
