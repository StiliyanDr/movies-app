import logging
import os
import time

import requests


_GENRES_URL = f"{os.environ['DB_SERVICE']}/movies/genres"

_MOVIES_LISTING_URL = f"{os.environ['DB_SERVICE']}/movies/all"

_MAX_RETRIES = 4


def list_movie_genres():
    """
    :returns: a list of strs - all the genres of the available movies.
    """
    return _do_request(_GENRES_URL, default=[])


def _do_request(url, params=None, default=None):
    for i in range(1, _MAX_RETRIES + 1):
        response = requests.get(url, params)

        if (response.status_code == requests.codes.ok):
            return response.json()
        else:
            logging.error(
                f"'{url}' returned {response.status_code} at "
                f"try {i}: {response.text}"
            )
            time.sleep(2 << i)

    return default


def list_movies(title=None,
                genres=None,
                length=None,
                year=None):
    """
    Lists movies that conform to the criteria defined with the optional
    arguments described below.

    :param title: a str - a title to match.
    :param genres: a list of strs - allowed genres.
    :param length: a two-element list of ints representing an interval
    [a, b] of allowed movie length (in minutes).
    :param year: a two-element list of ints representing an interval
    [a, b] of allowed movie year.
    :returns: a list of movie documents (dicts).
    """
    params = _params_for(title, genres, length, year)
    movies = _do_request(_MOVIES_LISTING_URL, params, default=[])

    return _transform(movies)


def _params_for(title, genres, length, year):
    params = {}

    if (title is not None):
        params["title"] = title

    if (genres is not None):
        params["genres"] = genres

    if (length is not None):
        params["length"] = length

    if (year is not None):
        params["year"] = year

    return params


def _transform(movies):
    return [
        _transform_fields_of(m)
        for m in movies
    ]


def _transform_fields_of(m):
    imdb = m.pop("imdb")
    m["rating"] = f"{imdb['rating']} ({imdb['votes']})"
    m["genre"] = ", ".join(m["genre"])
    m["cast"] = ", ".join(m["cast"])

    return m
