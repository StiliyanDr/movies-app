import datetime as dt


MOVIES_TABLE_COLUMNS = [
    "title",
    "year",
    "length",
    "rating",
]

MOVIES_TABLE_HIDDEN_COLUMNS = [
    "id",
    "image_path",
]

MOVIES_TABLE_PAGE_SIZE = 15

MAX_MOVIE_LENGTH_MINS = 4 * 60

MIN_MOVIE_YEAR = 1800

MAX_MOVIE_YEAR = dt.date.today().year
