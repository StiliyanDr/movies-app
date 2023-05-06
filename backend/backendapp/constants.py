from types import MappingProxyType

import pymongo


MOVIES_PROJECTION = MappingProxyType({
    "released": 0,
    "last_updated": 0,
})

MOVIES_PER_PAGE = 15

PAGINATION_SORT = (
    ("year", pymongo.DESCENDING),
    ("_id", pymongo.ASCENDING),
)
