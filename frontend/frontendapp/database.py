import json
import logging
import os
import time
from types import MappingProxyType

import requests


_GENRES_URL = rf"http://{os.environ['DB_SERVICE']}/movies/genres"

_MOVIES_LISTING_URL = rf"http://{os.environ['DB_SERVICE']}/movies/all"

_MAX_RETRIES = 4

_HEADERS = MappingProxyType({"Content-Type": "application/json"})


def list_movie_genres():
    """
    :returns: a list of strs - all the genres of the available movies.
    """
    return _do_request(_GENRES_URL, default=[])


def _do_request(url, params=None, default=None):
    if (params is not None):
        params = json.dumps(params)

    for i in range(1, _MAX_RETRIES + 1):
        response = requests.get(url, data=params, headers=_HEADERS)

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
    m["plot"] = m.get("plot", "")
    m["genres"] = ", ".join(m.get("genres", []))
    m["cast"] = ", ".join(m.get("cast", []))
    m["poster"] = m.get("poster", "")
    m["title"] = m.get("title", "")
    m["year"] = m.get("year", 0)
    m["length"] = m.get("length", 0)

    imdb = m.pop("imdb")
    m["rating"] = (f"{imdb['rating']} ({imdb['votes']})"
                   if imdb is not None
                   else "")

    return m
