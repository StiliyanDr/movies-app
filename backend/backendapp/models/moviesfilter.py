from typing import List, Optional, Tuple

from pydantic import BaseModel


class MoviesFilter(BaseModel):
    """
    Represents a movies query request.
    """
    title: str = ""
    genres: List[str] = []
    length: Optional[Tuple[int, int]] = None
    year: Optional[Tuple[int, int]] = None
