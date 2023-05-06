import os

from flask import g
import pymongo


def get_db():
    if "db" not in g:
        g.client = pymongo.MongoClient(os.environ["MONGO_URI"])
        g.db = g.client.movies_db

    return g.db


def close_db(e=None):
    if "db" in g:
        client = g.pop("client")
        g.pop("db")
        client.close()


def init_app(app):
    app.teardown_appcontext(close_db)
