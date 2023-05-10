import datetime as dt
from typing import Optional

from pydantic import BaseModel, Field

from backendapp import constants as const
from backendapp.models.objectid import PydanticObjectId


class Comment(BaseModel):
    """
    Represents a movie comment.
    """
    name: str
    text: str
    movie_id: PydanticObjectId
    date: dt.datetime
    id: Optional[PydanticObjectId] = Field(None, alias="_id")

    def to_bson(self):
        return self.dict(by_alias=True, exclude_none=True)

    def to_json(self):
        return {
            "name": self.name,
            "text": self.text,
            "date": self.date.strftime(const.COMMENTS_DATE_FORMAT),
            "movie_id": str(self.movie_id),
            "_id": str(self.id),
        }
