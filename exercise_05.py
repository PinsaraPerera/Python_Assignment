
class Movie:
    def __init__(self, title, genre, rating):
        self.title = title
        self.genre = genre
        self.rating = rating

class MovieDatabase:
    def __init__(self):
        self.movies = []
        self.unique_genres = set()

    def add_movie(self, movie):
        self.movies.append(movie)
        self.unique_genres.add(movie.genre) # add genre to the set of unique genres

    def sort_movies_by_rating(self):
        self.movies.sort(key=lambda x: x.rating, reverse=True) # sort the movies by rating in descending order
        return self.movies
    
    def search_movie_by_genre(self, genre):
        return [movie for movie in self.movies if movie.genre == genre] # create a list of movies with the given genre

# create some movie objects   
m1 = Movie("Harry Potter", "Fantasy", 8.1)
m2 = Movie("The Lord of the Rings", "Fantasy", 8.8)
m3 = Movie("Spider Man", "Action", 9.0)
m4 = Movie("Jonny English", "Comedy", 6.2)
m5 = Movie("The love", "Romance", 7.6)

# create a movie database object
movie_db = MovieDatabase()

# add the movies to the database
movie_db.add_movie(m1)
movie_db.add_movie(m2)
movie_db.add_movie(m3)
movie_db.add_movie(m4)
movie_db.add_movie(m5)

# sort the movies by rating
sorted_movies = movie_db.sort_movies_by_rating()
print("Movies sorted by rating:")
for movie in sorted_movies:
    print(f"{movie.title}: {movie.rating}")

# search for movies with the genre "Fantasy"
fantasy_movies = movie_db.search_movie_by_genre("Fantasy")
print("\nFantasy movies:")
for movie in fantasy_movies:
    print(f"{movie.title}: {movie.rating}")

# print the unique genres
print("\nUnique genres:")
for genre in movie_db.unique_genres:
    print(genre)