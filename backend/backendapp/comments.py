import datetime as dt
import urllib.parse

from bson.objectid import ObjectId
from flask import (
    Blueprint,
    request,
)

from backendapp import constants as const
from backendapp.db import get_db
from backendapp.models.comment import Comment
from backendapp.models.objectid import PydanticObjectId


bp = Blueprint("comments", __name__, url_prefix="/comments")


@bp.route("/<string:movie_id>")
def list_comments_for_movie(movie_id):
    hex_id = urllib.parse.unquote(movie_id)
    db = get_db()

    cursor = db.comments.find({"movie_id": ObjectId(hex_id)},
                              const.COMMENTS_PROJECTION)

    return [_comment_to_json(c) for c in cursor]


def _comment_to_json(doc):
    doc["name"] = doc.get("name", "-")
    doc["text"] = doc.get("text", "")
    date = doc.get("date")
    doc["date"] = (date.strftime(const.COMMENTS_DATE_FORMAT)
                   if (date is not None)
                   else "-")

    return doc


@bp.route("/", methods=["POST"])
def add_comment():
    comment = _create_comment_for(request.get_json())
    db = get_db()
    insert_result = db.comments.insert_one(comment.to_bson())
    comment.id = PydanticObjectId(str(insert_result.inserted_id))

    return comment.to_json()


def _create_comment_for(raw_comment):
    if ("movie_id" in raw_comment):
        raw_comment["movie_id"] = PydanticObjectId(
            raw_comment["movie_id"]
        )
        raw_comment["date"] = dt.datetime.utcnow()

    return Comment(**raw_comment)
