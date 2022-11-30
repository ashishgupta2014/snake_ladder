from pydantic import BaseModel


class Ladder(BaseModel):
    """Ladder descriptions"""
    start: int
    end: int
