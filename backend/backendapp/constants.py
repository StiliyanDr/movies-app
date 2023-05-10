from types import MappingProxyType

import pymongo


MOVIES_PROJECTION = MappingProxyType({
    "released": 0,
    "last_updated": 0,
})

COMMENTS_PROJECTION = MappingProxyType({
    "name": 1,
    "text": 1,
    "date": 1,
    "_id": 0,
})

COMMENTS_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

MOVIES_PER_PAGE = 15

PAGINATION_SORT = (
    ("year", pymongo.DESCENDING),
    ("_id", pymongo.ASCENDING),
)

DESCENDING_YEAR_SORT = (
    ("year", pymongo.DESCENDING),
)
