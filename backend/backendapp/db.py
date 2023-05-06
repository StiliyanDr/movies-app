import os

from flask import g
import pymongo


def get_db():
    """
    Establishes a MongoDB connection, associates it with the current
    request and returns the movies_db database of the connection.

    The connection is reused throughout the request's lifetime.
    """
    if "db" not in g:
        g.client = pymongo.MongoClient(os.environ["MONGO_URI"])
        g.db = g.client.movies_db

    return g.db


def close_db(e=None):
    """
    Closes the DB connection associated with the current request.
    """
    if "db" in g:
        client = g.pop("client")
        g.pop("db")
        client.close()


def init_app(app):
    app.teardown_appcontext(close_db)
