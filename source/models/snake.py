from pydantic import BaseModel


class Snake(BaseModel):
    """Snake description"""
    head: int
    tail: int
