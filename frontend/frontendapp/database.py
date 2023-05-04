
def list_movie_genres():
    return [
        "Comedy",
        "Drama",
        "Thriller",
    ]


def list_movies(title, genres, length, year):
    return [{
        "title": "Titanic",
        "year": 1997,
        "length": 194,
        "rating": "7.7 (716392)",
        "id": 0,
        "image_url": r"https://m.media-amazon.com/images/M/MV5BMDdmZGU3NDQtY2E5My00ZTliLWIzOTUtMTY4ZGI1YjdiNjk3XkEyXkFqcGdeQXVyNTA4NzY1MzY@._V1_SY1000_SX677_AL_.jpg",
        "plot": "A seventeen-year-old aristocrat falls in love with a kind, but poor artist aboard the luxurious, ill-fated R.M.S. Titanic.",
        "cast": ", ".join([
           "Leonardo DiCaprio",
           "Kate Winslet",
           "Billy Zane",
           "Kathy Bates"
        ]),
        "genre": ", ".join([
            "Drama",
            "Romance"
        ]),
    }]
