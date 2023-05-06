from flask import (
    Blueprint,
    request,
    url_for,
)

from backendapp import constants as const
from backendapp.db import get_db
from backendapp.models.moviesfilter import MoviesFilter


bp = Blueprint("movies", __name__, url_prefix="/movies")


@bp.route("/genres")
def list_genres():
    db = get_db()

    return db.movies.distinct("genres")


@bp.route("/")
def find_movies_paginated():
    """
    GET a list of movies, optionally filtering them.

    The results are paginated using the `page` parameter.
    """
    cursor = _find_movies_for(request)
    page = int(request.args.get("page", 1))
    cursor = _advance_cursor_to(page, cursor)
    total_movies = _get_total_movies_count()
    links = _pagination_links_for(page, total_movies)

    return {
        "movies": _to_json_list(cursor),
        "_links": links,
    }


def _find_movies_for(request):
    q = _build_query_for(MoviesFilter(**request.get_json()))
    db = get_db()

    return db.movies.find(q, const.MOVIES_PROJECTION)


def _build_query_for(filter):
    query = {}

    if (filter.title):
        query["title"] = filter.title

    if (filter.genres):
        query["genres"] = {"$all": filter.genres}

    if (filter.year is not None):
        query["year"] = {
            "$gte": filter.year[0],
            "$lte": filter.year[1]
        }

    if (filter.length is not None):
        query["length"] = {
            "$gte": filter.length[0],
            "$lte": filter.length[1],
        }

    return query


def _advance_cursor_to(page, cursor):
    return cursor.sort(
        list(const.PAGINATION_SORT)
    ).skip(
        (page - 1) * const.MOVIES_PER_PAGE
    ).limit(
        const.MOVIES_PER_PAGE
    )


def _get_total_movies_count():
    db = get_db()
    return db.movies.count_documents({})


def _pagination_links_for(page, total_movies):
    last_page = (total_movies // const.MOVIES_PER_PAGE) + 1
    links = {
        "self": {
            "href": url_for(
                "movies.find_movies_paginated",
                page=page,
                _external=True
            )
        },
        "last": {
            "href": url_for(
                "movies.find_movies_paginated",
                page=last_page,
                _external=True
            )
        },
    }

    if page > 1:
        links["prev"] = {
            "href": url_for(
                "movies.find_movies_paginated",
                page=page - 1,
                _external=True
            )
        }

    if page < last_page:
        links["next"] = {
            "href": url_for(
                "movies.find_movies_paginated",
                page=page + 1,
                _external=True
            )
        }

    return links


def _to_json_list(cursor):
    return [
        _replace_oid_with_hex_in(doc)
        for doc in cursor
    ]


def _replace_oid_with_hex_in(doc):
    doc["_id"] = str(doc["_id"])

    return doc


@bp.route("/all")
def find_movies():
    """
    GET a list of movies, optionally filtering them.

    The results are not paginated.
    """
    cursor = _find_movies_for(request)

    return _to_json_list(cursor)
