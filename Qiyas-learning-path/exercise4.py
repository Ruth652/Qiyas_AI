from functools import reduce
# =====================================================
# Exercise 4: Movie Rating Analysis System
# =====================================================

movies = [
    ("Inception", 8.8),
    ("Titanic", 7.9),
    ("Avatar", 8.1),
    ("Batman", 6.5),
    ("Joker", 9.0),
    ("Frozen", 5.9)
]


def highest_rated_movie(movie_list):
    """
    Return highest rated movie.
    """

    return max(m[1] for m in movies)


def lowest_rated_movie(movie_list):
    """
    Return lowest rated movie.
    """
    return min(m[1] for m in movies)


def average_rating(movie_list):
    """
    Calculate average movie rating.
    """
    return reduce(lambda total, m: m[1] + total, movie_list, 0) / len(movie_list)


def movies_above_8(movie_list):
    """
    Use filter() to return movies above 8.0.
    """
    avg_ = average_rating(movie_list)
    return list(filter(lambda m: m[1] > avg_, movie_list))


def sort_movies(movie_list):
    """
    Sort movies by rating descending.
    """
    return sorted(movie_list, key=lambda m:m[1])


def process_ratings(movie_list):
    """
    Square ratings above 7.
    Cube ratings below 7.
    """
    return [m[1] ** 3 if m[1] % 2 else m[1] ** 2 for m in movie_list]


def add_rating_bonus(movie_list):
    """
    Add 0.5 bonus rating using map().
    """
    return list(map(lambda m: (m[0], m[1] + 0.5), movie_list))




print("highest_rated_movie",highest_rated_movie(movies))
print("lowest_rated_movie",lowest_rated_movie(movies))
print("average_rating",average_rating(movies))
print("movies_above_8",movies_above_8(movies))
print("sort_movies",sort_movies(movies))
print("process_ratings",process_ratings(movies))
print("add_rating_bonus",add_rating_bonus(movies))